import os
item_name = input("Enter the item name:")
if os.path.exists("items.txt"):
    with open("items.txt","a") as f:
        f.write(item_name + "\n")
else:
    with open("items.txt","w") as f:
        f.write(item_name + "\n")   

with open("items.txt","r") as f:
    items = f.readlines()
    print("Items in the file:")
    for item in items:
        print(item.strip())

