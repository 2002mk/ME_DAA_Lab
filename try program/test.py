def enc(msg,e,n):
    en=''
    for i in msg:
        in_msg=ord(i)
        en+=str((in_msg**e)%n)+' '
    return en.strip()
        
e=3
msg="hello"
str_=" "
n=55
new_msg=enc(msg,e,n)
for i in new_msg:
    i=str(i)
print(new_msg)