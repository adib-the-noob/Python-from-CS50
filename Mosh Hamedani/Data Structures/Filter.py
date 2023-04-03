items =[
    ("Product1", 10),
    ("Product4", 17),
    ("Product6", 16),
    ("Product5", 14),   
]

x = list(filter(lambda item:item[1] > 13, items))
for item in x:
    print(item)