class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        else:
            element = self.sequence[self.current_index % len(self.sequence)]
            self.current_index += 1
            self.number -= 1
            return element


result = sequence_repeat('I Love Python', 3)
for item in result:
 print(item, end ='')
