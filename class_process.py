from class_tree import Tree
from class_node import Node
from itertools import permutations
import message_handler


def majority(nodes):
    counter0 = 0
    counter1 = 0
    for node in nodes:
        if int(node.value) == 1:
            counter1 += 1
        else:
            counter0 += 1
    if counter1 > counter0:
        return 1
    else:
        return 0

class Process:
    def __init__(self, process_id, initial_decision, number_of_processes, am_i_faulty=False):
        self.process_id = process_id
        self.faulty = am_i_faulty
        self.initial_decision = initial_decision
        self.number_of_processes = number_of_processes
        self.root = Node(value=self.initial_decision, path="", leaf_flag=True)
        self.tree = Tree(self.root)
        self.level = len(self.root.path)

    # generate all the message ( all leafs + values + sender ( process_id )
    def send_messages(self):
        leaf_nodes = self.tree.get_leafs()
        messages = []
        for node in leaf_nodes:
            if not self.faulty:
                message = "value" + str(node.value) + "path" + str(node.path) + "sender" + str(self.process_id)
                messages.append(message)
            else:
                message = "this message is garbage"
                messages.append(message)
        return messages

    # generate the next level leafs of the tree
    def generate_next_level_nodes(self):
        self.level += 1
        digits = ''.join(str(i) for i in range(1, self.number_of_processes+1))
        next_level_paths = [''.join(p) for p in permutations(digits, self.level)]
        nodes = []
        for path in next_level_paths:
            nodes.append(Node(value=None, path=path, leaf_flag=True))
        return nodes

    # before generating new level of nodes all the old nodes should be non leaf
    def update_leafs(self):
        for node in self.tree.get_leafs():
            node.leaf_flag = False


    def update_tree(self, messages):
        valid_messages = message_handler.process_nested_message_lists(messages) # validation all messages as string
        messages_as_dict = [] # extract all messages to dict
        for message in valid_messages:
            messages_as_dict.append(message_handler.extract_message_parts(message))
        self.update_leafs()
        # now all the messages are in dict type
        new_level_nodes = self.generate_next_level_nodes()
        for node in new_level_nodes:
            value = None
            for message in messages_as_dict:
                if message["sender"] == node.path[-1] and message["path"] == node.path[:-1]:
                    value = message["value"]
                    break
            node.value = value
            self.tree.list_of_nodes.append(node)


    def decision_making(self):
        for node in self.tree.list_of_nodes:
            if node.leaf_flag:
                if node.value is None or node.value == "None":
                    node.value = 0
        for node in reversed(self.tree.list_of_nodes):
            if not node.leaf_flag:
                childes = self.tree.get_childes(node)
                node.value = majority(childes)
        return self.root.value

    def print_final_info(self):
        values = []
        for node in self.tree.list_of_nodes:
            values.append(node.value)
        return values
