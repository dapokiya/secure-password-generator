print ("Hye..!")
print("i am password generator")
length=int(input("input your password length"))

symbol=raw_input("password in spacial symbol..like @,#,%,$...etc(if yes then press y other pree n) ")
number=raw_input("password in digit ..like 1,2,3,4,etc ?")
lcase=raw_input("password in lower case ..like a,b,c,d,etc ?")
ucase=raw_input("password in upper case ..like A,B,C,D,etc ?")

list_symbol=["@","#","$","%","&","*"]
list_number=[0,1,2,3,4,5,6,7,8,9]
list_lcase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
list_ucase=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


st="y"
password=[]
n=length
import random
i=0
x=0
while(length>0):
    
    if symbol==st and length<=n and length>0:
        z=random.choice(list_symbol)
        password.append(z)
        length-=1
    
    

    if number==st and length<=n  and length>0:
        z=random.choice(list_number)
        password.append(z)
        length-=1
    

    
    if lcase==st and length<=n  and length>0:
        z=random.choice(list_lcase)
        password.append(z)
        length-=1



    if ucase==st and length<=n  and length>0:
        z=random.choice(list_ucase)
        password.append(z)
        length-=1



    else:
        pass

print("your password is")
for i in password:
    print i; 



