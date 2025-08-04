names = ['foo', 'john', 'jane', 'doe']

for name in names:
  print(name)
  if name == 'jane':
    print('found jane')
    break

nums = list(range(1, 10))

for num in nums:
  print(num)

n = 100
sum = 0
while n > 0:
  sum = sum + n
  n = n - 10

print(sum)

int(123)
int(12.3)
float(12.3)
float('12.3')
str(123)
bool(1)

n1 = 255
hex(n1)
n2 = 0xFF
n2
print(n1 == n2)
print(hex(n1))