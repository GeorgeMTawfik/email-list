import re

my_list = [] # only 4 emailsgit che

x = 4

while x > 0 :

    email = input("enter your email ")
    valid = re.findall(r"[A-Za-z0-9]+[._-]?[A-Za-z0-9]*@[A-Za-z0-9]+\.com" , email)

    if valid :

        my_list.append(email)
        x -= 1

    else :

        print("try again")
        continue

print("#" * 20)

for c , address in enumerate(my_list) :

    print(f"email number {c + 1} is {address}")

print("#" * 20)
