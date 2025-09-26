filename = "students.txt"

try:
    with open(filename, "r") as f:
        existing_names = f.read().strip()
        if existing_names:
            print("Existing student names:")
            print(existing_names)
        else:
            print("No student names found.")
except FileNotFoundError:
    print("No student names found.")

while True:
    try:
        count = int(input("How many student names do you want to add? "))
        if count < 1:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

new_names = []
for i in range(count):
    name = input(f"Enter name of student {i+1}: ").strip()
    if name:
        new_names.append(name)

with open(filename, "a") as f:
    for name in new_names:
        f.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as f:
    print(f.read().strip())