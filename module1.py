import re

my_list = []

x = 5

while x > 0 :

    email = input("enter your email ")
    valid = re.findall(r"[A-Za-z0-9]+[._-]?[A-Za-z0-9]*@[A-Za-z0-9]+\.com" , email)

    if valid :

        my_list.append(email)
        x -= 1

    else :

        print("try again")
        continue

print("the emails are")
print("#" * 20)

for c , address in enumerate(my_list) :

    print(f"email number {c + 1} is {address}")

print("#" * 20)
print("5 valid emails stored successfully")