import random

print("Would you like a tutorials as the game goes on?")
print("(1) Yes, I want tutorials!")
print("(2) No, I DONT want tutorials!")
choice = int(input("Please input the number of the option you would like to choose: "))
if choice == 2:
    print("Tutorials have been turned off.")
    tutorial = False
elif choice == 1:
    print("Tutorials will be turned on.")
    tutorial = True
else:
    print("Invalid option. Tutorials have been turned on.")
    tutorial = True

Pmaxstat = int(input("(Debug) Please enter how many stat points you would like to have: "))
Pcurstat = Pmaxstat
print("There are 4 categorys: hp, attack, defense, magic.")
statdone = False
while statdone == False:
    Pstatpic1 = False
    while Pstatpic1 == False:
        print(Pcurstat,"unspent points")
        if tutorial == True:
            print("Hp is short for hit points, its a measure of how hurt you can get before you die.")
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
                Php_conversion = int(input("(Debug) How much hp should 1 skill point give you? "))
                if Php_conversion <= 0:
                    print("You can NOT put 0 or negativ values!")
                else:
                    Php_conversion_math = True
                    Pmaxhp = Pmaxhp * Php_conversion
                    Pcurhp = Pmaxhp

    Pstatpic2 = False
    while Pstatpic2 == False:
        print(Pcurstat,"unspent points")
        if tutorial == True:
            print("Attack is the measure of how much you will reduce the enemies hit points")
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
        if tutorial == True:
            print("Defense is how much the enemies attack is reduced by. A higher defense also gives you a better chance to parry an incoming attack.")
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
        if tutorial == True:
            print("Magic is a measure of how strong your spells will be.")
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
    Pstatcreator = int(input("Input the number of the choice you want: "))
    if Pstatcreator == 1:
        statdone = True
    else:
        Pbasedmg = 0
        Pdef = 0
        Pmagic = 0
        Pcurstat = Pmaxstat

print("Done creating a caracter!")

Emaxhp = int(input("(Debug) Enter the number of hit points your enemy should have: "))
Ecurhp = Pmaxhp
Edmg = int(input("(Debug) How many points should your enemy have in attack? "))
Edef = int(input("(Debug) How many points should your enemy have in defense? "))
Emagic = int(input("(Debug) How many points should your enemy have in magic? "))
print("(Debug) Your enemys stats are:",Edmg,"attack,",Edef,"defense,",Emagic,"magic and your enemy has",Emaxhp,"HP")
print("(Debug) You've made your enemy!")

Pflee = False
Eflee = False
startturn = False
Eambush = int(input("(Debug) Please input how strong shoulds the enemy ambush be (the enemys dmg*(this input)//1) (100 = enemy base damage, 0 = no bonus dmg(If the calculated dmg is less than 1  this will still deal 1 dmg)) "))
Pdmgbufftimer = 0
Pdmgbuff = int(input("(Debug) Please input how strong shouls your empowered attacks be (your dmg + (your dmg*(this input)//1) (100 = double dmg, 0 = no bonus dmg(If the multiplyed dmg is less than 1 this will still deal +1 dmg)) "))
Pdmgbuff = Pdmgbuff/100
Pcurdmg = Pbasedmg 
tutdeff = False
Tutbuff = False
Edefbuff = int(input("(Debug) How much should the enemies buff multiply their deffense? (Enemy def + (Enemy def*(this)//1) (100 = double def, 0 = no bonus dmg(If the multiplyed def is less than 1 this will still block +1 dmg)) "))
Edefbuff = Edefbuff/100
Edefbufftimer = 0
Buffbasedur = int(input("(Debug) How long should buffs last on their own?(turns) (affects both player and enemy) "))
Buffduronmagic = int(input("(Debug) How much longer should buffs be based on magic?(100= each point in magic makes it last a nother turn, 0= magic does not make spells last longer) (affects both player and enemy) "))
parry = int(input("(Debug) What should be the chance to get a parry? (100=guaranteed parry  0=no parry at all) "))
defensetoparry = int(input("(Debug) How much armore do you need for a 1 percent increase in chance to parry? (1 = 1 defense gives 1 precent higher chance to parry, 10 = 10 defense is needed for 1 percent increase) "))

parrydmg = int(input("(Debug) How much damage should the enemy deal to it self if you correcly parry? (200 = deals double the dmg it meant to deal to you, 100 = it will take as much dmg as it wanted to deal to you, 0= it wont deal damage to your oponent) "))
Phealstr = int(input("(Debug) How much health should each point of magic restore (100=1 magic point is 1 hp  0 = no amount of magic will make you heal) "))

Phealcooldown = int(input("(Debug) How much cooldown should there be after using a heal? (1 = 1 turn untill you can use spells again  10 = 10 turns befor you can use any spell again) "))
Pstrcooldown = int(input("(Debug) How much cooldown should there be after using a strenght buff? (1 = 1 turn untill you can use any spells again  10 = 10 turns befor you can use any spell again) "))
Pmagiccooldownreduction = int(input("(Debug) How much should points in magic reduce the cooldown of magic (100 = 1 point reduces cooldown by 1 turn  0 = points in magic will NOT reduce cooldown) "))
Pcurmagiccooldown = 0


while Pcurhp > 0 and Ecurhp > 0 and Pflee == False and Eflee == False:
    if startturn == False:
        print()
        startturn2 = random.randint(1,2)
        if startturn2 == 1:
            print("The enemy ambushed you! You take slight damage.")
            if (Edmg*Eambush)//100 < 1:
                Pcurhp -= 1
                startturn = True
            else:
                Pcurhp -= (Edmg*Eambush)//100
                startturn = True
        if startturn2 == 2:
            print("You ambush your enemy! Your next attack is empowered.")
            int(Pdmgbufftimer)
            Pdmgbufftimer += 2
            startturn = True
    Edice = random.randint(1,100)
    if Edice < 80:
        print("Your enemy intends to attack.")
        Eaction = 1
    elif Edice >= 80 and Edice < 100:
        print("Your enemy intends to buff it self.")
        Eaction = 2
        if tutorial == True and Tutbuff == False:
            print("A buff is a positiv affect that is usually a spell.")
            Tutbuff = True
    else:
        print("Your enemy intends to escape next turn.")
        Eaction = 3
    print()
    if Pdmgbufftimer > 0:
        Pcurdmg = Pbasedmg+(Pbasedmg*Pdmgbuff)//1
        Pdmgbufftimer -= 1
    else:
        Pcurdmg = Pbasedmg
    if Pdmgbufftimer > 0:
        print("You have",Pcurhp,"Hp,",Pcurdmg,"strenght,","You still have a damage buff for",Pdmgbufftimer,"more turns,",Pdef,"defense,",Pmagic,"magic")
    else:
        print("You have",Pcurhp,"Hp,",Pcurdmg,"strenght,",Pdef,"defense,",Pmagic,"magic")
    print()
    if Edefbufftimer > 0:
        Ecurdef = Edef+(Edef*Edefbuff)//1
        Edefbufftimer -= 1
    else:
        Ecurdef = Edef
    if Edefbufftimer > 0:
        print("Your enemy has",Ecurhp,"Hp,",Edmg,"strenght,",Ecurdef,"defense for",Edefbufftimer,"more turns,",Emagic,"magic")
    else:
        print("Your enemy has",Ecurhp,"Hp,",Edmg,"strenght,",Ecurdef,"defense,",Emagic,"magic")
    print()
    print("What would you like to do?")
    print("(1)  Attack")
    print("(2)  Block")
    print("(3)  Magic")
    print("(4)  Flee")
    
    choice = int(input("Please input the number before the choice you want "))
    print()
    if choice == 1:
        if Eaction == 1:
            if Edefbufftimer > 0:
                Edice = random.randint(0,Edef+Edefbuff)
                Edefbufftimer -= 1
            else:
                Edice = random.randint(0,Edef)
            
            if (Pcurdmg - ((Edice*0.5)//1)) < 1:
                Ecurhp -= 1
            else:
                Ecurhp -= (Pcurdmg - ((Edice*0.5)//1))
            
            Edice = random.randint(0,Edmg)
            Pdice = random.randint(0,Pdef)
            if Edice-((Pdice*0.5)//1) < 1:
                Pcurhp -= 1
            else:
                Pcurhp -= Edice-((Pdice*0.5)//1)
            if Pcurmagiccooldown > 0:
                Pcurmagiccooldown -=1

        elif Eaction == 2:
            if Edefbufftimer > 0:
                Edice = random.randint(0,Edef+Edefbuff)
                Edefbufftimer -= 1
            else:
                Edice = random.randint(0,Edef)
            
            if (Pcurdmg - ((Edice*0.5)//1)) < 1:
                Ecurhp -= 1
            else:
                Ecurhp -= (Pcurdmg - ((Edice*0.5)//1))

            Edefbufftimer += 1+Buffbasedur+((Buffduronmagic * Emagic)//100)
            if Pcurmagiccooldown > 0:
                Pcurmagiccooldown -=1
        
        else:
            if Edefbufftimer > 0:
                Edice = random.randint(0,Edef+Edefbuff)
                Edefbufftimer -= 1
            else:
                Edice = random.randint(0,Edef)
            
            if (Pcurdmg - ((Edice*0.5)//1)) < 1:
                Ecurhp -= 1
            else:
                Ecurhp -= (Pcurdmg - ((Edice*0.5)//1))

            Eflee = True
            if Pcurmagiccooldown > 0:
                Pcurmagiccooldown -=1

    elif choice == 2:
        if tutorial == True and tutdeff == False:
            print("Normaly if you dont block only half of your defense but if you block you use your full block and have a chance to parry the oponents attack.")
            tutdeff = True
        if Eaction == 1:
            Pdice = random.randint(1,100)
            Pextraparry = Pdef//defensetoparry
            if Pdice <= parry+Pextraparry:
                Edice = random.randint(0,Edmg)
                Ecurhp -= Edice*parrydmg//1
                print("You parryd their attack and dealt",parrydmg,"%" "of the damage they tried to deal to you.")
                if Pcurmagiccooldown > 0:
                    Pcurmagiccooldown -=1
            else:
                Edice = random.randint(0,Edmg)
                Pdice = random.randint(1,Pdef+1)
                if Edice- Pdice < 2:
                    print("You blocked their attack.")
                else:
                    Pcurhp -= Edice-Pdice
                if Pcurmagiccooldown > 0:
                    Pcurmagiccooldown -=1
        
        elif Eaction == 2:
            print("You blocked for no reason.")
            Edefbufftimer += Buffbasedur+((Buffduronmagic * Emagic)//100)
            if Pcurmagiccooldown > 0:
                Pcurmagiccooldown -=1
        else:
            print("You blocked for no reason.")
            if Pcurmagiccooldown > 0:
                Pcurmagiccooldown -=1
            Eflee = True

    elif choice == 3:
        if Pcurmagiccooldown > 0:
            print("Your magic is on cooldown for", Pcurmagiccooldown,"turns")
        else:
            print("You have 2 spells:")
            print("(1) Heal")
            print("(2) Damage buff")
            print("(3) Back")
            if tutorial == True and Tutbuff == False:
                print("A buff is a positiv affect that is usually a spell.")
                Tutbuff = True
            choice = int(input("Please input the number before the choice you want "))
            print()
            if choice == 1:
                Pdice = random.randint(0,Pmagic)
                Pcurhp += Pdice
                if Pcurhp > Pmaxhp:
                    Pcurhp = Pmaxhp
                Pcurmagiccooldown = (Phealcooldown-((Pmagic*Pmagiccooldownreduction)//100))
                if Pcurmagiccooldown < 0:
                    Pcurmagiccooldown = 0
            else:
                Pdmgbufftimer += 1+(Buffbasedur+(Pmagic*Buffduronmagic)//100)
                Pcurmagiccooldown = (Pstrcooldown-((Pmagic*Pmagiccooldownreduction)//100))
                if Pcurmagiccooldown < 0:
                    Pcurmagiccooldown = 0
            
            if Eaction == 1:
                Edice = random.randint(0,Edmg)
                Pdice = random.randint(0,Pdef)
                if Edice-((Pdice*0.5)//1) < 1:
                    Pcurhp -= 1
                else:
                    Pcurhp -= Edice-((Pdice*0.5)//1)
    else:
        Pflee = True

print()
if Ecurhp < 1 and Pcurhp <1:
    print("You wore each other out and both died.")
elif Ecurhp > 1 and Pcurhp <1 and Pflee==False:
    print("You were killed in combat.")
elif Ecurhp > 1 and Pcurhp <1 and Pflee==True:
    print("You were killed while trying to escape.")
elif Ecurhp < 1 and Pcurhp >1 and Eflee==False:
    print("You killed it.")
elif Ecurhp < 1 and Pcurhp >1 and Eflee==True:
    print("You killed it while it was trying to escape.")
else:
    print("You both ran away.")
                