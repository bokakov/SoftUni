def grocery_store(**kwargs):
    result = ""
    for product_name, quantity in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
        result += f"{product_name}: {quantity}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))