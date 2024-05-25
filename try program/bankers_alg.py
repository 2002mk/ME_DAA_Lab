def proc_in(p,r):
    pr=list()
    for i in range(p):
            aloc=list(map(int, input(f"Enter the aloccation processor{i} for {r}with space between:").split()))
            pr.append(aloc)
    return pr

def max_aloc(p,r):
    m_pr=list()
    for i in range(p):
            aloc=list(map(int, input(f"Enter the aloccation processor{i} for {r}with space between:").split()))
            m_pr.append(aloc)
    return m_pr


p=int(input("Enter the number of processor:"))
r=int(input("Enter the number of resorces:"))
pr=proc_in(p,r)
print(pr)
print("Maximum alocation matrix:")
MaxAlo=max_aloc(p,r)
print(MaxAlo)
av_re=list(map(int, input("Enter the available resource:").split()))
print(av_re)
