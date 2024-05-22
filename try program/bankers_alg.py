def proc_in(p):
    pr=list()
    for i in range(p):
        pr.append(list(map(int,input(f"Enter the processor{i}:").split())))
    return pr


p=int(input("Enter the number of processor:"))
r=int(input("Enter the number of resorces:"))

