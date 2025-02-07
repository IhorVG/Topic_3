def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    x = int(input("¬вед≥ть перше число: "))
    y = int(input("¬вед≥ть друге число: "))
    print(f"Ќ—ƒ({x}, {y}) = {gcd(x, y)}")