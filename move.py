from re import I


Hudvar = True
Heloszoba = False
Hnappali = False
Hszuloszoba = False
Hgyerekszoba = False
Hkonyha = False
Qmennyelhaza = 1
Qegyelesaludjal1 = 0
Qegyelesaludjal2 = 0
Ikannal = False
Ikulcs = True

print("Megérkeztél egy hosszú nap után haza és meg álsz az udvaron.")

for i in range(0,9999,1):
    print("Mit akarsz csinálni?")
    print("(1) Menni egy szobába")
    print("(2) Megnézed az inventoryt")
    print("(3) Küldetések")
    action = int(print("Kérem adja meg azt a számot amit választani akar!: "))
    if action == 3:
        if Qmennyelhaza == True:
            print("Mennyél be a házba.")
        if Qegyelesaludjal1 == True:
            print("Egyél valamit a konyhában.")
        if Qegyelesaludjal2 == True:
            print("Aludjál egyet a szobádban.")
        action = 0
    elif action == 2:
        if Ikannal == False and Ikulcs == False:
            print("Nincsen nálad semmi")
        if Ikulcs == True:
            print("Nálad van a ház kulcsod.")
        if Ikannal == True:
            print("Van nálad egy kanál")
        action = 0
    elif action == 1:
        if Hudvar == True:
            print("Hova akarsz menni?")
            print("(1) Előszoba")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            if action == 1:
                print("Oda mész az ajtóhoz de zárva van.")
                if Ikulcs == True:
                    print("Elő veszed a kulcsod a zsebedből és kinyitod az ajtót és be mész az előszobába.")
                    Hudvar = False
                    Heloszoba = True
                    Qmennyelhaza += 1
                    Qegyelesaludjal1 += 1
                else:
                    print("Nincsen kulcsod")
    else:
        print("Nem megfelelő számot adott meg!")