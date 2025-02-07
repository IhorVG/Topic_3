def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

a = 12
b = 45

print(gcd(a,b))