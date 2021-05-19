import time
import random









































player_stats = {"Name" : "", "LVL" : 1, "MLVL" : 5, "ATK" : 200, "MDEF" : 100, "DEF" : 0, "MHP" : 1000, "HP" : 1000, "GOLD" : 1, "EN" : 1, "orbA" : 0, "orbD" : 0, "orbH" : 0}
enemy_stats = {"Name" : "", "ATK" : 200, "MHP" : 1000, "HP" : 1000}
battle = {"action" : 0, "actor" : 0, "statusP" : 0, "statusE" : 0}
upgrade = {"priceG" : 5, "priceE" : 3}
items = [1,1,1]
message = 0


def battle_startend():
    global player_stats
    global enemy_stats
    global battle
    global startend
    print("\n" * 200)
    enemy_stats["HP"] = enemy_stats["MHP"]

    if startend == "Start":
        print("==========\n" + str(enemy_stats["Name"]) + " Approaches!\n==========")
        time.sleep(2)
        battle = {"action" : 0, "actor" : 0, "statusP" : 0, "statusE" : 0}
        battle_player()
    elif startend == "Win":
        print("==========\nVICTORY!\n==========\n\nGot:")

        
        goldearnt = random.randint(9,15)
        player_stats["GOLD"] += goldearnt
        print(str(goldearnt) + " GOLD!")
        
        rng = random.randint(1,3)
        if rng != 3:
            enearnt = random.randint(1,2)
            player_stats["EN"] += enearnt
            print(str(enearnt) +" EP!")

        rng = random.randint(1,4)
        if rng == 1:
            rng = random.randint(1,3)
            player_stats["orbA"] += rng
            print(str(rng) + " Crimson Orb!")
        elif rng == 2:
            rng = random.randint(2,4)
            player_stats["orbD"] += rng
            print(str(rng) + " Protected Orb!")
        elif rng == 3:
            rng = random.randint(3,4)
            player_stats["orbH"] += rng
            print(str(rng) + " Shiny Orb!")
            
        
        input("\n >")
        enemy_stats["ATK"] += int(enemy_stats["ATK"] * 0.2)
        enemy_stats["MHP"] += int(enemy_stats["MHP"] * 0.2)
        welcome()
    elif startend == "Lose":
        print("==========\nGAME OVER!\n==========\n")
        print("Press ENTER to go to MAIN MENU")
        input(" >")
        player_stats["GOLD"] = 0
        player_stats["EN"] += 1
        player_stats["HP"] = player_stats["MHP"]
        battle = {"action" : 0, "actor" : 0, "statusP" : 0, "statusE" : 0}
        upgrade["priceG"] -= 2
        message = 0
        welcome()
    else:
        print("Error")
        print(str(startend))
        input()
        startend = "Start"
        welcome()





def battle_player():
    global player_stats
    global enemy_stats
    global battle
    global startend
    print("\n" * 200)
    battle["actor"] = player_stats["Name"]
    player_stats["DEF"] = 0
    
    percentP = int((player_stats["HP"]/player_stats["MHP"]) * 100)
    if percentP == 0:
        percentP = 1



    print("==========\n" + str(player_stats["Name"]) + " [" + str(percentP) + "% HP]\n==========\n")
    print("1. Fight")
    print("2. Defend")
    print("\n3. Action")

    a=input("\n >")

    if a == "1":
        battle["action"] = "Fight"
    elif a == "2":
        battle["action"] = "Defend"
    elif a == "3":
        while True:
            print("\n" * 200)
            print("==========\nACTION\n==========\n")
            print("1. Observe")
            print("2. Stand menacingly (Uses turn)")
            print("\n3. Back")
            a=input("\n >")

            if a == "1":
                print("\n" * 200)
                print("==========")
                print(str(player_stats["Name"]) + " [" + str(player_stats["HP"]) + "/" + str(player_stats["MHP"]) + "HP]")
                print("ATK: " + str(player_stats["ATK"]) + "   DEF: " + str(player_stats["MDEF"]))
                print("==========")
                print(str(enemy_stats["Name"]) + " [" + str(enemy_stats["HP"]) + "/" + str(enemy_stats["MHP"]) + "HP]")
                print("ATK: " + str(enemy_stats["ATK"]))
                print("==========")
                
                input("\n >")
                decision = 1
                break
            elif a == "2":
                battle["action"] = "Stand Menacingly"
                decision = 2
                break
            elif a == "3":
                decision = 3
                break

        if decision == 1:
            battle_player()
        elif decision == 3:
            battle_player()

    else:
        battle_player()

    if battle["statusP"] == "Dizzy":
        battle["action"] = "Stand like an Idiot"
        battle["statusP"] = 0

    battle_neutral()
        

def battle_neutral():
    global player_stats
    global enemy_stats
    global battle
    global startend
    print("\n" * 200)
    print("==========")
    print(str(battle["actor"]) + "\nused\n'" + str(battle["action"]) + "'!")
    print("==========\n")

    damage = 0
    crit = 0

    if battle["actor"] == player_stats["Name"]:
        if battle["action"] == "Fight":
            damage = player_stats["ATK"]
            rng = random.randint( int(-(player_stats["ATK"] * 0.1))  , int(player_stats["ATK"] * 0.1))
            damage += rng

            crit = random.randint(1,10)

            if crit == 1:
                damage += damage
                crit = "(CRITICAL!)"
            else:
                crit = ""

            enemy_stats["HP"] -= damage

            if enemy_stats["HP"] <= 0:
                enemy_stats["HP"] = 0
        elif battle["action"] == "Defend":
            player_stats["DEF"] = player_stats["MDEF"]
            

    elif battle["actor"] == enemy_stats["Name"]:
        if battle["action"] == "Fight":
            damage = enemy_stats["ATK"]
            rng = random.randint( int(-(enemy_stats["ATK"] * 0.1))  , int(enemy_stats["ATK"] * 0.1))
            damage += rng

            crit = random.randint(1,10)

            if crit == 1:
                damage += damage
                crit = "(CRITICAL!)"
            else:
                crit = ""

            damage -= player_stats["DEF"]

            
            if damage < 0:
                enemy_stats["HP"] += damage
            else:
                player_stats["HP"] -= damage

            if player_stats["HP"] <= 0:
                player_stats["HP"] = 0

            if player_stats["DEF"] >= player_stats["MDEF"]:
                rng = random.randint(1,3)
                if rng != 1:
                    battle["statusE"] = "Dizzy"
                    print(str(enemy_stats["Name"]) + " became Dizzy!")
                else:
                    battle["statusP"] = "Dizzy"
                    print("Broken defence!")
                    print(str(player_stats["Name"]) + " became Dizzy!")

    else:
        print("Error")
        print(str(battle))

    if battle["action"] == "Fight":
        if damage < 0:
            print(str(damage) + " damage reflected! " + str(crit))
        else:
            print(str(damage) + " damage dealt! " + str(crit))
            

    time.sleep(2)
    input("\nContinue>")


    if player_stats["HP"] <= 0:
        startend = "Lose"
        battle_startend()
    elif enemy_stats["HP"] <= 0:
        startend = "Win"
        battle_startend()
    else:
        if battle["actor"] == player_stats["Name"]:
            battle_enemy()
        elif battle["actor"] == enemy_stats["Name"]:
            battle_player()


def battle_enemy():
    global player_stats
    global enemy_stats
    global battle
    global startend
    battle["actor"] = enemy_stats["Name"]
    
    percentE = int((enemy_stats["HP"]/enemy_stats["MHP"]) * 100)
    if percentE == 0:
        percentE = 1
    
    print("\n" * 200)
    print("==========\n" + str(enemy_stats["Name"]) + "'s [" + str(percentE) + "% HP] TURN!\n==========")

    
    if battle["statusE"] == "Dizzy":
        battle["action"] = "Stand like an idiot"
        battle["statusE" ] = 0
    else:
        battle["action"] = "Fight"
        
    
    time.sleep(3)
    battle_neutral()
        
        



def welcome():
    global startend
    global message
    print("\n" * 200)
    print("==========\nWelcome to Swordfight V2\n(Remember the one from 2019! It's back!)\n==========\n")
    print("1. Fight")
    print("2. Upgrade")
    print("3. Orb Exchange")
    print("\n4. Check stats")
    print("5. Heal (1 EP)")
    print("\n6. Exit")

    a=input("\n >")

    if a == "1":
        startend = "Start"
        battle_startend()
    elif a == "2":
        message = "Get stronger!"
        shop()
    elif a == "3":
        message = "Trade Items!"
        shop2()
    elif a == "4":
        stats()
    elif a == "5":
        if player_stats["EN"] >= 1:
            if player_stats["HP"] < player_stats["MHP"]:
                player_stats["EN"] -= 1
                player_stats["HP"] = player_stats["MHP"]
                print("\n" * 200)
                print("==========\nHealed!\n==========\n")
                input("Back>")
                player_stats["HP"] = player_stats["MHP"]
                welcome()
            else:
                print("\n" * 200)
                print("==========\nAlready max HP!\n==========\n")
                input("Back>")
                welcome()
        else:
            print("\n" * 200)
            print("==========\nNot enough Energy Points!\n==========\n")
            input("Back>")
            welcome()
            
    elif a == "6":
        exit()
    else:
        welcome()


def shop():
    global message
    global upgrade
    global player_stats
    
    print("\n" * 200)
    print("==========\nUPGRADE\n" + str(message) +"\n==========\nGOLD: " + str(player_stats["GOLD"]) + "\nEnergy Points: " + str(player_stats["EN"]) + "\n==========\n")
    print("1. Increase LVL     (" + str(upgrade["priceG"]) + " GOLD)")
    print("2. Increase Max LVL (3 Energy Points)")
    print("\n3. Exit")
    
    a=input("\n >")

    if a == "1":
        if player_stats["LVL"] < player_stats["MLVL"]:
            if player_stats["GOLD"] >= upgrade["priceG"]:
                player_stats["GOLD"] -= upgrade["priceG"]
                upgrade["priceG"] += 1
                
                player_stats["LVL"] += 1
                
                rng = random.randint(1,3)
                if rng == 1:
                    player_stats["ATK"] += int(player_stats["ATK"] * 0.3)
                    message = "Level up! ATK increased!"
                elif rng == 2:
                    player_stats["MDEF"] += int(player_stats["MDEF"] * 0.3)
                    message = "Level up! DEF increased!"
                elif rng == 3:
                    player_stats["MHP"] += int(player_stats["MHP"] * 0.3)
                    message = "Level up! HP increased!"
                    
                player_stats["HP"] = player_stats["MHP"]

                shop()
            else:
                message = "Not enough GOLD"
                shop()
        else:
            message = "Max LVL reached"
            shop()
            
    elif a == "2":
        if player_stats["LVL"] >= player_stats["MLVL"]:
            if player_stats["EN"] >= upgrade["priceE"]:
                player_stats["EN"] -= upgrade["priceE"]
                player_stats["MLVL"] += 5
                
                player_stats["ATK"] += int(player_stats["ATK"] * 0.4)
                player_stats["MDEF"] += int(player_stats["MDEF"] * 0.4)
                player_stats["MHP"] += int(player_stats["MHP"] * 0.4)
                player_stats["HP"] = player_stats["MHP"]
                
                message = ("Max level increased to " + str(player_stats["MLVL"]) + "!\nAll stats increased!")

                shop()
            else:
                message = "Not enough Energy Points"
                shop()
        else:
            message = "You can't ascend yet!"
            shop()
            
    elif a == "3":
        welcome()
    else:
        message = "Select a valid option"
        shop()



def shop2():
    global message
    global player_stats

    print("\n" * 200)
    print("==========\nORB EXCHANGE\n" + str(message) + "\n==========\n\n")

    if player_stats["orbA"] > 0:
        print("1. Trade Crimson Orb " + str(player_stats["orbA"]))
    if player_stats["orbD"] > 0:
        print("2. Trade Protected Orb " + str(player_stats["orbD"]))
    if player_stats["orbH"] > 0:
        print("3. Use Shiny Orb " + str(player_stats["orbH"]))

    print("\n4.Convert Orbs")
    print("5. Back")
    a = input("\n >")

    if player_stats["orbA"] > 0 and a == "1":
        player_stats["orbA"] -= 1
        player_stats["ATK"] += int(player_stats["ATK"] * 0.1)
        message = "ATK Increased"
        shop2()
    elif player_stats["orbD"] > 0 and a == "2":
        player_stats["orbD"] -= 1
        player_stats["MDEF"] += int(player_stats["MDEF"] * 0.1)
        message = "DEF Increased"
        shop2()
    elif player_stats["orbH"] > 0 and a == "3":
        player_stats["orbH"] -= 1
        player_stats["MHP"] += int(player_stats["MHP"] * 0.1)
        player_stats["HP"] = player_stats["MHP"]
        message = "HP Increased"
        shop2()
    elif a == "4":

        convert = {"convertU" : 0, "convertT" : 0}
        decision = 0
        message = "Convert ORBs"
        
        while True:
            print("\n" * 200)
            print("==========\nCONVERSION\n" + str(message) +"\n==========\n")
            if player_stats["orbA"] > 0:
                print("1. Convert Crimson Orb " + str(player_stats["orbA"]))
            if player_stats["orbD"] > 0:
                print("2. Convert Protected Orb " + str(player_stats["orbD"]))
            if player_stats["orbH"] > 0:
                print("3. Convert Shiny Orb " + str(player_stats["orbH"]))

            print("\n4. Back")
            a=input("\n >")

            if a == "1" and player_stats["orbA"] > 0:
                convert["convertU"] = "orbA"
                break
            elif a == "2" and player_stats["orbD"] > 0:
                convert["convertU"] = "orbD"
                break
            elif a == "3" and player_stats["orbH"] > 0:
                convert["convertU"] = "orbH"
                break
            elif a == "4":
                decision = "Back"
                break
            else:
                message = "Cannot Convert"

        message = "Convert to?"
        
        if decision == "Back":
            shop2()
        else:
            while True:
                print("\n" * 200)
                print("==========\nCONVERSION\n" + str(message) + "\nEnergy Points: " + str(player_stats["EN"]) +"\n==========\n")
                print("1. Convert to Crimson Orb")
                print("2. Convert to Protector Orb")
                print("3. Convert to Shiny Orb")

                print("\n4. Back")
                a=input("\n >")

                if a == "1" and player_stats["EN"] > 0:
                    convert["convertT"] = "orbA"
                    player_stats["EN"] -= 1
                    break
                elif a == "2" and player_stats["EN"] > 0:
                    convert["convertT"] = "orbD"
                    player_stats["EN"] -= 1
                    break
                elif a == "3" and player_stats["EN"] > 0:
                    convert["convertT"] = "orbH"
                    player_stats["EN"] -= 1
                    break
                elif a == "4":
                    decision = "Back"
                    break
                else:
                    message = "Cannot Convert"

            if decision == "Back":
                shop2()
            else:
                player_stats[str(convert["convertT"])] += 1
                player_stats[str(convert["convertU"])] -= 1
                message = "Successfully Converted!"

            shop2()

        
                

                
            
    elif a == "5":
        welcome()
    else:
        message = "Cannot exchange"
        shop2()





def item3():
    print("\n" * 200)
    print("==========\nITEM SHOP\nGOLD: " + str(player_stats["GOLD"]) + "\n==========\n")
    print("1. Buy Bandage (2 GOLD)")
    print("2. Medicine    (5 GOLD)")
    print("3. Healing Orb (10 GOLD)")
    a=input("\n >")

    if a == "1" and player_stats["GOLD"] >= 2:
        #nice
    


def stats():
    global player_stats
    print("\n" * 200)
    print("==========\n" + str(player_stats["Name"]) + "\nLvl " + str(player_stats["LVL"]) +"\n[" + str(player_stats["HP"]) + "/" + str(player_stats["MHP"]) + "HP]\n==========\n")
    print("ATK: " + str(player_stats["ATK"]) + "   DEF: " + str(player_stats["MDEF"]))
    print("GOLD: " + str(player_stats["GOLD"]))
    print("Energy Points: " + str(player_stats["EN"]))

    input("\nBack>")
    welcome()







print("\n" * 200)
print("What's your name?")
player_stats["Name"] = input(" >")

print("\n" * 200)
print("Who's your worst enemy?")
enemy_stats["Name"] = input(" >")

if player_stats["Name"] == enemy_stats["Name"]:
    enemy_stats["Name"] = str(str(random.randint(100,999)) + " Enemy")
    
welcome()












