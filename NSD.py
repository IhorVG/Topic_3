def nsd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x = int(input("Введіть перше число 12345678: "))
y = int(input("Введіть друге число 12345678: "))

print("НСД:", nsd(x, y))
