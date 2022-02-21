import random

Tutorial = 2
while Tutorial < 0 and Tutorial > 1:
    print("Would you like a tutorial on the games mechanics?")
    print("(0) No, i do NOT want a tutorial.")
    print("(1) Yes, i do want a tutorial.")
    Tutorial = int(input("Type the number of the option you would like to choose. "))
    if Tutorial < 0 or Tutorial > 1:
        print("Invalid option was selected.")

Pmaxstat = int(input("Please enter how many stat points you would like to have: "))
Pcurstat = Pmaxstat
print("There are 4 categorys: hp, attack, defense, magic.")
statdone = False
while statdone == False:
    Pstatpic1 = False
    while Pstatpic1 == False:
        print(Pcurstat,"unspent points")
        Pmaxhp = int(input("How many points would you like to put into your hp?: "))
        if Pmaxhp > Pcurstat:
            print("You dont have that many skill points!")
        elif Pmaxhp <= 0:
            print("You cant input negativ numbers or 0!")
        else:
            Pcurstat -= Pmaxhp
            Pstatpic1 = True
            Php_conversion_math = False
            while Php_conversion_math == False:
                Php_conversion = int(input("How much hp should 1 skill point give you? "))
                if Php_conversion <= 0:
                    print("You can NOT put 0 or negativ values!")
                else:
                    Php_conversion_math = True
                    Pmaxhp = Pmaxhp * Php_conversion
                    Pcurhp = Pmaxhp

    Pstatpic2 = False
    while Pstatpic2 == False:
        print(Pcurstat,"unspent points")
        Pbasedmg = int(input("How many points would you like to put into attack? "))
        if Pbasedmg > Pcurstat:
            print("You dont have that many skill points!")
        elif Pbasedmg < 0:
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pbasedmg
            Pstatpic2 = True

    Pstatpic3 = False
    while Pstatpic3 == False:
        print(Pcurstat,"unspent")
        Pdef = int(input("How many points would you like to put into defense? "))
        if Pdef > Pcurstat:
            print("You dont have that many skill points!")
        elif Pdef < 0:
            
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pdef
            Pstatpic3 = True 

    Pstatpic4 = False
    while Pstatpic4 == False:
        print(Pcurstat,"unspent")
        Pmagic = int(input("How many points would you like to put into magic? "))
        if Pmagic > Pcurstat:
            print("You dont have that many skill points!")
        elif Pmagic < 0:
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pmagic
            Pstatpic4 = True
    print("Your stats are:",Pbasedmg,"attack,",Pdef,"defense,",Pmagic,"magic and you have",Pmaxhp,"HP")
    if Pcurstat != 0:
        print("You still have",Pcurstat,"unspent skill points!")
    print("Are you happy with your stats?")
    print("(1) Yes")
    print("(2) No")
    Pstatcreator = int(input("Inpuit the number of the choice you want: "))
    if Pstatcreator == 1:
        statdone = True
    else:
        Pbasedmg = 0
        Pdef = 0
        Pmagic = 0
        Pcurstat = Pmaxstat

print("Done creating a caracter!")

Emaxhp = int(input("Enter the number of hit points your enemy should have: "))
Ecurhp = Pmaxhp
Edmg = int(input("How many points should your enemy have in attack? "))
Edef = int(input("How many points should your enemy have in defense? "))
Emagic = int(input("How many points should your enemy have in magic? "))
print("Your enemys stats are:",Edmg,"attack,",Edef,"defense,",Emagic,"magic and your enemy has",Emaxhp,"HP")
print("You've made your enemy!")

Pflee = False
Eflee = False
startturn = False
Pempowered = 0
Eempowered = 0
Eambush = int(input("Please input how strong shoulds the enemy ambush be (the enemys dmg*(this input)//1) (100 = enemy damage, 0 = no bonus dmg(If the calculated dmg is less than 1  this will still deal 1 dmg)) "))
Pempow_multiply = int(input("Please input how strong shouls your empowered attacks be (your dmg + (your dmg*(this input)//1)) (100 = double dmg, 0 = no bonus dmg(If the multiplyed dmg is less than 1 this will still deal +1 dmg)) "))


while Pcurhp > 0 and Ecurhp > 0 and Pflee == False and Eflee == False:
    if startturn == False:
        print()
        startturn2 = random.randint(1,2)
        if startturn2 == 1:
            print("The enemy ambushed you! You take slight damage.")
            if (Edmg*0.5)//1 < 1:
                Pcurhp -= 1
                startturn = True
            else:
                Pcurhp -= (Edmg*Eambush)//1
                startturn = True
        if startturn2 == 2:
            print("You ambush your enemy! Your next attack is empowered.")
            Pempowered += 1
            startturn = True
    print()
    print("What would you like to do?")
    print("(1)  Attack")
    print("(2)  Block")