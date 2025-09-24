import re
user_name = input("Enter your name: ")
feedback = input("Enter your feedback: ")

try:
    if user_name == "":
        raise ValueError("Name cannot be empty.")
    if feedback == "":
        raise ValueError("Feedback cannot be empty.")
except ValueError as e:
    print(e)
else:
    print(f"Name: {user_name}, Feedback: {feedback}")
finally:
    print("Thank you for your feedback.")