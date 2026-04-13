def average(*args: float) -> float:
    return sum(args) / len(args) if args else 0.0

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)
print(middle)
print(last)