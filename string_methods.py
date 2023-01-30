name = input("Enter your name: ")
# print(f"Your name is {name}")

# String methods
# for removing whitespace

name = name.strip()
print(f"Your name is {name}")

# for capitalizing the first letter of the string
name = name.capitalize()
print(f"Your name is {name}")

# for capitalizing all the letters of the string
name = name.upper()
print(f"Your name is {name}") 

# for capitalizing all the first letters of all the workds in the string
name = name.title()
print(f"Your name is {name}")

name = name.strip().upper()
print(f"Your name is {name}")