def nsd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))

print("НСД:", nsd(x, y))
