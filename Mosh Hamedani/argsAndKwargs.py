def multuply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return number


print(multuply(1, 3, 4, 3))

# def save_user(**user):
#     print(user)
#1
# save_user(
#     id=1,
#     name="adib",
#     age=12
# )