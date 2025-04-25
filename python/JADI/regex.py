import re

pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$'
email = input("Enter email: ")

if re.match(pattern, email):
    print("OK")
else:
    print("WRONG")
