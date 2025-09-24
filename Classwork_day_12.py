import re
title_of_book = input("Enter the title of the book: ")
year_of_publication = input("Enter the year of publication: ")

try:
    if not re.fullmatch(r"[A-Za-z ]+", title_of_book):
        raise ValueError("Title must contain only alphabetic characters and spaces.")
    if not re.fullmatch(r"(19/20)\d{2}", year_of_publication):
        raise ValueError("Year must be a four-digit number starting with 19 or 20.")
except ValueError as e:
    print(e)
else:
    print(f"Title: {title_of_book}, Year of Publication: {year_of_publication}")    
finally:
    print("Validation complete.")
