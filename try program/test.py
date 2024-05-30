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

def need_rec(pr,MaxAlo):
      need_res=[]
      for i in range(int(len(pr))):
            for j in range(int(len(i))):
                  need=list(pr[i][j]+MaxAlo[i][j])
            need_res.append(need)
      return need_res

p=int(input("Enter the number of processor:"))
r=int(input("Enter the number of resorces:"))
pr=proc_in(p,r)
print(pr)
print("Maximum alocation matrix:")
MaxAlo=max_aloc(p,r)
print(MaxAlo)
av_re=list(map(int, input("Enter the available resource:").split()))
print(av_re)
need_res=sum(pr,MaxAlo)
print("the needed Resorc:\n",need_res)