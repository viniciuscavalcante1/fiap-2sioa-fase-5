def fibonacci_iterativo(n):
    f = -1
    fib_menos_1 = 1
    fib_menos_2 = 0
    for i in range(3, n + 1):
        f = fib_menos_1 + fib_menos_2
        fib_menos_2 = fib_menos_1
        fib_menos_1 = f
    return f