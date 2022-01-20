Hudvar = True
Heloszoba = False
Hnappali = False
Hszuloszoba = False
Hgyerekszoba = False
Hkonyha = False
Qmennyelhaza = True
QmennyelhazaF = False
Qegyelesaludjal1T = False
Qegyelesaludjal1 = False
Qegyelesaludjal1F = False
Qegyelesaludjal2 = False
Qegyelesaludjal2F = False
Ikannal = False
Ikulcs = True
#H = hely    I = item     Q = quest  F = elvégeet  T = trigger ekkor kapja meg

print("Megérkeztél egy hosszú nap után haza és meg álsz az udvaron.")

for i in range(0,9999,1):
    print()
    print("Mit akarsz csinálni?")
    print("(1) Menni egy szobába")
    print("(2) Megnézed az inventoryt")
    print("(3) Küldetések megnézése")
    print("(4) Körbe nézel hol vagy")
    action = int(input("Kérem adja meg azt a számot amit választani akar!: "))
    print()
    if action == 3:
        if Qmennyelhaza == True:
            print("Mennyél be a házba.")
        if Qegyelesaludjal1 == True and Qegyelesaludjal1F == False:
            print("Nézzél körben a konyhába és egyél valamit.")
        if Qegyelesaludjal2 == True and Qegyelesaludjal2F == False:
            print("Aludjál egyet a szobádban.")
        action = 0
    elif action == 2:
        if Ikannal == False and Ikulcs == False:
            print("Nincsen nálad semmi")
            print()
        if Ikulcs == True:
            print("Nálad van a ház kulcsod.")
            print()
        if Ikannal == True:
            print("Van nálad egy kanál")
            print()
        action = 0
    elif action == 1:
        if Hudvar == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Előszoba")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("Oda mész az ajtóhoz de zárva van.")
                if Ikulcs == True:
                    print("Elő veszed a kulcsod a zsebedből és kinyitod az ajtót és be mész az előszobába.")
                    Hudvar = False
                    Heloszoba = True
                    Qmennyelhaza = False
                    QmennyelhazaF = True
                    Qegyelesaludjal1 = True
                    if Qegyelesaludjal1 == True and Qegyelesaludjal1F == False and Qegyelesaludjal1T == False:
                        print("Éhes vagy, lehet meg kéne néznem mi van a hütöben. (Nézd meg a küldetéseidet!)")
                        Qegyelesaludjal1T = True
                else:
                    print("Nincsen kulcsod")
        elif Heloszoba == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Udvar")
            print("(2) Nappali")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("Úgy döntesz ki mész az udvarra.")
                Heloszoba = False
                Hudvar = True
            elif action == 2:
                print("Bementél a nappaliba.")
                Heloszoba = False
                Hnappali = True
        elif Hnappali == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Elöszoba")
            print("(2) Konyha")
            print("(3) Felnött szoba")
            print("(4) Gyerekszoba")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("El mentél az elöszobába")
                Hnappali = False
                Heloszoba = True
            elif action == 2:
                print("Be mentél a konyhába.")
                Hnappali = False
                Hkonyha = True
            elif action == 3:
                print("Be mentél a Felnött szobába.")
                Hnappali = False
                Hszuloszoba = True
            elif action == 4:
                print("Be mentél a Gyerekszobába.")
                Hnappali = False
                Hgyerekszoba = True
        elif Hkonyha == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Nappali")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("Vissza mentél a nappaliba.")
                Hkonyha = False
                Hnappali = True
        elif Hszuloszoba == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Nappali")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("Vissza mentél a Nappaliba.")
                Hszuloszoba = False
                Hnappali = True
        elif Hgyerekszoba == True:
            print()
            print("Hova akarsz menni?")
            print("(1) Nappali")
            action = 0
            action = int(input("Kérem adja meg azt a számot ahova menni akar: "))
            print()
            if action == 1:
                print("Vissza mentél a Nappaliba.")
                Hgyerekszoba = False
                Hnappali = True

    elif action == 4:
        action = 0
        if Hudvar == True:
            print("Az udvaron a túlnött fűtöl nehéz menni.")
        elif Heloszoba == True:
            print("Nincsen itt semmit nézni csak egypár régi eszköz és téli ruhák.")
        elif Hnappali == True:
            print("A régi kanapé televan kutya és macska szörrel.")
        elif Hgyerekszoba == True:
            print("A kis fiad éppen csöndben alszik.")
        elif Hkonyha == True:
            if Ikannal == True and Qegyelesaludjal1 == True and Qegyelesaludjal1F == False:
                print("Eszel egykis levest és mikor végeztel úgy döntöttél hogy lefekszel.")
                Qegyelesaludjal1F = True
            elif Ikannal == False and Qegyelesaludjal1 == True and Qegyelesaludjal1F == False:
                print("Körbe néztél a konyhába és találtál egy kis jegyzetet, hogy van leves a mikroban és kanalat talahatsz a szekrényben.")
                print("Elő vettél egy kanalat.")
                Ikannal = True
            else:
                print("Nincsen mit nézni, csak egypár koszos tányér amit még senkisem mosott el.")
        elif Hszuloszoba == True:
            print("Ahogyan ott van a különleges valakid, ugy döntesz, hogy befekszel mellé és alszol.")
            Qegyelesaludjal2F = True
            print("Köszönőm a játékot, még ha akarod körbe nézhetsz.")
    else:
        print("Nem megfelelő számot adott meg!")

