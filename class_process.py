class Process:
    def __init__(self, process_id, initial_decision, number_of_processes, number_of_failures):
        self.process_id = process_id
        self.initial_decision = initial_decision
        self.number_of_processes = number_of_processes
        self.number_of_failures = number_of_failures
        self.values = self.number_of_processes * [None]

    def send_message(self):
        message = {
            ""
        }
