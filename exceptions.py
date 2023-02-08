def main():
    x = get_value()
    print(f"Value of x is {x}")

def get_value():
    while True:
        try:
            name = int(input("Enter your name: "))
        except ValueError:
            print("X is not a number")
        else:
            return name
    
main()