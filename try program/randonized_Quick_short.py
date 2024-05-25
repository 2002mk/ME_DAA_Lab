import random
def Ran_quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot = random.choice(arr)
    left = []
    right = []
    pivot_List=[]
    for i in arr:
        if(i < pivot):
            left.append(i)
        elif i<pivot:
            right.append(i)
        else:
            pivot_List.append(i)
    return Ran_quick_sort(left) +pivot_List+ Ran_quick_sort(right)



n=int(input("Enter the number of elements in array:"))
arr=[]
for i in range(0,n):
    a=int(input("Enter the element or array:"))
    arr.append(a)
print("The original Array or List:\n",arr)
r=Ran_quick_sort(arr)
print("Arral after shorted",r)