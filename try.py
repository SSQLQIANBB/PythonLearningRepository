# 错误处理

# try:
#   print('try python')
#   r = 1 / 0
#   print('this will not be printed', r)
# except ZeroDivisionError as e:
#   print('error:', e)
# finally:
#   print('finally block executed')


# 多个错误捕获
# try:
#   r = 10 / 0
#   b = 1 / int('a')

# except ZeroDivisionError as e:
#   print('ZeroDivisionError:', e)
# except ValueError as e:
#   print('ValueError:', e)
# finally:
#   print('finally block executed')
# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
  r = 10 / 10
  b = 1 / 1

except ZeroDivisionError as e:
  print('ZeroDivisionError:', e)
except ValueError as e:
  print('ValueError:', e)
else:
  print('No errors occurred, result:', r, b)
finally:
  print('finally block executed')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# try:
#   foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeError as e:
#     print('UnicodeError')

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了

# 记录错误

import logging

try:
    r = 10 / 0
except ZeroDivisionError as e:
    logging.error('Error occurred: %s', e, exc_info=True)

print('end')

# raise
# raise语句可以用来抛出一个错误，通常在except语句块中使用。
# 例如，如果捕获到一个错误，但不想处理它，而是将它重新抛出，可以使用raise语句：

class CustomError(ValueError):
    pass

try:
    r = 10 / 0
except ZeroDivisionError as e:
    print('Caught an error:', e)
    raise CustomError('A custom error occurred: %s' % e)


print('end')