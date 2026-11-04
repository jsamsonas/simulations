import time
import sys
import textwrap

def clear_screen():
    # Prints blank lines to simulate a screen clear for readability
    print("\n" * 40)

def wrap(text, width=76):
    # Wraps long lines so words aren't split across lines on screen
    return "\n".join(textwrap.fill(line, width) if len(line) > width else line
                     for line in text.split("\n"))

def slow_print(text, delay=0.015):
    # Simulates a teletype/telegraph effect by printing character by character
    for char in wrap(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n" + "-" * 60)

def slow_text_only(text, delay=0.015):
    # Same as above but without the dashed line at the end
    for char in wrap(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class CivilWarSimulation:
    def __init__(self):
        self.score = 0
        self.player_name = ""

        # Define the four scenarios based on the turning points
        self.scenarios = [
            {
                "title": "Turning Point 1: The Aftermath of Antietam (September 1862)",
                "role": "Major General George B. McClellan",
                "background": "The Battle of Antietam has just concluded. It is the bloodiest single day in American military history. You have successfully halted Confederate General Robert E. Lee's invasion of Maryland. President Lincoln desperately needs a definitive victory here to safely issue his preliminary Emancipation Proclamation without it looking like an act of desperation. Lee's army is battered and backed up against the Potomac River, but they are holding their ground.",
                "advisors": {
                    "1": {"name": "General Fitz John Porter", "title": "Corps Commander", "advice": "General, our men are exhausted. We have taken horrific casualties. Keep the V Corps in reserve. If we attack and fail, the capital is lost."},
                    "2": {"name": "General Ambrose Burnside", "title": "Corps Commander", "advice": "We have Lee pinned! He has no reserves left. Send in the fresh troops now and we can destroy the Army of Northern Virginia today!"},
                    "3": {"name": "President Abraham Lincoln", "title": "via telegraph", "advice": "General, you must destroy the rebel army. I need a decisive victory to change the political goals of this war. Do not let General Lee escape across the river."}
                },
                "options": {
                    "A": "Commit your fresh reserves (the V Corps) in a massive frontal assault to crush Lee's army.",
                    "B": "Hold your position, claim a defensive victory, and allow Lee to retreat across the Potomac.",
                    "C": "Wait two days for reinforcements from Washington before making any offensive moves."
                },
                "results": {
                    "A": {"points": 10, "text": "Aggressive, but potentially war-winning. Historically, McClellan did NOT do this. He was too cautious. Had he attacked, he might have destroyed Lee's army and shortened the war. Lincoln issued the Emancipation Proclamation anyway, but was furious that Lee escaped."},
                    "B": {"points": 5, "text": "This is what McClellan historically did. You secured a strategic victory, which gave Lincoln the political capital to issue the Emancipation Proclamation, changing the war's goals. However, your caution allowed the war to continue for three more years."},
                    "C": {"points": 0, "text": "Waiting gave Lee the perfect opportunity to slip his entire army safely across the Potomac River under the cover of darkness. You lost the chance to end the war early."}
                }
            },
            {
                "title": "Turning Point 2: The Summer of '63 - Gettysburg (July 1863)",
                "role": "Major General George Meade",
                "background": "It is July 4th, 1863. Yesterday, you decisively defeated Lee's army at Gettysburg, repulsing Pickett's Charge. Word has also just arrived that General Grant has captured Vicksburg in the West, splitting the Confederacy. Lee's army is now retreating through a heavy rainstorm toward the swollen Potomac River. Your army is victorious but completely exhausted.  Should you risk an aggressive pursuit in the mud to try to destroy Lee's army, or should you let them escape and consolidate your victory at Gettysburg?",
                "advisors": {
                    "1": {"name": "General John Sedgwick", "title": "Corps Commander", "advice": "General Meade, our army is shattered. We have lost over 20,000 men. We need to rest, resupply, and tend to our wounded before we can even think of moving."},
                    "2": {"name": "General Alfred Pleasonton", "title": "Cavalry Commander", "advice": "The rebels are retreating in chaos! The rain has flooded the river, trapping them. If we march immediately, we can pin them against the water and force a surrender of the entire army."},
                    "3": {"name": "General Henry Halleck", "title": "General-in-Chief", "advice": "The President expects you to pursue and destroy Lee's army before they cross the river. Do not let this opportunity slip away, but protect Washington."}
                },
                "options": {
                    "A": "Launch an immediate, aggressive pursuit through the mud to attack General Lee's rearguard.",
                    "B": "Shadow General Lee's retreat cautiously, waiting to see if he makes a mistake before attacking.",
                    "C": "Remain at Gettysburg to bury the dead, care for the wounded, and wait for better weather."
                },
                "results": {
                    "A": {"points": 10, "text": "A bold move! Historians debate if General Meade's battered army could have destroyed General Lee, but Lincoln believed an aggressive pursuit would have ended the war right there."},
                    "B": {"points": 5, "text": "This is exactly what Meade did. You pursued cautiously. By the time you caught up to Lee, the river had receded enough for him to escape. The twin victories of Gettysburg and Vicksburg crippled the South, but the war went on."},
                    "C": {"points": 0, "text": "By refusing to move, you give General Lee a massive head start. While your men appreciate the rest, Washington is furious at your lack of initiative."}
                }
            },
            {
                "title": "Turning Point 3: The Overland Campaign (May 1864)",
                "role": "Lieutenant General Ulysses S. Grant",
                "background": "You have been promoted to command all Union armies. You just fought the gruesome Battle of the Wilderness in dense, burning woods. You took massive casualties (over 17,000 men), and tactically, it looks like a defeat. The Northern public is growing terribly tired of the endless death toll. In the past, Union generals who lost to Confederate General Lee here always retreated back to Washington to regroup.",
                "advisors": {
                    "1": {"name": "General George Meade", "title": "Army Commander", "advice": "We have taken a beating, General. The men are demoralized. Standard procedure is to fall back across the Rapidan River to resupply and plan a new campaign."},
                    "2": {"name": "Charles Dana", "title": "War Department Observer", "advice": "Grant, the political fallout in Washington will be severe. The public cannot stomach these casualties. Lincoln's re-election is in jeopardy if we keep bleeding like this."},
                    "3": {"name": "General Philip Sheridan", "title": "Cavalry Commander", "advice": "Do not retreat! General Lee wants us to back down. If we keep pressing him, he will run out of men before we do. We must maintain contact."}
                },
                "options": {
                    "A": "Retreat across the river to resupply and appease the anxious public.",
                    "B": "Slide your army to the left (South) toward Spotsylvania, refusing to retreat and forcing Lee to fight again.",
                    "C": "Order another massive frontal assault straight into the burning woods."
                },
                "results": {
                    "A": {"points": 0, "text": "This would have been a disaster. By retreating, you give up the initiative, prolonging the war and devastating Northern morale. This is exactly what Lincoln feared you would do."},
                    "B": {"points": 10, "text": "This is what Grant did! When the troops realized they were marching South instead of retreating North, they cheered. This decision to relentlessly press Lee, despite the horrific casualties, was the turning point that doomed the Confederacy."},
                    "C": {"points": 5, "text": "An assault here would result in senseless slaughter. While aggressive, it lacks strategic finesse. You must press the enemy, but not blindly."}
                }
            },
            {
                "title": "Turning Point 4: The Fall of Atlanta & The Election (September 1864)",
                "role": "Major General William T. Sherman",
                "background": "You have successfully captured the critical rail hub of Atlanta! This massive victory has drastically boosted Northern morale just in time to ensure President Lincoln's re-election against George McClellan. However, Confederate General John Bell Hood has taken his army and marched North to attack your supply lines in Tennessee. You are deep in enemy territory.",
                "advisors": {
                    "1": {"name": "General George Thomas", "title": "The 'Rock of Chickamauga'", "advice": "Sherman, you must protect your supply lines! Send forces back into Tennessee to chase Hood down and destroy him before he ruins everything we've built."},
                    "2": {"name": "President Abraham Lincoln", "title": "via telegraph", "advice": "I am worried about your army being stranded deep in Georgia without supplies. Please coordinate with General Thomas to secure your rear."},
                    "3": {"name": "General Ulysses S. Grant", "title": "General-in-Chief", "advice": "If you can split the Confederacy again, do it. I trust your judgment, but ensure Hood doesn't undo our progress in the West."}
                },
                "options": {
                    "A": "Turn your entire army around and chase Hood's army into Tennessee.",
                    "B": "Heavily fortify Atlanta, hunker down for the winter, and wait for Hood to attack you.",
                    "C": "Send a fraction of your men to deal with Hood, abandon your supply lines entirely, and march the rest of your army to the Sea (Savannah)."
                },
                "results": {
                    "A": {"points": 5, "text": "A safe, traditional military move. However, chasing Hood through the mountains would be slow and exhausting, bogging down the war effort when Lincoln needed a final push."},
                    "B": {"points": 0, "text": "Hunkering down wastes the momentum of your victory. It allows the Confederacy time to regroup and gives the Northern public the impression that the war is stalled again."},
                    "C": {"points": 10, "text": "Brilliant and historically accurate! You sent Thomas to crush Hood, while you undertook the famous 'March to the Sea'. By abandoning your supply lines, you destroyed the Confederacy's ability to wage war and broke the South's psychological will to fight."}
                }
            }
        ]

    def start(self):
        clear_screen()
        print("=========================================================")
        print("        CROSSROADS OF THE CIVIL WAR: A SIMULATION        ")
        print("=========================================================")
        print("\nWelcome to the Command Tent.")
        self.player_name = input("Please enter your last name to begin: ")

        welcome_msg = f"\nWelcome, General {self.player_name}. The fate of the United States rests heavily upon your shoulders.\nYou will face four critical turning points. Review the intelligence, consult your advisors, and make your orders."
        slow_print(welcome_msg)

        input("\nPress Enter to begin the campaign...")

        for index, scenario in enumerate(self.scenarios):
            self.run_scenario(index + 1, scenario)

        self.end_game()

    def run_scenario(self, num, scenario):
        clear_screen()
        print(f"--- {scenario['title']} ---")
        print(f"Your Role: {scenario['role']} (Acting as General {self.player_name})")
        print("\nBACKGROUND:")
        slow_print(scenario['background'])

        while True:
            # Extract names for the menu
            adv1 = scenario['advisors']['1']
            adv2 = scenario['advisors']['2']
            adv3 = scenario['advisors']['3']

            print("\nCOMMAND MENU:")
            print(f"1. Consult {adv1['name']} ({adv1['title']})")
            print(f"2. Consult {adv2['name']} ({adv2['title']})")
            print(f"3. Consult {adv3['name']} ({adv3['title']})")
            print("4. Make your official decision")

            choice = input("\nEnter your choice (1-4): ").strip()

            if choice in ['1', '2', '3']:
                advisor = scenario['advisors'][choice]
                print(f"\n*** INCOMING DISPATCH: {advisor['name']} ***")
                slow_text_only(f"\"{advisor['advice']}\"")
                input("\nPress Enter to return to the Command Menu...")
            elif choice == '4':
                self.make_decision(scenario)
                break
            else:
                print("\nInvalid input. Please select 1, 2, 3, or 4.")

    def make_decision(self, scenario):
        print("\n=========================================================")
        print("THE DECISION")
        print("=========================================================")
        for key, text in scenario['options'].items():
            slow_text_only(f"Option {key}: {text}", delay=0.01)

        while True:
            decision = input("\nGeneral, what are your orders? (A/B/C): ").strip().upper()
            if decision in scenario['options']:
                result = scenario['results'][decision]
                points_earned = result['points']
                self.score += points_earned

                print("\n=========================================================")
                print("AFTERMATH")
                print("=========================================================")
                slow_text_only(result['text'])
                print(f"\nPoints earned for this decision: {points_earned}/10")
                input("\nPress Enter to proceed to the next phase of the war...")
                break
            else:
                print("Invalid order, General. Please choose A, B, or C.")

    def end_game(self):
        clear_screen()
        print("=========================================================")
        print("                   WAR'S END                             ")
        print("=========================================================")
        slow_text_only(f"General {self.player_name}, the war is over. Your decisions have shaped history.")
        print(f"\nFinal Command Score: {self.score} / 40")

        print("\nEvaluation:")
        if self.score == 40:
            slow_text_only("Master Strategist! You made brilliant, aggressive choices that crushed the rebellion swiftly.")
        elif self.score >= 25:
            slow_text_only("Capable Commander. You steered the Union to victory, though some of your choices prolonged the bloodshed.")
        elif self.score >= 10:
            slow_text_only("Overly Cautious. You survived the war, but your lack of initiative cost thousands of lives and nearly lost the political will to fight.")
        else:
            slow_text_only("Relieved of Command. Your decisions were detrimental to the Union cause. It is a miracle the nation survived.")

        print("\nThank you for playing the simulation!")

if __name__ == "__main__":
    game = CivilWarSimulation()
    game.start()
