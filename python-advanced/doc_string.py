# def returnSum(*numbers: int):
#     """This function returns the sum of all the arguments"""
#     sum = 0
#     for number in numbers:
#         sum += number
#     return sum

# print(returnSum(1, 2, 3, 4, 5))
# print(returnSum.__doc__)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fibonacci(firstNumber, secondNumerb, limit):
    series = [firstNumber, secondNumerb]
    for i in range(2, limit):
        series.append(series[i-1] + series[i-2])
    return series

print(fibonacci(2, 3, 10))