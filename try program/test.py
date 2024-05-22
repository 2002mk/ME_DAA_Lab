def str_dec(msg):
    int_m=[]
    print("string to decimal")
    for i in msg:
        int_m.append(ord(i))
    print(int_m)
    return int_m

def enc(msg,e,n):
    en=str_dec(msg)
    new_msg=[]
    for i in en:
        new_msg.append((i**e)%n)
    # en=[chr(i) for i in en]
    return new_msg
def dec(new_msg,d,n):
    omsg=[]
    for i in new_msg:
        omsg.append((i**d)%n)
    print("new string list is:",omsg)
    return ''.join(chr(i) for i in omsg)
        
e=17
d=2753
msg="hello"
print(msg)
n=3233
new_msg=[]
new_msg=enc(msg,e,n)
print("encripted Message",new_msg)
or_msg=[]
or_msg=dec(new_msg,d,n)
print(or_msg)