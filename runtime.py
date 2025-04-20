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