# def shortes_distance(arr):

n=int(input("Enter the number of nodes:"))
vertix=[]
for i in range(n):
    arr=list(map(int,input(f"Enter the adjcent value of {i} as 1 remaining 0:").split()))
    vertix.append(arr)
print(vertix)
adj={}
adj_ver=[]
for i in range(n):
    for j in range(n):
        if vertix[i][j]!=0:
            adj_ver.append(j)
        adj[i]={i:adj_ver}
        adj_ver=[]
print(adj)