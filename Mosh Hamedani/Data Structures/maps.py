items =[
    ("Product1", 10),
    ("Product4", 17),
    ("Product6", 16),
    ("Product5", 14),
]

prices = []
for item in items:
    prices.append(item[1])

new_price = map(lambda item:item[1], items)
print(new_price)
for item in new_price:
    print(item)