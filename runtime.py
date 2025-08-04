#!/usr/bin/env python3

print('runtime python')

a = 'ABC'

b = a

a = '123'

print(b)

# 除法
print(100 / 3) # 33.333

print(100 // 3) # 33

# 字符编码转换

print(ord('A'), chr(66))

b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')

age = 90

if age > 3:
    print('adult')
elif age > 18:
    print('young')
else :
    print('child')


s = input('birth:')
birth = int(s)
if birth > 2000:
    print('00后')
else:
    print('00前')


# match
match age:
    case 18:
        print('18')
    case 19:
        print('19')
    case _:
        print('other')

match age:
    case x if x > 18:
        print('adult')
    case x if x > 3:
        print('young')
    case 1 | 2 | 3:
        print('child')

args = ['a', 'b', 'c']

match args:
    case ['a']:
        print('a')
    case ['a', other, *rest]:
        print('a', other, rest)
    case __:
        print('other')

