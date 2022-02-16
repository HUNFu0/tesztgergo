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
        else:
            Pcurstat -= Pdmg
            Pstatpic1 = True

    Pstatpic2 = False
    while Pstatpic2 == False:
        print(Pcurstat,"unspent")
        Pdef = int(input("How many points would you like to put into defense? "))
        if Pdef > Pcurstat:
            print("You dont have that many skill points!")
        else:
            Pcurstat -= Pdef
            Pstatpic2 = True 

    Pstatpic3 = False
    while Pstatpic3 == False:
        print(Pcurstat,"unspent")
        Pmagic = int(input("How many points would you like to put into magic? "))
        if Pmagic > Pcurstat:
            print("You dont have that many skill points!")
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
