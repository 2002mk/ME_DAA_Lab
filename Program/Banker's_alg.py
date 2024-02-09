def main():
    # Get input from the user
    n = int(input("Enter the number of processes: "))  # Number of processes
    m = int(input("Enter the number of resource types: "))  # Number of resource types

    # Allocation Matrix
    print("Allocation matrix")
    alloc = []
    for i in range(n):
        alloc.append(list(map(int, input(f"Enter allocation for Process {i}: ").split())))

    # MAX Matrix
    print("MAX matrix")
    max = []
    for i in range(n):
        max.append(list(map(int, input(f"Enter MAX for Process {i}: ").split())))

    # Available Resources
    avail = list(map(int, input("Enter the available resources: ").split()))

    # Initialization
    f = [0] * n
    ans = [0] * n
    ind = 0
    for k in range(n):
        f[k] = 0

    need = [[0 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]

    # Applying Banker's Algorithm
    for k in range(n):
        for i in range(n):
            if f[i] == 0:
                flag = 0
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = 1
                        break

                if flag == 0:
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1

    # Determine whether the system is safe or unsafe
    safe = all(f)
    if safe:
        print("The system is in a safe state.")
        print("The safe sequence:")
        for i in range(n - 1):
            print("P", ans[i], " -> ", sep="", end="")
        print("P", ans[n - 1], sep="")
    else:
        print("The system is in an unsafe state.")


if __name__ == "__main__":
    main()