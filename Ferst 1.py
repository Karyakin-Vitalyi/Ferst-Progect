import random


a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'abcdefghijklmnopqrstuvwxyz'
c = '1234567890/'
d = '[]{}?.,!@#$%^&*()_+|-><?/*+'

res = a + b + c + d

password = ''.join(random.sample(res, 12))
print("Генератор паролей:")
print(password)

