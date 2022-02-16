import random


Pmaxhp = int(input("Enter the number of hit points you would like to have: "))
Pcurhp = Pmaxhp
Pmaxstat = int(input("Please enter how many stat points you would like to have: "))
Pcurstat = Pmaxstat
print("There are 3 categorys: attack, defense, magic.")
statdone = False
while statdone == False:
    Pstatpic1 = False
    while Pstatpic1 == False:
        print(Pcurstat,"unspent points")
        Pdmg = int(input("How many points would you like to put into attack? "))
        if Pdmg > Pcurstat:
            print("You dont have that many skill points!")
        elif Pdmg < 0:
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pdmg
            Pstatpic1 = True

    Pstatpic2 = False
    while Pstatpic2 == False:
        print(Pcurstat,"unspent")
        Pdef = int(input("How many points would you like to put into defense? "))
        if Pdef > Pcurstat:
            print("You dont have that many skill points!")
        elif Pdef < 0:
            
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pdef
            Pstatpic2 = True 

    Pstatpic3 = False
    while Pstatpic3 == False:
        print(Pcurstat,"unspent")
        Pmagic = int(input("How many points would you like to put into magic? "))
        if Pmagic > Pcurstat:
            print("You dont have that many skill points!")
        elif Pmagic < 0:
            print("You cant input negativ numbers!")
        else:
            Pcurstat -= Pmagic
            Pstatpic3 = True
    print("Your stats are:",Pdmg,"attack,",Pdef,"defense,",Pmagic,"magic and you have",Pmaxhp,"HP")
    if Pcurstat != 0:
        print("You still have",Pcurstat,"unspent skill points!")
    print("Are you happy with your stats?")
    print("(1) Yes")
    print("(2) No")
    Pstatcreator = int(input("Inpuit the number of the choice you want: "))
    if Pstatcreator == 1:
        statdone = True
    else:
        Pdmg = 0
        Pdef = 0
        Pmagic = 0
        Pcurstat = Pmaxstat

print("Done creating a caracter!")

Emaxhp = int(input("Enter the number of hit points your enemy should have: "))
Ecurhp = Pmaxhp
Emaxstat = int(input("Please enter how many stat points your enemy should have: "))
Ecurstat = Emaxstat
print("There are 3 categorys: attack, defense, magic.")
Estatdone = False
while Estatdone == False:
    Estatpic1 = False
    while Estatpic1 == False:
        print(Ecurstat,"unspent points")
        Edmg = int(input("How many points should your enemy have in attack? "))
        if Edmg > Ecurstat:
            print("There arent that many skill points!")
        elif Edmg < 0:
            print("You cant input negativ numbers!")
        else:
            Ecurstat -= Edmg
            Estatpic1 = True

    Estatpic2 = False
    while Estatpic2 == False:
        print(Ecurstat,"unspent")
        Edef = int(input("How many points should your enemy have in defense? "))
        if Edef > Ecurstat:
            print("There arent that many skill points!")
        elif Edef < 0:
            print("You cant input negativ numbers!")
        else:
            Ecurstat -= Edef
            Estatpic2 = True 

    Estatpic3 = False
    while Estatpic3 == False:
        print(Ecurstat,"unspent")
        Emagic = int(input("How many points should your enemy have in magic? "))
        if Emagic > Ecurstat:
            print("There arent that many skill points!")
        elif Emagic < 0:
            print("You cant input negativ numbers!")
        else:
            Ecurstat -= Emagic
            Estatpic3 = True
    print("Your enemys stats are:",Edmg,"attack,",Edef,"defense,",Emagic,"magic and your enemy has",Emaxhp,"HP")
    if Ecurstat != 0:
        print("You still have",Ecurstat,"unspent skill points!")
    print("Are you happy with your stats?")
    print("(1) Yes")
    print("(2) No")
    Estatcreator = int(input("Inpuit the number of the choice you want: "))
    if Estatcreator == 1:
        Estatdone = True
    else:
        Edmg = 0
        Edef = 0
        Emagic = 0
        Ecurstat = Emaxstat

print("You've made your enemy!")

print(random.randint(0,Pdmg))
