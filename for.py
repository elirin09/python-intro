spill = []

for i in range(5):
    s = input(f"Skriv inn favorittspill {i + 1}: ")
    spill.append(s)

print("Dine favorittspill")
for i in range(len(spill)):
    print(f"{i + 1}. {spill[i]}")
    