n = int(input())
c = n % 10
b = (n % 100) // 10
a = n // 100
m = a + b + c

print(m)

print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
