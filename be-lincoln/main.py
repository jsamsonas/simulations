import time
import sys
import textwrap

# =====================================================================
# HISTORICAL DATA DICTIONARY
# =====================================================================

SIMULATION_DATA = {
    "trent_affair": {
        "title": "The Trent Affair (Late 1861)",
        "intro": "The Union Navy has intercepted a British mail ship, the Trent, and arrested two Confederate diplomats (James Mason and John Slidell) who were on their way to Europe to seek help for the South. The Northern public is thrilled, but Great Britain is furious. They consider this an illegal act of war, and they are sending thousands of troops to Canada, ready to attack the Union.",
        "options": {
            "A": "Keep the diplomats imprisoned. The Union Navy acted bravely, and the South cannot be allowed to make alliances.",
            "B": "Apologize to Great Britain and release the diplomats to keep the British out of the war.",
            "C": "Release the diplomats but publicly refuse to issue a formal apology, hoping that satisfies both sides without looking weak."
        },
        "advisors": [
            {"name": "Gideon Welles (Secretary of the Navy)", "opinion": "Captain Wilkes is a national hero! We cannot back down now. The public demands we keep them locked up!"},
            {"name": "William Seward (Secretary of State)", "opinion": "Mr. President, Britain is readying for war. Our military is already stretched thin fighting the Confederacy. We cannot survive fighting the South and the British Empire at the same time."},
            {"name": "Senator Charles Sumner", "opinion": "According to international law, Great Britain is actually in the right here. We must release them to avoid a disastrous war that would destroy the Union."}
        ],
        "lincoln_choice": "B",
        "lincoln_action_phrase": "apologize to Great Britain and release the diplomats",
        "reveal": "By swallowing his pride and angering the Northern public, Lincoln successfully kept Great Britain out of the Civil War, which was crucial for the Union's eventual victory. He reportedly remarked, 'One war at a time.'"
    },
    "hunters_proclamation": {
        "title": "General Hunter's Unauthorized Proclamation (May 1862)",
        "intro": "General David Hunter, a Union commander, has just issued a military order freeing all enslaved people in South Carolina, Georgia, and Florida. He did this without asking for your permission! The abolitionists are cheering, but politicians in the Border States (slave states that stayed in the Union) are threatening to leave and join the Confederacy if you let this stand.",
        "options": {
            "A": "Let the order stand. It weakens the rebellion and does the right thing by freeing enslaved people.",
            "B": "Revoke the order immediately. Remind everyone that only the President, not generals, has the power to make such massive political decisions.",
            "C": "Modify the order to only free enslaved people who are actively being forced to work for the Confederate military, ignoring everyone else."
        },
        "advisors": [
            {"name": "Salmon P. Chase (Secretary of the Treasury)", "opinion": "Let the order stand! It weakens the Confederacy's economy and is morally just. It's time to strike a blow against slavery."},
            {"name": "Border State Politicians", "opinion": "If you do not cancel this radical order, our states will secede! You will lose Maryland, Kentucky, and Missouri, and the Union will be lost!"},
            {"name": "Horace Greeley (Newspaper Editor)", "opinion": "Finally, a General taking real action! Do not interfere with General Hunter. The people are behind him."}
        ],
        "lincoln_choice": "B",
        "lincoln_action_phrase": "revoke the unauthorized emancipation order",
        "reveal": "Lincoln stated clearly that he, as Commander-in-Chief, was the only one who could issue such an order, and he desperately needed the Border States to stay in the Union. However, secretly, Lincoln had already begun drafting the Emancipation Proclamation."
    },
    "dakota_war": {
        "title": "The Dakota War Executions (Late 1862)",
        "intro": "Following an uprising by the Dakota people in Minnesota due to broken treaties and starvation, a military tribunal has sentenced 303 Dakota men to hang. White settlers in Minnesota are demanding mass executions, threatening mob violence if you don't approve them. However, reviewing the transcripts shows the trials were incredibly rushed and unfair.",
        "options": {
            "A": "Approve all 303 executions to appease the furious settlers and prevent mob violence in Minnesota.",
            "B": "Pardon all 303 men. The military tribunals were a sham, and the Dakota were driven to violence by the government breaking its promises.",
            "C": "Personally review the trial transcripts and only approve the executions of those proven to have massacred civilians, rather than those who just fought in battles."
        },
        "advisors": [
            {"name": "General John Pope", "opinion": "You must approve all the executions, Mr. President. If you do not, the white settlers will take the law into their own hands and slaughter every Native American in the state."},
            {"name": "Bishop Henry Whipple", "opinion": "President {student_name}, this system is broken. Our own corrupt agents starved the Dakota into war. You must show mercy and reform the system."},
            {"name": "Gideon Welles (Secretary of the Navy)", "opinion": "You are a lawyer, sir. You must look at the evidence. We cannot execute men based on sham trials, but we also cannot let murderers go free."}
        ],
        "lincoln_choice": "C",
        "lincoln_action_phrase": "review the transcripts and reduce the executions to 38",
        "reveal": "Lincoln and his lawyers worked for weeks reviewing the transcripts. He commuted the death sentences of 265 men, allowing 38 to be hanged. While it remains the largest mass execution in US history, Lincoln's decision to intervene cost him politically but prevented a much larger, legally baseless slaughter."
    },
    "cabinet_coup": {
        "title": "The Cabinet Coup (December 1862)",
        "intro": "The war is going terribly. After the devastating Union loss at Fredericksburg, Radical Republican Senators are furious. They blame your trusted Secretary of State, William Seward, for the Union's failures and demand you fire him. Your Secretary of the Treasury, Salmon P. Chase, has been secretly encouraging these Senators. Seward has offered his resignation to save you the trouble.",
        "options": {
            "A": "Accept Seward's resignation to please the powerful Senators and try to unite the Republican party.",
            "B": "Refuse to let the Senate dictate your cabinet. Trap the Senators and Chase in a meeting so you can keep your team intact.",
            "C": "Fire Secretary Chase immediately for his disloyalty and publicly defend Seward."
        },
        "advisors": [
            {"name": "Senator William Fessenden", "opinion": "Seward is a terrible influence on you, President {student_name}. You must dismiss him immediately to save the country from ruin."},
            {"name": "William Seward (Secretary of State)", "opinion": "I will resign my post to save you from this political crisis, Mr. President. My presence is tearing the government apart."},
            {"name": "Salmon P. Chase (Secretary of the Treasury)", "opinion": "(In public to you) We must do what is best for the Union. (In secret to the Senators) Seward is ruining everything, the President is too weak to stop him."}
        ],
        "lincoln_choice": "B",
        "lincoln_action_phrase": "refuse to let the Senate dictate your cabinet",
        "reveal": "Lincoln set up a surprise meeting between the angry Senators and his entire Cabinet (except Seward). He forced Secretary Chase to defend the Cabinet in front of the Senators he had secretly been complaining to. Embarrassed, Chase offered his resignation the next day. Lincoln refused both resignations, effectively keeping his team and proving he was the one in charge."
    },
    "vallandigham": {
        "title": "The Arrest of Clement Vallandigham (May 1863)",
        "intro": "Clement Vallandigham, a prominent Northern politician and vocal critic of your administration, has been making fiery speeches urging soldiers to desert and calling the war a failure. General Burnside had him arrested and tried by a military tribunal, which sentenced him to prison for the rest of the war. Democrats are screaming that you are a tyrant destroying free speech.",
        "options": {
            "A": "Keep him in military prison. Free speech has limits during a rebellion, and he is actively hurting the Union army's morale.",
            "B": "Release him and issue an apology. Arresting a political opponent for a speech violates the First Amendment.",
            "C": "Change his sentence from prison to banishment. Send him across enemy lines into the Confederacy."
        },
        "advisors": [
            {"name": "General Ambrose Burnside", "opinion": "The man is a traitor! He is discouraging enlistments while our boys are dying. He must remain locked up!"},
            {"name": "Northern Democrats", "opinion": "Tyrant! You are destroying the Constitution! A man has the right to criticize the government without being thrown in a military dungeon!"},
            {"name": "A Moderate Republican Advisor", "opinion": "If you keep him in prison, you make him a martyr. If you release him, you look weak. We must find a creative way to get rid of him."}
        ],
        "lincoln_choice": "C",
        "lincoln_action_phrase": "banish Vallandigham to the Confederacy",
        "reveal": "In a brilliant political maneuver, Lincoln commuted the prison sentence and ordered Vallandigham banished to the South. By sending him to the people he claimed to sympathize with, Lincoln made Vallandigham look ridiculous rather than like a martyr for free speech, deflating the crisis."
    },
    "fort_pillow": {
        "title": "The Fort Pillow Massacre Response (April 1864)",
        "intro": "Horrific news has reached Washington. Confederate troops under General Nathan Bedford Forrest captured Fort Pillow in Tennessee. Instead of taking the surrendered Black Union soldiers as prisoners of war, the Confederates massacred them. The Northern public and your military advisors are absolutely outraged, demanding blood for blood.",
        "options": {
            "A": "Order the immediate execution of Confederate prisoners of war in retaliation for the murdered Black soldiers.",
            "B": "Demand an official investigation and threaten retaliation, but hold off on mass executions to prevent the war from becoming a cycle of endless murder.",
            "C": "Issue an order refusing to take any Confederate prisoners at all going forward. No quarter shall be given."
        },
        "advisors": [
            {"name": "Edwin Stanton (Secretary of War)", "opinion": "We must retaliate immediately! For every Black soldier murdered at Fort Pillow, we must execute a Confederate prisoner of war. They must learn there are consequences!"},
            {"name": "Frederick Douglass (Abolitionist Leader)", "opinion": "The Confederacy must be taught that Black soldiers are Union soldiers. Severe retaliation is the only way to protect them from future massacres."},
            {"name": "Gideon Welles (Secretary of the Navy)", "opinion": "Executing defenseless prisoners is savage, President {student_name}. We cannot sink to the Confederacy's level, or this war will become a dark cycle of endless revenge and bloodletting."}
        ],
        "lincoln_choice": "B",
        "lincoln_action_phrase": "demand an investigation rather than order mass executions",
        "reveal": "Lincoln officially threatened retaliation, but he ultimately could not bring himself to order the mass execution of innocent Confederate prisoners. He feared it would trigger a horrific cycle of revenge killings that would destroy the humanity of the nation. The lack of direct retaliation frustrated many, but it prevented the war from descending into further barbarism."
    },
    "hampton_roads": {
        "title": "The Hampton Roads Peace Conference (February 1865)",
        "intro": "The war is nearing its end, and the South is losing. Confederate leaders, including their Vice President Alexander Stephens, have requested a secret meeting to discuss peace. The country is exhausted by the horrific death toll. Some in the North want peace at any price, while others demand you crush the South utterly.",
        "options": {
            "A": "Accept a ceasefire immediately. Agree to let them keep slavery as long as they stop shooting and rejoin the Union.",
            "B": "Refuse to meet with them entirely. The only acceptable outcome is their unconditional surrender and total destruction.",
            "C": "Meet with them, but insist that the war will only stop if they rejoin the Union and accept the end of slavery entirely."
        },
        "advisors": [
            {"name": "Francis Preston Blair (Journalist & Politician)", "opinion": "Mr. President, the slaughter must end. Meet with them. Find a compromise. Bring our boys home."},
            {"name": "Radical Republican Congressman", "opinion": "Do not negotiate with traitors! If you compromise on slavery now, all those hundreds of thousands of men will have died for nothing!"},
            {"name": "William Seward (Secretary of State)", "opinion": "You should hear them out, sir. But you hold all the cards. We are winning. Do not give up the core goals of this war."}
        ],
        "lincoln_choice": "C",
        "lincoln_action_phrase": "meet but refuse to compromise on reunion and emancipation",
        "reveal": "Lincoln personally attended the Hampton Roads conference. He was willing to listen, but he held firm to his absolute conditions: the Confederacy must disband, rejoin the Union, and accept the abolition of slavery. The Confederates refused, and the war continued for two more bloody months until Lee's surrender at Appomattox."
    }
}

# =====================================================================
# SIMULATION FUNCTIONS
# =====================================================================

def slow_print(text, delay=0.025):
    """Prints text one character at a time for a typewriter effect."""
    # Wrap long lines at 76 characters so words aren't split across lines
    text = "\n".join(textwrap.fill(line, 76) if len(line) > 76 else line
                     for line in text.split("\n"))
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() # Move to the next line after finishing the string

def print_separator():
    print("\n" + "="*70 + "\n")

def run_scenario(scenario_key, student_name):
    """Runs a single scenario and returns True if the student matched Lincoln, False otherwise."""
    scenario = SIMULATION_DATA[scenario_key]

    print_separator()
    slow_print(f"--- {scenario['title'].upper()} ---", 0.03)
    print("\nTHE SITUATION:")
    slow_print(scenario["intro"].format(student_name=student_name))

    # Advisor Loop
    while True:
        print("\n" + "-"*40)
        slow_print("WHO WOULD YOU LIKE TO CONSULT?", 0.02)

        # List out the available advisors dynamically
        for i, advisor in enumerate(scenario["advisors"]):
            print(f"{i + 1}) {advisor['name']}")

        decision_number = len(scenario["advisors"]) + 1
        print(f"{decision_number}) I'm ready to make my decision.")

        choice = input("\nEnter a number: ").strip()

        try:
            choice_index = int(choice) - 1

            if 0 <= choice_index < len(scenario["advisors"]):
                # Student picked an advisor
                advisor = scenario["advisors"][choice_index]
                opinion = advisor["opinion"].format(student_name=student_name)
                print("\n" + "."*20)
                slow_print(f"[{advisor['name']} enters the room...]", 0.03)
                slow_print(f"\"{opinion}\"")
                print("."*20)
                time.sleep(0.8) # A brief pause before looping the menu

            elif choice_index == len(scenario["advisors"]):
                # Student is ready to decide
                break

            else:
                print("\nInvalid choice. Please pick a number from the list.")
        except ValueError:
            print("\nPlease enter a valid number.")

    # Present the final options dynamically
    print("\n" + "="*40)
    slow_print("IT IS TIME TO DECIDE.", 0.03)
    print("YOUR OPTIONS:")

    valid_choices = list(scenario["options"].keys())
    for key in valid_choices:
        slow_print(f"{key}) {scenario['options'][key]}", 0.02)

    # Input loop to ensure the student chooses a valid option
    options_str = ", ".join(valid_choices[:-1]) + f", or {valid_choices[-1]}"
    while True:
        student_choice = input(f"\nPresident {student_name}, what is your order? (Type {options_str}): ").strip().upper()
        if student_choice in valid_choices:
            break
        print(f"Invalid choice. Please enter {options_str}.")

    print("\n" + "."*30)
    slow_print("PROCESSING HISTORY...", 0.05)
    print("."*30 + "\n")

    # Check if the student made the same choice as Lincoln
    matched_lincoln = (student_choice == scenario["lincoln_choice"])

    if matched_lincoln:
        slow_print(f"Congratulations! You chose to lead like Lincoln and {scenario['lincoln_action_phrase']}.")
        slow_print("Here's how it impacted the nation:\n")
    else:
        slow_print("You made a tough call, but President Lincoln took a different path.")
        slow_print(f"He chose to {scenario['lincoln_action_phrase']}.")
        slow_print("Here's how it impacted the nation:\n")

    slow_print(scenario["reveal"])

    return matched_lincoln

def main():
    print_separator()
    slow_print("      WELCOME TO THE BE LINCOLN SIMULATION      ", 0.03)
    print_separator()

    slow_print("It is the middle of the American Civil War. President Lincoln faces the enormous challenge of keeping the Union together.")
    slow_print("It is your turn to step into his boots and face similar difficulties.")
    slow_print("The fate of the Union and millions of enslaved people rests on your shoulders. Good luck!")

    student_name = input("\nPlease enter your last name: ").strip().title()
    if not student_name:
        student_name = "Lincoln"

    print("\n" + "*"*50)
    slow_print(f"Welcome to the Oval Office, President {student_name}.")
    slow_print("Let's see if you can navigate some of the most difficult choices of the Civil War.")
    print("*"*50)
    time.sleep(1)

    # Updated list of scenarios to play
    scenarios_to_play = [
        "trent_affair",
        "hunters_proclamation",
        "dakota_war",
        "cabinet_coup",
        "vallandigham",
        "fort_pillow",
        "hampton_roads"
    ]

    score = 0
    total_rounds = len(scenarios_to_play)

    # Run through the scenarios and track score
    for i, scenario_key in enumerate(scenarios_to_play):
        is_correct = run_scenario(scenario_key, student_name)

        if is_correct:
            score += 1
        else:
            # Provide encouragement if they missed it
            print()
            if i < total_rounds - 1:
                slow_print("Even though you chose a different option than President Lincoln, you'll have an opportunity to get it right in the next round! Good luck!")
            else:
                slow_print("Even though you chose a different option than President Lincoln, you made it through the hardest choices of the war.")

        # Display running score
        current_round = i + 1
        print("\n" + "-"*30)
        slow_print(f"CURRENT SCORE: {score} / {current_round}", 0.04)
        print("-"*30)

        if current_round < total_rounds:
            input("\nPress Enter to continue to the next crisis...")
        else:
            input("\nPress Enter to view your final results...")

    # Final Sign-off
    print_separator()
    slow_print(f"Your term in office is complete, President {student_name}.")
    slow_print(f"FINAL SCORE: {score} out of {total_rounds} decisions matched Lincoln.")
    print("\nThanks for playing the Be Lincoln Simulation!")
    print_separator()

# =====================================================================
# EXECUTE THE GAME
# =====================================================================
if __name__ == "__main__":
    main()
