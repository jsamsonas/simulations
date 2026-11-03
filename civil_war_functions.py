#import needed modules
import sys
import time
import random

line = "______________________________________________________________________________"

#battles players can type in (lowercase) - used to check their choice
valid_battles = [
    "bull run", "battle of bull run",
    "peninsula campaign", "peninsula",
    "antietam", "battle of antietam",
    "fredericksburg", "battle of fredericksburg",
    "chancellorsville", "battle of chancellorsville",
    "gettysburg", "battle of gettysburg",
    "wilderness", "the wilderness", "battle of the wilderness",
    "petersburg", "battle of petersburg", "siege of petersburg",
    "sailors creek", "sailor's creek", "battle of sailors creek", "battle of sailor's creek",
]

#remembers whether print_slow left the cursor in the middle of a line
_line_open = False

def print_slow(text):
    global _line_open
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    if text:
        _line_open = not text.endswith("\n")

def ask(prompt):
    #works like input(), but first finishes any half-printed line so the
    #web terminal doesn't erase it when it shows the prompt
    global _line_open
    if _line_open:
        sys.stdout.write("\n")
        sys.stdout.flush()
        _line_open = False
        if prompt.startswith("\n"):
            prompt = prompt[1:]
    return input(prompt)

def get_user_name():
    name = ""
    while name == "":
        name = ask("Please enter your name: ").strip().lower().title()
    return name

def sim_introduction(name):
    print_slow(f"\nWelcome, {name}! It is 1861, and the United States is at war with itself.")
    print_slow("\nIn this simulation you will enlist as a soldier and fight in some of the")
    print_slow("\nmajor battles of the Civil War in the Eastern Theater.")
    print_slow("\nYour chances of being wounded, captured or killed in each battle are based")
    print_slow("\non the real casualty rates for your side in that battle.")
    print_slow("\nSurvive your enlistment and you get to go home.\n")

def get_user_side():
    side = ""
    side_list = ["union", "confederate"]
    while side not in side_list:
        side = ask("Please choose a side to fight on.\nYou can choose either 'Union' or 'Confederate': ").strip().lower()
        if side not in side_list:
            print_slow("Please pick a side or make sure you spell the side you chose correctly.\n")
    return side

def greet_user_side(name, side):
    if side == "Union":
        print_slow(f"\nWelcome to the Army of the Potomac, Private {name}!")
        print_slow("\nYou have enlisted for 6 battles. Fight for the Union!\n")
    else:
        print_slow(f"\nWelcome to the Army of Northern Virginia, Private {name}!")
        print_slow("\nYou have enlisted for 8 battles. Fight for the Confederacy!\n")

def battle_selection():
    battle = ""
    while battle not in valid_battles:
        battle = ask("\nWhich battle would you like to fight in? ").strip().lower()
        if battle not in valid_battles:
            print_slow("Please choose a battle from the list, and check your spelling.")
    return battle

def random_roll():
    numbers_list = list(range(1, 26))
    random.shuffle(numbers_list)
    return tuple(numbers_list[:12])

def get_user_number():
    while True:
        answer = ask("\nEnter a number between 1-25 to determine if you're killed, captured or wounded: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= 25:
            return int(answer)
        print_slow("Please enter a whole number from 1 to 25.")

def wounded_one(name):
    print_slow(f"\nI can see that you're wounded, {name}.")
    print_slow("\nI'll take you to the regimental surgeon.")

def wounded_two(name, side):
    print_slow(f"\nA staggering number of {side} soldiers were wounded today, {name}.")
    print_slow("\nUnfortunately, you were among them.")

def captured_one(name):
    print_slow(f"\nYou've been captured, {name}.")
    print_slow("\nYou spend months in a crowded prison camp before you are finally exchanged")
    print_slow("\nand returned to your regiment.")

def killed_in_action(name, battle):
    print_slow(f"\nA few days from now, {name}, your family will read about the {battle}.")
    print_slow("\nUnfortunately, they will see your name listed among those who died.")

def killed_in_action_two(battle):
    print_slow(f"\nUnfortunately, you were killed in action during the {battle}.")

def survived_one(name, battle):
    print_slow(f"\nAs the fighting dies down, {name}, you're overjoyed that you survived the {battle}.")

def survived_two(battle):
    print_slow("\nAs you sit around the camp fire that evening, you mourn the loss of friends.")
    print_slow(f"\nAt the same time, you thank God that you survived the {battle}.")

def survived_three(side, battle):
    print_slow(f"\nAs the long lines of {side} soldiers march away from the {battle},")
    print_slow("\nyou count yourself fortunate that you came away unharmed.")

def survived_battles_statement(battles_fought):
    if battles_fought == 1:
        print_slow("\nYou have survived 1 battle.")
    else:
        print_slow(f"\nYou have survived {battles_fought} battles.")

def average_casualty_rate(casualty_rate, battles_fought):
    overall_rate = casualty_rate / battles_fought
    return overall_rate

def casualty_rate_statement(overall_rate):
    print_slow(f"\nThe average casualty rate in the battles you've fought is {overall_rate:.0f}%.\n")
