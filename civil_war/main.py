#import needed modules
import sys
import time
import random

#import needed functions
from civil_war_functions import*

#introduction text
print_slow("                       Welcome to the Civil War Simulation!\n")
line = "______________________________________________________________________________"
print(line)
print()

#user input for name
name = get_user_name()

#sim introduction
sim_introduction(name)
print(line)

#user input for side
side = get_user_side().title()
greet_user_side(name,side)

#list of battles
list_of_battles = ["Bull Run", "Peninsula Campaign", "Antietam", "Fredericksburg", "Chancellorsville", "Gettysburg", "The Wilderness", "Siege of Petersburg", "Sailor's Creek"]
print_slow("Here is a list of battles you can choose from (in chronological order): \n")
for battles in list_of_battles:
    print(battles)

#frequently used statements
sim_end_statement = f"Thanks for playing the Civil War Simulation, {name}!"

#establish casualty rate
casualty_rate = 0

#tracks whether the player is still alive (set to False when killed in action)
alive = True

#establish while loop
battles_fought = 0
if side == "Confederate":
    battle_count = 8
else:
    battle_count = 6
while battles_fought < battle_count:
    print(line)

#establish while loop for user input for battles
    battle = battle_selection()
    battles_fought += 1

#bull run
    if battle == "bull run" or battle == "battle of bull run":
        battle = "Battle of Bull Run"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 15
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"{name}, you and your {side} comrades are fighting in the Battle of Bull Run,\nthe first major battle of the Civil War. ")
            print_slow(f"\nYou and the men of your regiment are excited by the battle - \neveryone expects the war to be over by Christmas, \nand no one wants to miss out on the action.")
            print_slow("\nDuring the battle, you and about 18,000 Union\nsoldiers were engaged in combat. \n1,982 of your comrades were killed, wounded or captured.\nThis is a 15% casualty rate.\n")
            print_slow(f"The battle was a {side} defeat. This war might last longer than we expected.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2} or a {sim_roll3} you're either captured or wounded.  \nIf you entered a {sim_roll4} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll4:
                print_slow(f"\nUnfortunately, {name}, you died today fighting the first battle \nof the Civil War.\n")
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_one(name,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 11
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"{name}, you and your {side} comrades are fighting in the \nBattle of Bull Run, the first major battle of the Civil War. ")
            print_slow("You and the soldiers of your regiment are excited to fight - \nthis is your chance to show those Yankees that one southerner can whip 10 of them!")
            print_slow("\nAbout 18,000 Confederate soldiers fought in the battle; \n2,708 of them were killed, wounded or captured.\nThis is an 11% casualty rate.")
            print_slow(f"\nFortunately for you, this battle was a {side} victory.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll} or a {sim_roll2} you're captured or wounded.  \nIf you entered a {sim_roll3} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll3:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_one(name,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#peninsula campaign
    if battle == "peninsula campaign" or battle == "peninsula":
        battle = "Peninsula Campaign"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 29
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"It is the spring of 1862, and the Army of the Potomac, led by General McClellan,\nis attempting to capture the Confederate capital of Richmond.\n")
            print_slow("From March until July, \n102,236 Union soldiers fought in a series of battles outside Richmond. \n29,298 of them were killed, wounded or captured.\nThis is a 29% casualty rate.\n")
            print_slow(f"This battle was a {side} defeat, and the Army of the Potomac retreated \nback to Washington having failed to capture Richmond.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, {sim_roll4} or a {sim_roll5} you're either captured or wounded.  \nIf you entered a {sim_roll6} or a {sim_roll7}, you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4 or user_number == sim_roll5:
                captured_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll6 or user_number == sim_roll7:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_two(battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 24
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"{name}, you and your regiment are defending Richmond in what \ncame to be known as the {battle}.")
            print_slow(f"\nDuring the battle, the commander of the Army of Northern Virginia,\nGeneral Joe Johnston, was wounded in action. ")
            print_slow(f"\nConfederate President Jefferson Davis replaced Johnston\nwith General Robert E. Lee, who successfully defended the capital.")
            print_slow("\n94,813 Confederate soldiers fought in the campaign,\nwhich lasted from March until July of 1862.\n23,119 of them were killed, wounded or captured.\nThis is a 24% casualty rate.")
            print_slow(f"\nThis battle was a {side} victory.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, or a {sim_roll4}, you're captured or wounded.  \nIf you entered a {sim_roll5} or {sim_roll6} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4:
                print_slow(f"\nI can see that you've been wounded, {name}. Quickly, make your way to the \nregimental surgeon.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll5 or user_number == sim_roll6:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_two(battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#antietam
    if battle == "antietam" or battle == "battle of antietam":
        battle = "Battle of Antietam"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 23
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"You and your {side} soldiers are fighting the worst one day battle\nin American history - the Battle of Antietam.\n")
            print_slow("Under the command of General McClellan,\n53,632 Union soldiers were engaged in combat for 12 hours. \n12,410 of them were killed, wounded or captured.\nThis is a 23% casualty rate.\n")
            print_slow(f"This battle was a {side} victory, and Lincoln used it as an opportunity\nto announce the Emancipation Proclamation.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2} or a {sim_roll3} you're either captured or wounded.\nIf you entered a {sim_roll4} or a {sim_roll5}, you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll4 or user_number == sim_roll5:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_three(side,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 34
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"You and your {side} soldiers are fighting the worst one day battle in\nAmerican history - the Battle of Antietam.")
            print_slow("General Lee, hoping to win a decisive victory, invades Maryland.  \nThe two sides meet near a small creek called Antietam.")
            print_slow("\n30,646 Confederate soldiers fought in this 12 hour battle under the command of \nGeneral Robert E. Lee; 10,337 of them were killed, wounded or captured.\nThis is a 34% casualty rate.")
            print_slow(f"\nThis battle was a {side} defeat.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, or a {sim_roll4}, you're captured or wounded.  \nIf you entered a {sim_roll5} or {sim_roll6} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll5 or user_number == sim_roll6:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_three(side,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#fredericksburg
    if battle == "fredericksburg" or battle == "battle of fredericksburg":
        battle = "Battle of Fredericksburg"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 11
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow("It is December of 1862.  Instead of preparing to celebrate Christmas with your\nfamily, you are fighting in the Battle of Fredericksburg.\n")
            print_slow("Once again, the Army of the Potomac is trying to capture \nRichmond under the command of yet another general.")
            print_slow(f"\nDuring the {battle}, about 114,000 Union soldiers \nwere engaged in combat under General Ambrose Burnside. \n12,653 of them were killed, wounded or captured.\nThis is an 11% casualty rate.\n")
            print_slow("You and your regiment were ordered to charge up a hill against \nConfederates positioned behind a low stone wall.  It was a massacre.")
            print_slow(f"\nThis battle was a crushing {side} defeat.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll} or a {sim_roll2} you're either captured or wounded.  \nIf you entered a {sim_roll3} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll3:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow("\nThat night as you warm yourself by the fire, \nyou can hear the cries and moans of the wounded still lying on the battlefield.")
                print_slow(f"\nYou're relieved to not be among them, \nand you try to comfort yourself with the thought\nthat maybe you'll make it home in time for Christmas after all.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 7
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow("It is December of 1862.  Instead of preparing to celebrate Christmas with your\nfamily, you are fighting in the Battle of Fredericksburg.")
            print_slow("\nThe battle is yet another attempt by the Union to capture Richmond.\nThey didn't get very far before you and your comrades stopped them.")
            print_slow("\nLed by General Lee, about 72,500 Confederate soldiers fought in the battle; \n5,377 of them were killed, wounded or captured.\nThis is a 7% casualty rate.")
            print_slow(f"\nThis battle was a major {side} victory.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll} you're captured or wounded.  \nIf you entered a {sim_roll2} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll:
                captured_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll2:
                print_slow(f"\nUnfortunately, {name}, you'll never celebrate Christmas with your family again.\n")
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow("\nAs the battle draws to a close, \nboth sides witness the most dazzling display of the \nnorthern lights perhaps ever seen in Virginia.")
                print_slow(f"\nAs you look up to the sky, you think to yourself that \nmaybe you'll make it home for Christmas after all.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#chancellorsville
    if battle == "chancellorsville" or battle == "battle of chancellorsville":
        battle = "Battle of Chancellorsville"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 13
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"{name}, you and the Army of the Potomac are invading Virginia \nunder the command of General Joe Hooker. ")
            print_slow("It is May of 1863.  \nUnion and Confederate forces are converging on a \nsmall town called Chancellorsville. ")
            print_slow("During the battle, \nabout 133,868 Union soldiers were engaged in combat. \n17,287 of them were killed, wounded or captured.\nThis is a 13% casualty rate.\n")
            print_slow(f"The battle was yet another crushing {side} defeat.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll} or a {sim_roll2} you're either captured or wounded.  \nIf you entered a {sim_roll3} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll3:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\nYou survived the battle, \nbut the war is not going well for the {side}.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 21
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow("The Army of the Potomac has invaded Virginia yet again and General Lee is \nmoving the Army of Northern Virginia to stop them. ")
            print_slow("It is May of 1863.  \nUnion and Confederate forces are converging on a small town called \nChancellorsville.")
            print_slow(f"\nAbout 60,298 Confederate soldiers fought in the {battle}; \n12,764 of them were killed, wounded or captured.\nThis is a 21% casualty rate.")
            print_slow(f"\nThis battle was yet another major {side} victory.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3} or a {sim_roll4} you're captured or wounded.  \nIf you entered a {sim_roll5} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll5:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\nNot only did you survive, but it looks like the \nConfederate States of America might survive this war too -  \nGeneral Lee led your {side} forces to another brilliant victory!")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)


#gettysburg
    if battle == "gettysburg" or battle == "battle of gettysburg":
        battle = "Battle of Gettysburg"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 22
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Lee, encouraged by his victory at Chancellorsville,\nhas invaded Pennsylvania in an attempt to win the war. ")
            print_slow(f"\nGeneral George Meade is leading you and your {side} comrades\ntowards a small crossroads town called \nGettysburg in an attempt to stop him. ")
            print_slow(f"\nYou are among 104,256 Union soldiers fighting in the {battle}. \n23,049 of them were killed, wounded or captured.\nThis is a 22% casualty rate.\n")
            print_slow(f"\nDuring the third day of the battle, Confederate forces charged \nacross an open field and were slaughtered.")
            print_slow(f"\nThe attack was known as Pickett's Charge. \nAbout 50% of the Confederate forces became casualties. ")
            print_slow(f"\nThe battle was a major {side} victory.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3} or a {sim_roll4} you're either captured or wounded.  \nIf you entered a {sim_roll5} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll5:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\nYou are amazed to come through this horrible battle unharmed when \nso many people you know did not.\nThe battle is won and for now, at least, the {side} is saved!")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 33
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Lee, encouraged by his victory at Chancellorsville,\nhas invaded Pennsylvania in an attempt to win the war. ")
            print_slow(f"\nIt is hoped that a {side} victory in Pennsylvania\nwill convince the Union the war cannot be won.")
            print_slow(f"\nAbout 75,000 Confederate soldiers fought in the {battle}; \nAbout 25,000 of them were killed, wounded or captured.\nThis is a 33% casualty rate.")
            print_slow(f"\nThis battle was a significant {side} defeat.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, {sim_roll4}, {sim_roll5} or a {sim_roll6} you're captured or wounded.  \nIf you entered a {sim_roll7} or {sim_roll8}, you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4 or user_number == sim_roll5 or user_number == sim_roll6:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll7 or user_number == sim_roll8:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\nAs your regiment retreats across the field, Union forces begin to chant, 'Fredericksburg!'.")
                print_slow(f"\nThey are reminding you and your comrades that your crushing defeat \nis payback for what you did to them at Fredericksburg.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#wilderness
    if battle == "wilderness" or battle == "the wilderness" or battle == "battle of the wilderness":
        battle = "Battle of the Wilderness"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 15
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"The Army of the Potomac is invading Virginia again\nwith a new commander (again).  His name is General Grant. ")
            print_slow(f"\nGrant promised President Lincoln he wouldn't turn back until he won the war.  \nLet's see if he's true to his word. ")
            print_slow(f"About 118,700 Union soldiers fought in the battle. \n17,666 of them were killed, wounded or captured.\nThis is a 15% casualty rate.\n")
            print_slow(f"The battle was a {side} defeat.\nGeneral Grant, however, is continuing to advance south into Virginia.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, or a {sim_roll3} you're either captured or wounded.  \nIf you entered a {sim_roll4} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll4:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\n{name}, you survived! Let's hope that General Grant\nis the one who can finally defeat General Lee.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 17
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Lee, in command of the {side} Army of Northern Virginia,\nis moving to stop a Union invasion of Virginia. ")
            print_slow(f"\nThe Union army is led by General Grant.\nLee hopes to stop Grant near a region of dense woods called The Wilderness. ")
            print_slow("\nAbout 66,140 Confederate soldiers fought in the battle;\n11,033 of them were killed, wounded or captured.\nThis is a 17% casualty rate.")
            print_slow(f"\nThis battle was a {side} victory,\nbut Union General Grant is advancing south regardless.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, or a {sim_roll3} you're either captured or wounded.  \nIf you entered a {sim_roll4} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3:
                wounded_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll4:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_three(side,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#petersburg
    if battle == "petersburg" or battle == "battle of petersburg" or battle == "siege of petersburg":
        battle = "Siege of Petersburg"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 34
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Grant has moved the Army of the Potomac south of Richmond\nto a railroad junction town called Petersburg. ")
            print_slow(f"\nInstead of one battle, this movement turns into a\nsiege that lasts about 10 months. ")
            print_slow("During the siege, \nabout 125,000 Union soldiers were engaged in combat. \n42,000 of them were killed, wounded or captured.\nThis is a 34% casualty rate.\n")
            print_slow(f"The battle was a {side} victory.\nGrant took Petersburg and the Confederate government fled Richmond.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, {sim_roll4}, {sim_roll5} or a {sim_roll6} you're either captured or wounded.  \nIf you entered a {sim_roll7} or a {sim_roll8} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4 or user_number == sim_roll5 or user_number == sim_roll6:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll7 or user_number == sim_roll8:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\n{name}, you survived! Richmond is ours! The war is coming to an end.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 47
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Lee is moving you and your comrades to Petersburg,\nan important railroad junction south of Richmond. ")
            print_slow(f"\nIf Petersburg falls and the Union captures the railroad,\nRichmond - the capital of the Confederacy - will fall too. ")
            print_slow("\nAbout 60,000 Confederate soldiers fought in the battle;\n28,000 of them were killed, wounded or captured.\nThis is a crushing 47% casualty rate.")
            print_slow(f"\nThis battle was a {side} defeat, and the war looks like it is lost.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, {sim_roll4}, {sim_roll5},\n{sim_roll6}, {sim_roll7}, {sim_roll8}, {sim_roll9} or a {sim_roll10} you're either captured or wounded.  \nIf you entered a {sim_roll11} or a {sim_roll12} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4 or user_number == sim_roll5 or user_number == sim_roll6 or user_number == sim_roll7 or user_number == sim_roll8 or user_number == sim_roll9 or user_number == sim_roll10:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll11 or user_number == sim_roll12:
                killed_in_action(name,battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_two(battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#sailor's creek
    if battle == "sailors creek" or battle == "sailor's creek" or battle == "battle of sailors creek" or battle == "battle of sailor's creek":
        battle = "Battle of Sailor's Creek"
#call random_roll function
        sim_roll, sim_roll2, sim_roll3, sim_roll4, sim_roll5, sim_roll6, sim_roll7, sim_roll8, sim_roll9, sim_roll10, sim_roll11, sim_roll12 = random_roll()
        if side == "Union":
            casualty_rate += 5
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"General Grant is closely pursuing Lee's retreating Army of Northern Virginia. ")
            print_slow(f"\nIf Grant can attack and defeat Lee, this war is as good as over.\nGrant caught up with Lee at a small creek called Sailor's Creek. ")
            print_slow("\nDuring the battle, \nabout 25,000 Union soldiers were engaged in combat. \n1,148 of them were killed, wounded or captured.\nThis is a 5% casualty rate.\n")
            print_slow(f"The battle was a huge {side} victory.\nAbout 25% of Lee's army surrendered.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, you're either captured or wounded.  \nIf you entered a {sim_roll2} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll:
                wounded_two(name,side)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll2:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                print_slow(f"\n{name}, you survived! General Lee has surrendered to General Grant!\nOur national nightmare is finally over.")
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
        if side == "Confederate":
            casualty_rate += 42
            overall_rate = average_casualty_rate(casualty_rate,battles_fought)
            print_slow(f"Since General Grant broke through at Petersburg, {name},\nyou and your comrades are on the run. ")
            print_slow(f"\nGrant caught up to Lee at a small creek called Sailor's Creek.\nIt was Grant's and Lee's last battle. ")
            print_slow(f"\nAbout 18,500 Confederate soldiers fought in the battle;\n7,700 of them were killed, wounded or captured.\nThis is a 42% casualty rate.")
            print_slow(f"\nThis battle was a {side} defeat,\nand General Lee surrendered to General Grant shortly after.")
            user_number = get_user_number()
            print_slow(f"If you entered a {sim_roll}, {sim_roll2}, {sim_roll3}, {sim_roll4}, {sim_roll5},\n{sim_roll6}, {sim_roll7}, {sim_roll8}, {sim_roll9} or a {sim_roll10} you're either captured or wounded.  \nIf you entered a {sim_roll11} you're dead. ")
            print_slow(f"\nYou entered a {user_number}.")
            if user_number == sim_roll or user_number == sim_roll2 or user_number == sim_roll3 or user_number == sim_roll4 or user_number == sim_roll5 or user_number == sim_roll6 or user_number == sim_roll7 or user_number == sim_roll8 or user_number == sim_roll9 or user_number == sim_roll10:
                captured_one(name)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)
            elif user_number == sim_roll11:
                killed_in_action_two(battle)
                casualty_rate_statement(overall_rate)
                alive = False
                break
            else:
                survived_three(side,battle)
                survived_battles_statement(battles_fought)
                casualty_rate_statement(overall_rate)

#end of the simulation - this runs after the loop finishes, whether the player survived or died
print()
print(line)
if alive:
    print_slow(f"Congratulations, {name}!  Your enlistment is up,\nand you've earned the right to go home in peace.")
    print_slow(f"\nYou, unlike many of your fellow {side} soldiers, survived the Civil War.\n")
    print(line)
print_slow(sim_end_statement)
print()
