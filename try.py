while True:
    try:
        tall = int(input("Skriv inn et heltall: "))
        break
    except ValueError:
        print("ugyldig input. Prøv igjen.")

print(f"Du skrev: {tall}")        