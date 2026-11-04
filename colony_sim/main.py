"""
THE COLONY SIMULATION
=====================
Students found a British colony in North America and guide it from the
early 1600s to the eve of the American Revolution. Each round has three
parts:
    1. Invest in the colony (at a price)
    2. Make a historical decision
    3. Survive a random event

If any category drops to 0 or below, the colony fails.

HOW TO EDIT
-----------
All of the game content lives in the dictionaries below:
    INVESTMENTS, ROUNDS, RANDOM_EVENTS
Each "effects" dictionary lists how many points a category gains (+)
or loses (-). The game prints those numbers for students automatically,
so the numbers on screen always match what actually happens.
"""

import random
import sys
import textwrap
import time

# =====================================================================
# TEACHER SETTINGS
# =====================================================================
TEACHERS = ["Mr. Sam", "Mrs. Sondej"]
CLASS_PERIODS = ["1", "2", "3", "4", "5", "6", "7", "8"]
STARTING_POINTS = 50
TYPE_SPEED = 0.02          # seconds per letter (smaller = faster)
WIDTH = 76                 # characters per line

# Each round, the colony produces food and money. What it produces depends
# on the Round 1 decision (trade or farm).
PRODUCTION = {
    "TRADE": {"food": 10, "economy": 15, "population": 5},
    "FARM": {"food": 15, "economy": 10, "population": 5},
}

# The five categories students must keep above zero
CATEGORIES = {
    "food": "Food",
    "economy": "Economy",
    "population": "Population",
    "natives": "Native Relations",
    "britain": "British Relations",
}

# =====================================================================
# INVESTMENTS
# "cost" = points spent. "protects" = random events it softens.
# =====================================================================
INVESTMENTS = {
    "1": {
        "name": "Schools",
        "cost": {"economy": -10, "food": -5},
        "message": "You chose to invest in schools for the children of {colony} - a wise decision!",
        "protects": "Helps during the Great Awakening",
    },
    "2": {
        "name": "Forts/Militia",
        "cost": {"economy": -20, "food": -5, "population": -5, "natives": -10},
        "message": "In this new and often hostile land, being prepared to defend yourself is always a good idea, {first}!",
        "protects": "Protects against Native War and Pirate Attack",
    },
    "3": {
        "name": "Infrastructure (roads, bridges, ports)",
        "cost": {"economy": -15, "food": -5, "natives": -5},
        "message": "Roads, bridges and ports will help {colony} prosper.",
        "protects": "Protects against Drought and Hurricane",
    },
    "4": {
        "name": "Medical Care",
        "cost": {"economy": -10, "food": -5},
        "message": "You chose to build more medical facilities for {colony}.",
        "protects": "Protects against Smallpox",
    },
    "5": {
        "name": "Representative to Britain",
        "cost": {"economy": -10, "food": -5},
        "message": "You chose to send someone to London to speak for {colony}.",
        "protects": "Protects against Caught Smuggling",
    },
}

# =====================================================================
# HISTORICAL DECISIONS (one per round)
# =====================================================================
ROUNDS = [
    {
        "title": "Round 1: Trade or Farm? (Early 1600s)",
        "text": """
            It is the early 1600s. You and several hundred English men and
            women have just finished building your new colony, {colony}. But
            a colony is more than a few buildings and a wall. Many decisions
            still need to be made - decisions that will decide the fate of
            the people who live here, now and in the future.

            The most pressing issue concerns the people who live right on
            your doorstep. Fishermen, other colonies and local reports say
            the Native Americans here call themselves the Powhatan. They are
            a large confederation of smaller tribes led by a single chief.

            If you TRADE with the Powhatan, {colony} won't grow much beyond
            its walls. Trade doesn't require much land or many people. If you
            make FARMING the heart of your economy, {colony} will grow bigger,
            richer and more crowded. But you'll also have conflict with the
            Powhatan, who won't sit quietly as you push into their land.

            Which will you choose, {first}? Will {colony} be known for trade
            and cooperation with the Native Americans? Or will it grow into
            an economic powerhouse on the coast of this new world?
        """,
        "choices": {
            "TRADE": {
                "label": "Trade with the Powhatan",
                "effects": {"economy": 30, "population": -20, "natives": 30},
                "message": "You chose trade and cooperation with the Powhatan.",
            },
            "FARM": {
                "label": "Make farming the heart of the economy",
                "effects": {"food": 30, "economy": 30, "population": 30, "natives": -20},
                "message": "You chose farming. {colony} is spreading into Powhatan land.",
            },
        },
    },
    {
        "title": "Round 2: Roger Williams and Religious Freedom (1636)",
        "text": """
            It is 1636. News has reached {colony} about a minister named
            Roger Williams. Williams argues that church and government should
            be completely separate, and that each person should be free to
            worship God as they choose. He also says colonists should pay
            Native Americans for their land instead of just taking it. For
            these ideas, Massachusetts banished him. Williams has started a
            new settlement he calls Providence.

            His ideas are spreading in {colony}. Some colonists want to follow
            his example: let people of any religion settle here and worship
            freely, and pay Native Americans fairly for land.

            Other colonists argue that Christianity is essential to good
            government. If we want to stay close to England, they say, the
            Anglican Church must remain the official church of {colony}. They
            also don't want to pay for Native land, since it would cost a
            fortune.

            What do you think, {first}? Should {colony} embrace religious
            FREEDOM and treat Native Americans more fairly? Or should things
            stay the SAME?
        """,
        "choices": {
            "FREEDOM": {
                "label": "Religious freedom and fair treatment of Native Americans",
                "effects": {"economy": -10, "population": -10, "natives": 20, "britain": -20},
                "message": "You chose religious freedom and fairer treatment of Native Americans.",
            },
            "SAME": {
                "label": "Keep the Anglican Church and current land policy",
                "effects": {"economy": 5, "population": 5, "natives": -15, "britain": 10},
                "message": "You chose to keep things the same.",
            },
        },
    },
    {
        "title": "Round 3: The Navigation Acts (1660s)",
        "text": """
            Parliament has passed the Navigation Acts of 1660 and 1663. These
            laws limit colonial trade with other European countries. Certain
            colonial products can only be shipped to England. Colonial goods
            can only travel on English ships. And European products headed to
            the colonies must pass through England first, where they are
            taxed.

            The goal is easy to see: England wants to make as much money as
            possible from its colonies - at our expense.

            That doesn't sit well with many people in {colony}. Some quietly
            suggest SMUGGLING to avoid the taxes and get better prices. Others
            say that even though we live far from England, we are still loyal
            English subjects, and we should OBEY the laws of Parliament.

            What do you think, {first}? Should {colony} obey the Navigation
            Acts even though they hurt us, or should we smuggle?
        """,
        "choices": {
            "SMUGGLE": {
                "label": "Smuggle goods in and out of the colony",
                "effects": {"economy": 20, "population": 10, "britain": -20},
                "message": "You chose to smuggle goods in defiance of Parliament.",
            },
            "OBEY": {
                "label": "Obey the Navigation Acts",
                "effects": {"economy": 5, "population": 5, "natives": -5, "britain": 20},
                "message": "You chose to obey Parliament's laws.",
            },
        },
    },
    {
        "title": "Round 4: The French and Indian War (1754)",
        "text": """
            War has come to the colonies! A young Virginia militia officer
            named George Washington has helped spark a war between Great
            Britain and France, along with France's Native American allies.

            Parliament is calling on the colonies to contribute men and money
            to the war effort. Answering the call will cost you, {first} -
            in men, in money, and in your relationship with local Native
            Americans. But it will strengthen your relationship with the
            British government, and could bring prosperity if Britain wins.

            Will {colony} go to WAR for King and Country? Or will {colony}
            stay UNINTERESTED and sit this one out?
        """,
        "choices": {
            "WAR": {
                "label": "Support the war with men and money",
                "effects": {"economy": -5, "population": -5, "natives": -15, "britain": 25},
                "message": "You lent your enthusiastic support to the war.",
            },
            "UNINTERESTED": {
                "label": "Sit this one out",
                "effects": {"economy": 5, "population": 5, "natives": 10, "britain": -20},
                "message": "You offered little more than casual support for the war.",
            },
        },
    },
    {
        "title": "Round 5: The Stamp Act (1765)",
        "text": """
            Welcome back to {colony}, {first}. The year is 1765. Britain is
            deep in debt after the war with France. To pay for its army in
            America, Parliament has passed the Stamp Act.

            This law taxes every piece of printed paper colonists use. Legal
            documents, licenses, newspapers, and even playing cards must now
            carry an official stamp.

            The people of {colony} are furious. They cry, "No taxation
            without representation!" A group called the Sons of Liberty is
            urging you to BOYCOTT British goods. Others say you should PAY
            the tax to keep the peace.
        """,
        "choices": {
            "PAY": {
                "label": "Pay the tax to keep the peace",
                "effects": {"economy": -10, "population": -10, "britain": 20},
                "message": "You obeyed the law and paid the tax. The King is pleased with {colony}'s loyalty, but your citizens feel betrayed.",
            },
            "BOYCOTT": {
                "label": "Boycott British goods",
                "effects": {"economy": 5, "population": 10, "britain": -20},
                "message": "You organized a boycott of British goods. British merchants are hurting and the King is furious, but your people are united.",
            },
        },
    },
    {
        "title": "Round 6: The Tea Crisis (1773)",
        "text": """
            It is 1773, and the mood in {colony} is tense. Britain has
            repealed most of its taxes, but it kept the tax on tea to prove
            that Parliament still has the right to tax the colonies.

            Three British ships loaded with tea have just anchored in the
            harbor. The governor demands that the tea be unloaded and the tax
            paid. Local patriots are gathering at the docks, disguised as
            Mohawks, ready to raid the ships.

            If you DESTROY the tea, there will be no turning back. It could
            mean war. Or you could ALLOW the tea to be unloaded and sold.
        """,
        "choices": {
            "ALLOW": {
                "label": "Allow the tea to be unloaded and sold",
                "effects": {"economy": 10, "population": -20, "britain": 30},
                "message": "You allowed the tea to be unloaded. Business is booming and the British are relieved, but the patriots will never trust you again.",
            },
            "DESTROY": {
                "label": "Destroy the tea in the harbor",
                "effects": {"economy": -10, "population": 20, "britain": -30},
                "message": "SPLASH! The harbor of {colony} is brown with tea. The British are sending warships. The Revolution has begun!",
            },
        },
    },
]

# =====================================================================
# RANDOM EVENTS
# "first_round" = earliest round the event can happen (keeps history in order)
# "protected_by" = the investment that softens the event
# =====================================================================
RANDOM_EVENTS = [
    {
        "name": "Drought",
        "first_round": 1,
        "text": "This was an unusually bad year for crops. Many people in {colony} have little to eat.",
        "effects": {"food": -20, "economy": -15, "population": -10},
        "protected_by": "Infrastructure (roads, bridges, ports)",
        "protected_text": "This was an unusually bad year for crops. But because you invested in infrastructure, {colony} could bring in food to make up for most of the losses.",
        "protected_effects": {"food": -5, "economy": -5, "population": -5},
    },
    {
        "name": "Native War",
        "first_round": 1,
        "text": "War has broken out between {colony} and nearby Native Americans! The fighting costs the colony dearly.",
        "effects": {"food": -10, "economy": -10, "population": -10, "natives": -20},
        "protected_by": "Forts/Militia",
        "protected_text": "War has broken out between {colony} and nearby Native Americans! Because you invested in forts and a militia, the damage was limited.",
        "protected_effects": {"food": -5, "economy": -5, "population": -5, "natives": -15},
    },
    {
        "name": "Hurricane",
        "first_round": 1,
        "text": "A hurricane has hit {colony}, leaving a wide trail of destruction.",
        "effects": {"food": -15, "economy": -20, "population": -10},
        "protected_by": "Infrastructure (roads, bridges, ports)",
        "protected_text": "A hurricane has hit {colony}, leaving a wide trail of destruction. Thanks to your infrastructure, the damage is easier to repair.",
        "protected_effects": {"food": -10, "economy": -10, "population": -5},
    },
    {
        "name": "Smallpox",
        "first_round": 1,
        "text": "Smallpox is spreading through {colony}. Many of the colony's young and old die.",
        "effects": {"food": -5, "economy": -10, "population": -20},
        "protected_by": "Medical Care",
        "protected_text": "Smallpox is spreading through {colony}. Because you invested in medical care, more colonists survive.",
        "protected_effects": {"food": -5, "economy": -5, "population": -10},
    },
    {
        "name": "Peace with Natives",
        "first_round": 1,
        "text": "After weeks of talks, a nearby Native American nation has agreed to live in peace with {colony}.",
        "effects": {"economy": 10, "population": 10, "natives": 20},
    },
    {
        "name": "Plentiful Harvest",
        "first_round": 1,
        "text": "{colony} was blessed with a good crop this year. This winter will be easier than most.",
        "effects": {"food": 20, "economy": 10, "population": 10},
    },
    {
        "name": "Pirate Attack",
        "first_round": 1,
        "text": "Spanish pirates attacked {colony}! They burned and looted their way through the colony.",
        "effects": {"food": -10, "economy": -10, "population": -15},
        "protected_by": "Forts/Militia",
        "protected_text": "Spanish pirates attacked {colony}! Your forts and militia kept the damage small.",
        "protected_effects": {"food": -5, "economy": -5, "population": -5},
    },
    {
        "name": "Royal Favor",
        "first_round": 2,
        "text": "The King's officials report that {colony} is a valuable, well-run colony. London sends praise - and new settlers.",
        "effects": {"economy": 10, "population": 5, "britain": 15},
    },
    {
        "name": "Caught Smuggling",
        "first_round": 3,   # only after the Navigation Acts
        "text": "Someone from {colony} was caught smuggling by the Royal Navy! The Navy promises to watch {colony} more closely. The King is not pleased.",
        "effects": {"economy": -10, "britain": -15},
        "protected_by": "Representative to Britain",
        "protected_text": "Someone from {colony} was caught smuggling by the Royal Navy! Luckily, your representative in London kept {colony} out of serious trouble.",
        "protected_effects": {"economy": -5, "britain": -5},
    },
    {
        "name": "Great Awakening",
        "first_round": 4,   # the Great Awakening was in the 1730s-1740s
        "text": "The Great Awakening has come to {colony}! Religious revival is drawing new families to the colony.",
        "effects": {"economy": 10, "population": 20},
        "protected_by": "Schools",
        "protected_text": "The Great Awakening has come to {colony}! Because you invested in schools, even more families want to settle here.",
        "protected_effects": {"economy": 15, "population": 30},
    },
]

# =====================================================================
# DISPLAY HELPERS
# =====================================================================
LINE = "_" * WIDTH


def wrap(text):
    """Wrap text to WIDTH. Blank lines separate paragraphs."""
    text = textwrap.dedent(text).strip("\n")
    paragraphs = text.split("\n\n")
    return "\n\n".join(textwrap.fill(" ".join(p.split()), WIDTH) for p in paragraphs)


def print_slow(text, speed=TYPE_SPEED):
    """Type text onto the screen one letter at a time."""
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def say(text, **names):
    """Fill in names like {colony}, wrap the text, and type it out."""
    print_slow(wrap(text.format(**names)))


def pause():
    input("\n[Press Enter to continue] ")


def show_effects(effects):
    """Print each change, like 'Food: +30'."""
    for key, label in CATEGORIES.items():
        if key in effects:
            print(f"   {label}: {effects[key]:+d}")


def apply_effects(scores, effects):
    for key, amount in effects.items():
        scores[key] += amount


def show_scores(scores):
    print("\n" + LINE)
    print("\nYOUR COLONY'S SCORES:\n")
    for key, label in CATEGORIES.items():
        value = scores[key]
        bar = "#" * max(0, min(value, 150) // 5)
        warning = "   <-- DANGER!" if value <= 15 else ""
        print(f"   {label:<18} {value:>4}  {bar}{warning}")
    print(LINE)


def failed_category(scores):
    """Return the first category at 0 or below, or None if all are safe."""
    for key in CATEGORIES:
        if scores[key] <= 0:
            return key
    return None


GAME_OVER_MESSAGES = {
    "food": "{colony} ran out of food!",
    "economy": "The economy of {colony} has collapsed!",
    "population": "The entire population of {colony} has died or left!",
    "natives": "War has broken out between {colony} and the Native Americans!",
    "britain": "Britain has revoked the charter of {colony}!",
}

# =====================================================================
# STUDENT INFORMATION
# =====================================================================
def ask_text(prompt):
    answer = ""
    while answer == "":
        answer = input(prompt).strip()
    return answer


def choose_from_list(prompt, options):
    """Show a numbered list and return the option the student picks."""
    for number, option in enumerate(options, 1):
        print(f"   {number}) {option}")
    while True:
        answer = input(prompt).strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print(f"   Please type a number from 1 to {len(options)}.")


def get_student_info():
    print_slow("Before we begin the simulation, please provide the following information.\n")
    first = ask_text("Please enter your first name: ").title()
    last = ask_text("Please enter your last name: ").title()

    period = ""
    while period not in CLASS_PERIODS:
        period = input("Enter your class period as a number (for example, 1): ").strip()
        if period not in CLASS_PERIODS:
            print("   Please type just the number of your class period, like 3.")

    print("\nWho is your history teacher?")
    teacher = choose_from_list("Type the number next to your teacher's name: ", TEACHERS)
    colony = ask_text("\nWhat would you like to name your colony? ")
    return first, f"{first} {last}", period, teacher, colony

# =====================================================================
# THE THREE PARTS OF EACH ROUND
# =====================================================================
def invest(scores, investments, names):
    print("\n" + "=" * WIDTH)
    print_slow("INVESTMENTS")
    print("=" * WIDTH)
    say("An important part of running a colony is investing in the future. "
        "Each investment can only be bought once, and it lasts for the rest of the game.", **names)
    print()

    available = []
    for number, item in INVESTMENTS.items():
        if item["name"] in investments:
            continue
        available.append(number)
        cost = ", ".join(f"{CATEGORIES[k]} {v:+d}" for k, v in item["cost"].items())
        print(f"   {number}) {item['name']}")
        print(f"        Cost: {cost}")
        print(f"        {item['protects']}")
    print("   0) Don't invest this round")

    if not available:
        print_slow("\nYou've already bought every investment!")
        return

    while True:
        answer = input("\nType the number of your choice: ").strip()
        if answer == "0":
            print_slow("You chose not to invest this round.")
            break
        if answer in available:
            item = INVESTMENTS[answer]
            print()
            say(item["message"], **names)
            show_effects(item["cost"])
            apply_effects(scores, item["cost"])
            investments.append(item["name"])
            break
        print("   Please type one of the numbers shown above.")

    if investments:
        print("\nYour investments so far: " + ", ".join(investments))


def historical_decision(round_info, scores, names):
    print("\n" + "=" * WIDTH)
    print_slow(round_info["title"])
    print("=" * WIDTH + "\n")
    say(round_info["text"], **names)

    choices = round_info["choices"]
    print("\nYOUR OPTIONS:")
    for word, choice in choices.items():
        print(f"   {word:<13} {choice['label']}")

    words = list(choices)
    prompt = f"\nWhat is your decision? Type {' or '.join(words)}: "
    while True:
        answer = input(prompt).strip().upper()
        if answer in choices:
            break
        print(f"   Please type {' or '.join(words)}.")

    choice = choices[answer]
    print()
    say(choice["message"], **names)
    print(f"\nHere's how it affected {names['colony']}:")
    show_effects(choice["effects"])
    apply_effects(scores, choice["effects"])
    return answer


def random_event(round_number, scores, investments, names):
    print("\n" + "=" * WIDTH)
    print_slow("RANDOM EVENT")
    print("=" * WIDTH)
    print_slow("Sometimes things happen that you just weren't expecting...")

    possible = [e for e in RANDOM_EVENTS if e["first_round"] <= round_number]
    event = random.choice(possible)
    time.sleep(0.5)
    print_slow(f"\n*** {event['name'].upper()} ***\n", 0.05)

    if event.get("protected_by") in investments:
        say(event["protected_text"], **names)
        effects = event["protected_effects"]
    else:
        say(event["text"], **names)
        effects = event["effects"]
    print()
    show_effects(effects)
    apply_effects(scores, effects)
    return event["name"]

def production(economy_type, scores, names):
    print("\n" + "=" * WIDTH)
    print_slow("THE YEARS PASS...")
    print("=" * WIDTH)
    if economy_type == "FARM":
        say("Colonists clear new fields and bring in the harvest. Families "
            "arrive from England, hoping for land of their own.", **names)
    else:
        say("Traders bring furs and goods into {colony}, and the colony grows "
            "a little food of its own. A few new families arrive from England.", **names)
    effects = PRODUCTION[economy_type]
    print()
    show_effects(effects)
    apply_effects(scores, effects)


# =====================================================================
# FINAL REPORT
# =====================================================================
def build_report(full_name, period, teacher, colony, rounds_survived, survived,
                 scores, decisions, investments):
    lines = [
        "THE COLONY SIMULATION - SUMMARY REPORT",
        f"Student: {full_name}",
        f"Teacher: {teacher}    Period: {period}",
        f"Colony: {colony}",
        f"Completed: {time.strftime('%B %d, %Y at %I:%M %p')}",
        "",
        f"Result: {'SURVIVED all 6 rounds!' if survived else f'Colony failed in round {rounds_survived + 1}'}",
        f"Rounds survived: {rounds_survived} of {len(ROUNDS)}",
    ]
    if survived:
        lines.append(f"Final colony score: {sum(scores.values())}")
    lines += ["", "DECISIONS"]
    for number, (round_info, answer, event) in enumerate(decisions, 1):
        label = round_info["choices"][answer]["label"] if answer else "(not reached)"
        lines.append(textwrap.fill(f"{number}. {round_info['title'].split(': ', 1)[1]}: {label}",
                                   WIDTH, subsequent_indent="   "))
        if event:
            lines.append(f"   Random event: {event}")
    lines += [
        "",
        "Investments: " + (", ".join(investments) if investments else "None"),
        "",
        "FINAL SCORES",
    ]
    for key, label in CATEGORIES.items():
        lines.append(f"   {label}: {scores[key]}")
    return "\n".join(lines)


def show_report(report):
    print("\n" + "=" * WIDTH)
    print("YOUR SUMMARY REPORT".center(WIDTH))
    print("Copy everything below and paste it into Canvas".center(WIDTH))
    print("=" * WIDTH)
    print(report)
    print("=" * WIDTH)
    # In the web version, also put the report in a box with a Copy button
    if sys.platform == "emscripten":
        try:
            from pyscript import document
            document.getElementById("report-text").value = report
            document.getElementById("report").hidden = False
            print("\nYour report is also in a box BELOW this game window.")
            print("Scroll down, click 'Copy report', then paste it into Canvas.")
        except Exception:
            pass

# =====================================================================
# MAIN GAME
# =====================================================================
def main():
    print_slow("=" * WIDTH, 0.002)
    print_slow("THE COLONY SIMULATION".center(WIDTH))
    print_slow("=" * WIDTH + "\n", 0.002)

    first, full_name, period, teacher, colony = get_student_info()
    names = {"first": first, "colony": colony}

    print()
    say("""
        Welcome to the Colony Simulation, {first}!

        You are in charge of a new British colony in North America. You will
        make all of the major decisions for {colony}, from its founding until
        the eve of the American Revolution.

        You must keep five categories in balance: Food, Economy, Population,
        Native Relations and British Relations. Each one starts at 50 points.
        If ANY category drops to 0 or below, {colony} will fail.

        Each round, three things happen. First, you may invest in your
        colony - at a price. Second, you make a decision based on real
        history. Third, {colony} faces a random event.

        Good luck!
    """, **names)

    scores = {key: STARTING_POINTS for key in CATEGORIES}
    investments = []
    decisions = []
    show_scores(scores)
    pause()

    survived = True
    rounds_survived = 0
    economy_type = "TRADE"
    for round_number, round_info in enumerate(ROUNDS, 1):
        answer = None
        event = None

        invest(scores, investments, names)
        if failed_category(scores) is None:
            pause()
            answer = historical_decision(round_info, scores, names)
            show_scores(scores)
        if failed_category(scores) is None:
            pause()
            event = random_event(round_number, scores, investments, names)
            show_scores(scores)

        if round_number == 1 and answer:
            economy_type = answer
        if failed_category(scores) is None and round_number < len(ROUNDS):
            pause()
            production(economy_type, scores, names)
            show_scores(scores)

        decisions.append((round_info, answer, event))
        failed = failed_category(scores)
        if failed:
            survived = False
            print()
            print_slow(f"--- GAME OVER, {first}: "
                       + GAME_OVER_MESSAGES[failed].format(**names) + " ---", 0.04)
            break

        rounds_survived = round_number
        if round_number < len(ROUNDS):
            print()
            print_slow(f"Great job, {first}! {colony} survived round {round_number}.")
            pause()

    # Rounds the student never reached still appear in the report
    for round_info in ROUNDS[len(decisions):]:
        decisions.append((round_info, None, None))

    if survived:
        print()
        say("""
            CONGRATULATIONS, {first}!

            You guided {colony} through more than 150 years of history. You
            navigated relations with Native Americans, survived British
            taxes, and built a thriving community.

            You are a true founder!
        """, **names)

        print(f"\nFinal colony score: {sum(scores.values())} "
              "(all five categories added together)")
    pause()
    report = build_report(full_name, period, teacher, colony, rounds_survived,
                          survived, scores, decisions, investments)
    show_report(report)
    print("\nThanks for playing the Colony Simulation!\n")


if __name__ == "__main__":
    main()
