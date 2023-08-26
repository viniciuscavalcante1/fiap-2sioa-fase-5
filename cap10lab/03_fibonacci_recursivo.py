def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return n
    return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)