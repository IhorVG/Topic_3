def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    x = int(input("������ ����� �����: "))
    y = int(input("������ ����� �����: "))
    print(f"���({x}, {y}) = {gcd(x, y)}")