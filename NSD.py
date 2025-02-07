def gcd(a, b):  
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    print(f"({x}, {y}) = {gcd(x, y)}")

def gcd2(a, b):
  while b:
    a, b = b, a % b
  return a

a = 12
b = 45

print(gc2d(a,b))

