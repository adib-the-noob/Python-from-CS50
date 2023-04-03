items =[
    ("Product1", 10),
    ("Product4", 17),
    ("Product6", 16),
    ("Product5", 14),
]

items.sort(key=lambda item:item[1])
print(items)