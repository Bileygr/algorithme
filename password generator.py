import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/\|!@#$%?&*()_+-=][}{^;.,`~°><:\"'"
password = ""

for c in range(20):
    password += random.choice(chars)
print(password)
