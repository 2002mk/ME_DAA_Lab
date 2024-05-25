import random
def RQS(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=random.choice(arr)
    left=[]
    right=[]
    for i in range(0,n):
        if(arr[i] > pivot):
            left.append(i)
        else:
            right.append(i)
    return RQS(left) +[pivot]+ RQS(right)



n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(0,n):
    a=int(input("Enter the element or array:"))
    arr.append(a)
print(arr)
r=RQS(arr)
print(r)