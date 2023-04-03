items =[
    ("Product1", 10),
    ("Product4", 17),
    ("Product6", 16),
    ("Product5", 14),
]

def sort_items(item):
    return item[1]

items.sort(key=sort_items)
print(items)