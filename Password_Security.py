#check password security

num = "0123456789"
symble = r'''`!@#$%^&*(){}[]+-*/\|'";:?,.<>'''
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = input("Enter a password:")
length = len(password)
while length==0 or password.isspace():
    password = input("Re-enter a password:")
    length = len(password)

lenflag = 0
#check length
if length <= 8:
    lenflag = 1
elif 8 < length < 16:
    lenflag = 2
else:
    lenflag = 3

#check chars
contflag = 0
for i in password:
    if i in num:
        contflag+=1
        break
for i in password:
    if i in symble:
        contflag+=1
        break
for i in password:
    if i in char:
        contflag+=1
        break

print("Security level:\n")
if lenflag == 1 or contflag==1:
    print("low")
elif lenflag == 2 or contflag == 2:
    print("Mid")
else:
    print("High")
    
