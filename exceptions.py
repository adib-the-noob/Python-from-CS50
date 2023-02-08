def main():
    x = get_value("What is the value of X?")
    print(f"Value of x is {x}")

def get_value(prompt):
    while True:
        try:
            name = int(input(prompt))
        except ValueError:
            print("X is not a number")
        else:
            return name
    
main()

# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     pass