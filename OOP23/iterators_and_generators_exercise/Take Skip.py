class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.generated_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_count >= self.count:
            raise StopIteration
        else:
            num = self.current
            self.current += self.step
            self.generated_count += 1
            return num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)