
grocery_list = ["milk", "bread", "eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_last_item():
    if grocery_list:  
        grocery_list.pop()
display_item = lambda item: print(f"Item: {item}")
def count_characters(items):
    if not items:  
        return 0
    return len(items[0]) + count_characters(items[1:])
print("Initial list:")
for i in grocery_list:
    display_item(i)

print("\nAdding 'butter'...")
add_item("butter")

print("\nList after adding:")
for i in grocery_list:
    display_item(i)

print("\nRemoving last item...")
remove_last_item()

print("\nList after removing last item:")
for i in grocery_list:
    display_item(i)

print("\nTotal characters in list:", count_characters(grocery_list))
