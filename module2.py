''' printing 5 valin emails user entering '''

import re

my_list = []

x = 5

while x > 0 :

    user = input("enter your username ")
    

    
    my_list.append(user)
    x -= 1

print("the usernames are")
print("#" * 20)

for c , address in enumerate(my_list) :

    print(f"username number {c + 1} is {address}")

print("#" * 20)
print("five valid usernames have been entered")
