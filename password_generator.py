import random

password = []
chars = r'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()'
length = 64

for i in range(length):
    password.append(random.choice(chars))

str_password = ''.join(password)
print(str_password)
