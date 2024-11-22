from class_tree import Tree
from class_node import Node
from itertools import permutations

class Process:
    def __init__(self, process_id, initial_decision, number_of_processes, number_of_failures):
        self.process_id = process_id
        self.initial_decision = initial_decision
        self.number_of_processes = number_of_processes
        self.number_of_failures = number_of_failures
        self.root = Node(value=self.initial_decision, path="", leaf_flag=True)
        self.tree = Tree(self.root)
        self.level = len(self.root.path)

    def send_messages(self):
        leaf_nodes = self.tree.get_leafs()
        messages = []
        for node in leaf_nodes:
            message = {
                "value": node.value,
                "path": node.path,
                "sender": self.process_id
            }
            messages.append(message)
        return messages

    def check_message(self, message):
        path = message["path"] + str(message["sender"])
        # check range of id's in path and uniq id's in path
        for node_id in path:
            if node_id not in range(1, self.number_of_processes + 1):
                return False
        # the message shouldn't include duplicated id in path
        seen_ids_in_path = set()
        for node_id in path:
            if not node_id.isdigit() or node_id in seen_ids_in_path:
                return False
            else:
                seen_ids_in_path.add(node_id)
        return True

    def receive_messages_validator(self, messages):
        # validation of messages
        valid_messages = []
        for message in messages:
            if self.check_message(message):
                valid_messages.append(message)
        return valid_messages

    def generate_next_level_nodes(self):
        self.level += 1
        digits = ''.join(str(i) for i in range(1, self.number_of_processes+1))
        next_level_paths = [''.join(p) for p in permutations(digits, self.level)]
        nodes = []
        for path in next_level_paths:
            nodes.append(Node(value=None, path=path, leaf_flag=True))
        return nodes

    def update_tree(self, messages):
        valid_messages = self.receive_messages_validator(messages)
        next_level_nodes = self.generate_next_level_nodes()
        # update value of nodes if they are in valid messages
        for node in next_level_nodes:
            for message in valid_messages:
                if message["path"]+str(message["sender"]) == node.path:
                    node.value = message["value"]
            self.tree.list_of_nodes.append(node)
        # update leaf flags
        for node in self.tree.list_of_nodes:
            if len(node.path) < self.level:
                node.leaf_flag = False

    def decision_making(self):



