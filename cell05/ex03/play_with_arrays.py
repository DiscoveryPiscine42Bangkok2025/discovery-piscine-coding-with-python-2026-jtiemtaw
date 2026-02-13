numbers = [2, 8, 9, 48, 8, 22, -12, 2]

print(numbers)

new_numbers = []

for n in numbers:
    new_numbers.append(n + 2)

result = set(new_numbers)

print(result)
