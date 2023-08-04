def even_odd_filter(**kwargs):
    result = {}
    for type_numbers, numbers in kwargs.items():
        if type_numbers == "even":
            result[type_numbers] = [x for x in numbers if x % 2 == 0]
        elif type_numbers == "odd":
            result[type_numbers] = [x for x in numbers if x % 2 != 0]
    return dict(sorted(result.items()))

print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))