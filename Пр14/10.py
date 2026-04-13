def process(a: int, b: int, *args: int, **kwargs: int) -> int:
    total = a + b + sum(args) + sum(kwargs.values())
    return total

print(process(1, 2, 3, 4, x=5, y=6))