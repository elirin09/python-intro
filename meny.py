def vis_meny():
    print("1) legg til tall")
    print("2) vis sum")
    print("q) avslutt")

tall_liste = []

while True:
    vis_meny()
    valg = input("Velg: ").strip().lower()

    if valg == "1":
        try:
            t = int(input("tall: "))
            tall_liste.append(t)
        except ValueError:
            print("dette var ikke et heltall. Prøv igjen.")
    elif valg == "2":
        print(f"Sum: {sum(tall_liste)}")
    elif valg == "q":
        break
    else:
        print("ugyldig valg.")