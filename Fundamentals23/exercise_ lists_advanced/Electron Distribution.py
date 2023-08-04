electrons = int(input())

result = []

while electrons > 0:
    n = len(result) + 1
    shell = min(2 * (n ** 2), electrons)
    result.append(shell)
    electrons -= shell

print(result)
