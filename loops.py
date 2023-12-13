

products = [
    {"price": 15},
    {"price": 45},
    {"price": 323},
    {"price": 15},
    {"price": 15},
    {"price": 4324},
    {"price": 15},
    {"price": 4324},
    {"price": 15},
    {"price": 15},
    {"name": "chicken"},
    {"price": 15},
    {"price": 15},
]

summ = 0
for product in products:
    price = product.get("price", 0)

    summ += price

print(summ)