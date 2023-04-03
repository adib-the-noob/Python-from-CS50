list1 = [1, 2, 3]
list2 = [30, 50, 100]

y = list(zip("+-+", "abc", list1, list2))
for x in y:
    print(x)
