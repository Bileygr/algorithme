from random import randint
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/1234567890-=àç^è;é.,\!@#$%?&*()_+ÀÇ¨È:É"
characters_length = len(characters)
password=""
i=0
while i!=17:
    position = randint(0,characters_length-1)
    password += characters[position]
    i=i+1
print(password)
