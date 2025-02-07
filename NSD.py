def nsd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == "__main__":
    x, y = map(int, input("Enter two numbers: ").split())
    print("NSD:", gcd(x, y))
