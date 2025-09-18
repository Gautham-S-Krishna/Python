# Pet Store Inventory Program

# Create the Empty List
inventory = []

# Function to add items
def add_item(item):
    inventory.append(item)

# Recursive function to count items
def count_items(items):
    if not items:  # Base case: if list is empty
        return 0
    return 1 + count_items(items[1:])  # Recursive step

# Lambda function to display items
show_item = lambda item: print(f"Item in Stock: {item}")

# Main function
def main():
    # Add items
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    # Display items
    print("Inventory List:")
    for item in inventory:
        show_item(item)

    # Count and display total number of items
    total = count_items(inventory)
    print(f"\nTotal number of items in stock: {total}")

# Run the program
main()
