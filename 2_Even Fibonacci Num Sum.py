def fibonacci(lim):
    a, b = 0, 1
    sequence = []
    while a <= lim:
        if a % 2 == 0:
            sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(4000000))
print(sum(fibonacci(4000000)))