def negative_vs_positive(data):
    min_number = data.index(min([x for x in data if x > 0]))
    positive_numbers = sum(data[min_number:])
    negative_numbers = sum(data[:min_number])

    if positive_numbers > abs(negative_numbers):
        text = "The positives are stronger than the negatives"
    else:
        text = "The negatives are stronger than the positives"
    return f"{negative_numbers}\n{positive_numbers}\n{text}"


input_numbers = sorted(int(x) for x in input().split())
print(negative_vs_positive(input_numbers))
