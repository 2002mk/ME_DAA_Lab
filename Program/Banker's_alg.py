class BankerAlgorithm:
    def __init__(self, max_resources):
        self.max_resources = max_resources
        self.current_resources = max_resources.copy()
        self.allocated = []
        self.needed = []
        self.available = max_resources.copy()
        self.processes = len(max_resources)
        self.finished = [False] * self.processes

    def add_process(self, allocated_resources, max_needed_resources):
        self.allocated.append(allocated_resources)
        self.needed.append(max_needed_resources)
        self.available = [self.available[i] - allocated_resources[i] for i in range(len(allocated_resources))]

    def is_safe_state(self, process_sequence=None):
        if process_sequence is None:
            process_sequence = []
        work = self.available.copy()
        finish = self.finished.copy()

        while True:
            found = False
            for i in range(self.processes):
                if not finish[i] and all(self.needed[i][j] <= work[j] for j in range(len(work))):
                    work = [work[j] + self.allocated[i][j] for j in range(len(work))]
                    finish[i] = True
                    process_sequence.append(i)
                    found = True

            if not found:
                break

        return all(finish), process_sequence

    def request_resources(self, process_id, resources_requested):
        if any(resources_requested[i] > self.needed[process_id][i] for i in range(len(resources_requested))):
            print("Error: Requested resources exceed maximum needed resources")
            return

        if any(resources_requested[i] > self.available[i] for i in range(len(resources_requested))):
            print("Error: Insufficient available resources to fulfill request")
            return

        self.available = [self.available[i] - resources_requested[i] for i in range(len(resources_requested))]
        self.allocated[process_id] = [self.allocated[process_id][i] + resources_requested[i] for i in range(len(resources_requested))]
        self.needed[process_id] = [self.needed[process_id][i] - resources_requested[i] for i in range(len(resources_requested))]

        safe, _ = self.is_safe_state()
        if safe:
            print("Resources allocated successfully. System in safe state.")
        else:
            print("Resources allocated. System in unsafe state. Rollback changes.")
            self.available = [self.available[i] + resources_requested[i] for i in range(len(resources_requested))]
            self.allocated[process_id] = [self.allocated[process_id][i] - resources_requested[i] for i in range(len(resources_requested))]
            self.needed[process_id] = [self.needed[process_id][i] + resources_requested[i] for i in range(len(resources_requested))]

    def release_resources(self, process_id, resources_released):
        if any(resources_released[i] > self.allocated[process_id][i] for i in range(len(resources_released))):
            print("Error: Released resources exceed allocated resources")
            return

        self.available = [self.available[i] + resources_released[i] for i in range(len(resources_released))]
        self.allocated[process_id] = [self.allocated[process_id][i] - resources_released[i] for i in range(len(resources_released))]
        self.needed[process_id] = [self.needed[process_id][i] + resources_released[i] for i in range(len(resources_released))]

    def display_state(self):
        print("Maximum resources:", self.max_resources)
        print("Allocated resources:", self.allocated)
        print("Needed resources:", self.needed)
        print("Available resources:", self.available)

# Example usage:
max_resources = [10, 5, 7]
banker = BankerAlgorithm(max_resources)

banker.add_process([0, 1, 0], [7, 5, 3])
banker.add_process([2, 0, 0], [3, 2, 2])
banker.add_process([3, 0, 2], [9, 0, 2])
banker.add_process([2, 1, 1], [2, 2, 2])
banker.add_process([0, 0, 2], [4, 3, 3])

banker.display_state()

banker.request_resources(1, [1, 0, 2])
banker.display_state()

banker.release_resources(3, [1, 0, 1])
banker.display_state()
