alder = int (input("hvor gammel er du? "))

if alder < 6:
    print ("gratis adgang")
elif alder < 18:
    print ("ungdomspris")
elif alder < 67:
    print ("voksenpris")   
else:
    print("pensjonistpris") 
