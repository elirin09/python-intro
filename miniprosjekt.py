import random

svar = random.randint(1, 100)
gjetning = int(input("Gjett et tall mellom 1 og 100: "))
while gjetning != svar:
    if gjetning < svar:
        print("For lavt!")
    else:
        print("For høyt!")
    gjetning = int(input("Gjett igjen: "))
print("Gratulerer! Riktig svar!")
