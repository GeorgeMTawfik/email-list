import re

my_list = []

x = 5

while x > 0 :

    email = input("enter your email ")
    valid = re.findall("[A-z0-9]+/.?|-?|_?@[A-z0-9]+.com", email)

    if valid :

        my_list.append(email)
        x -= 1

    else :

        print("try again")
        continue


for c , address in enumerate(my_list) :

    print(f"email number {c + 1} is {address}")
