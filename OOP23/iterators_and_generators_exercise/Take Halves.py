def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        result = []
        for item in seq:
            result.append(item)
            if len(result) == n:
                break
        return result

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
