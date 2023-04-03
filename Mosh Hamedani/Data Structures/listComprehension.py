items =[
    ("Product1", 10),
    ("Product4", 17),
    ("Product6", 16),
    ("Product5", 14),
]
x = [item[1] for item in items if item[1] > 15]
print(x)