def avalia(x, y, n):
    print("oi")
    if x < y:
        return avalia(x + n, y - 1, n + 2)
    else:
        return y


print(f"resultado da funcao: {avalia(2, 15, 3)}")