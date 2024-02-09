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

# Function to take user input for resources
def get_resource_input(resource_name):
    resources = input(f"Enter space-separated {resource_name} resources: ").strip().split()
    return [int(resource) for resource in resources]

# Function to take user input for processes
def get_process_input(num_processes):
    allocated_resources = [get_resource_input(f"allocated resources for process {i+1}") for i in range(num_processes)]
    max_needed_resources = [get_resource_input(f"maximum needed resources for process {i+1}") for i in range(num_processes)]
    return allocated_resources, max_needed_resources

# Example usage:
def main():
    num_resources = int(input("Enter the number of resources: "))
    max_resources = get_resource_input("maximum")
    banker = BankerAlgorithm(max_resources)

    num_processes = int(input("Enter the number of processes: "))
    allocated_resources, max_needed_resources = get_process_input(num_processes)

    for i in range(num_processes):
        banker.add_process(allocated_resources[i], max_needed_resources[i])

    banker.display_state()

    while True:
        action = input("Enter action (request/release/exit): ").strip().lower()
        if action == "exit":
            break
        elif action == "request":
            process_id = int(input("Enter process ID: ")) - 1
            resources_requested = get_resource_input("requested")
            banker.request_resources(process_id, resources_requested)
        elif action == "release":
            process_id = int(input("Enter process ID: ")) - 1
            resources_released = get_resource_input("released")
            banker.release_resources(process_id, resources_released)
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
