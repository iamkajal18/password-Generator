import random
letter=["a","q","w","r","t","y","u"]
number=['1','2','3','4','5','6','7']
symbol=['!','@','#','%','*','^']

print("Welcome to password Generator!")

letters=int(input("how many lettters would to like in your password:"))
numbers=int(input("how many numbers would to like in your password:"))
symbols=int(input("how many symbols would to like in your password:"))

password = ""
for char in range(1,letters+1):
    password +=random.choice(letter)
for char in range(1,numbers+1):
   password +=random.choice(number)
for char in range(1,symbols+1):
    password += random.choice(symbol)        

print(password)