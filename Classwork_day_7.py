# Initial Grocery List
grocery_list = ["milk", "bread", "eggs"]

# Add Item Function
def add_item(item):
    grocery_list.append(item)

# Remove Last Item Function
def remove_last_item():
    if grocery_list:  # check if list is not empty
        grocery_list.pop()

# Lambda Function for Display
display_item = lambda item: print(f"Item: {item}")

# Recursive Character Count Function (Bonus)
def count_characters(items):
    if not items:  # base case: empty list
        return 0
    return len(items[0]) + count_characters(items[1:])

# -----------------------
# Example Usage:
# -----------------------
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
