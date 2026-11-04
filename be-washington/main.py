#!/usr/bin/env python3
"""
BE WASHINGTON: The Beginnings of the French and Indian War
==========================================================
An interactive decision-making simulation for 8th grade U.S. History.

Students step into George Washington's boots in 1753-1754 and make six
decisions leading up to the French and Indian War. After each choice, they
see a likely outcome of THEIR decision, then learn what Washington ACTUALLY
did and why it mattered.

At the end, students see how often they matched Washington, get a
"leadership style" profile, and receive a
summary report they can copy into Canvas. Where the computer allows it,
the report is also saved as a .txt file. In the web version, nothing is
saved -- the report appears in a box with a "Copy report" button.

Runs on any standard Python 3 install (IDLE, Thonny, VS Code, Replit,
Trinket, etc.). No extra packages are needed.

HOW TO EDIT
-----------
All of the story content lives in these variables below:
    INTRO_SECTIONS, DECISIONS, EPILOGUE, PROFILES
Each decision is a dictionary. Each option has:
    "text"       -> what the student sees as the choice
    "short"      -> a short label used in the final report
    "style"      -> "bold", "cautious", or "diplomatic" (for the profile)
    "historical" -> True for the choice Washington actually made
    "outcome"    -> what happens if the student picks it
Blank lines inside text separate paragraphs. Lines starting with "- "
are shown as bullet points.
"""

import os
import sys
import textwrap
import time

# =========================================================================
# TEACHER SETTINGS
# =========================================================================
TYPEWRITER = True      # True = text "types" onto the screen. False = instant.
TYPE_SPEED = 0.015     # Seconds per character (smaller = faster).
WIDTH = 76             # Characters per line.
SAVE_REPORT = True     # Try to save a .txt report at the end.
CONFIRM_CHOICES = True # Ask "Lock in this decision?" after each choice.


# =========================================================================
# STORY CONTENT: INTRODUCTION
# =========================================================================
INTRO_SECTIONS = [
    ("The Prize: The Ohio River Valley", """
        West of the Appalachian Mountains lies the Ohio River Valley: thick
        forests, rich soil, and rivers that work like highways into the heart
        of North America. The most important spot is the Forks of the Ohio,
        where two rivers meet to form the Ohio River. (Today, Pittsburgh sits
        right there.)
    """),

    ("Who Wants It?", """
        - THE FRENCH need it to connect their colonies in Canada with Louisiana. Without it, New France is cut in two.
        - THE BRITISH, especially Virginia, want it for new farmland. Rich Virginians -- including Governor Dinwiddie and Washington's own brothers -- have invested in land there.
        - NATIVE NATIONS -- the Shawnee, Delaware, and Mingo -- already live there. To them, both empires are outsiders.
    """),

    ("You Are George Washington", """
        It's 1754. The French are building forts in the Ohio Valley, and they
        ignored Virginia's warning to leave. Governor Dinwiddie sends you, a
        22-year-old lieutenant colonel, with about 160 soldiers to protect a
        new Virginia fort at the Forks.

        You've never fought in a battle. The decisions are now yours.
    """),
]


# =========================================================================
# STORY CONTENT: THE DECISIONS
# =========================================================================
DECISIONS = [
    # ---------------------------------------------------------------- 1
    {
        "title": "The Fort Has Fallen",
        "when": "April 1754",
        "where": "Wills Creek, the edge of the Virginia frontier",
        "setup": """
            You've reached the edge of the frontier with 160 untrained men.
            Many of them don't even have shoes.

            Then bad news arrives: about 500 French soldiers with cannons have
            captured the Virginia fort at the Forks. Now they're building their
            own fort there: Fort Duquesne.

            The fort you came to protect is gone. You're outnumbered more than
            three to one.
        """,
        "question": "What do you do, Colonel Washington?",
        "options": [
            {
                "text": "Write the French a letter demanding they leave, and wait "
                        "for an answer.",
                "short": "Demand by letter that the French leave",
                "style": "diplomatic",
                "historical": False,
                "outcome": """
                    You already tried that last winter, and the French said no.
                    Now they have 500 soldiers and a new fort. Weeks pass, and
                    nothing changes.
                """,
            },
            {
                "text": "Push forward. Cut a road toward the Forks and wait for "
                        "reinforcements closer to the action.",
                "short": "Push forward into the Ohio Country",
                "style": "bold",
                "historical": True,
                "outcome": """
                    Your men start chopping a road through the mountains. It's
                    brutal work, but it shows everyone that Virginia isn't
                    giving up.
                """,
            },
            {
                "text": "March back to Virginia. The mission is impossible now.",
                "short": "Retreat to Virginia",
                "style": "cautious",
                "historical": False,
                "outcome": """
                    Your men are safe, but Governor Dinwiddie is furious. The
                    French now control the Forks without a fight.
                """,
            },
        ],
        "history": """
            Washington pushed forward, cutting a road deeper into territory the
            French now controlled. It was bold -- maybe reckless -- for an
            officer with no battle experience.
        """,
        "think": "Was pushing forward brave or reckless?",
    },

    # ---------------------------------------------------------------- 2
    {
        "title": "Friends in the Forest?",
        "when": "May 1754",
        "where": "The Ohio Country",
        "setup": """
            Your men are farmers, not woodsmen, and this forest is unfamiliar.
            The French have Native allies who know every trail.

            Tanacharison, a Seneca leader called the "Half King," hates the
            French and offers to help. He knows the land -- but he expects
            respect, gifts, and a voice in your decisions.
        """,
        "question": "How do you respond to Tanacharison?",
        "options": [
            {
                "text": "Keep your distance. Take his information, but make no "
                        "promises.",
                "short": "Keep Tanacharison at a distance",
                "style": "cautious",
                "historical": False,
                "outcome": """
                    You get some information, but Tanacharison can tell you
                    don't trust him. Half-friendship earns only half-help.
                """,
            },
            {
                "text": "Go it alone. You want full control of your mission.",
                "short": "Go it alone",
                "style": "bold",
                "historical": False,
                "outcome": """
                    Without guides, you're blind in the forest. The French know
                    where you are long before you know where they are.
                """,
            },
            {
                "text": "Make him an ally. Send gifts and invite his warriors to "
                        "scout for you.",
                "short": "Ally with Tanacharison",
                "style": "diplomatic",
                "historical": True,
                "outcome": """
                    Tanacharison's scouts become your eyes and ears. Soon they
                    bring news that changes everything.
                """,
            },
        ],
        "history": """
            Washington made Tanacharison an ally. But Washington gave orders
            instead of listening, and he couldn't provide the gifts his allies
            expected. Before the biggest battle of the campaign, Tanacharison
            and his warriors left.
        """,
        "think": "What did Native nations want out of this conflict?",
    },

    # ---------------------------------------------------------------- 3
    {
        "title": "Jumonville Glen",
        "when": "May 28, 1754",
        "where": "A rocky ravine in the forest",
        "setup": """
            Tanacharison's scouts find about 35 French soldiers hiding in a
            rocky ravine. Why are they hiding? Are they spies? Messengers?

            You march 40 men all night through pouring rain. At dawn, you and
            Tanacharison's warriors surround the ravine. Below you, the French
            are just waking up. They haven't seen you.
        """,
        "question": "What are your orders?",
        "options": [
            {
                "text": "Step out, announce yourself, and demand to know what "
                        "they're doing.",
                "short": "Make contact and demand answers",
                "style": "diplomatic",
                "historical": False,
                "outcome": """
                    Their officer, Ensign Jumonville, says he's a messenger
                    with a letter ordering the British to leave. No one dies --
                    but now the French know exactly how small your force is.
                """,
            },
            {
                "text": "Attack now, while you have the element of surprise.",
                "short": "Attack by surprise",
                "style": "bold",
                "historical": True,
                "outcome": """
                    Musket fire crashes into the ravine. In about fifteen
                    minutes, it's over.
                """,
            },
            {
                "text": "Pull back quietly and keep watching.",
                "short": "Pull back and watch",
                "style": "cautious",
                "historical": False,
                "outcome": """
                    Hiding 50 men isn't easy. The French spot you, or slip away
                    to report your position. Your surprise is gone.
                """,
            },
        ],
        "history": """
            In a 15-minute fight, about 10 French soldiers were killed,
            including their commander, Ensign Jumonville. Twenty-one were
            captured.

            Who fired first is still debated. Washington said the French went
            for their weapons. The French said Jumonville was a peaceful
            diplomat, and they called it murder. Either way, the French would
            want revenge.
        """,
        "think": "Was Jumonville a spy or a diplomat? Does it matter who fired first?",
    },

    # ---------------------------------------------------------------- 4
    {
        "title": "Stand or Retreat?",
        "when": "June 1754",
        "where": "The Great Meadows",
        "setup": """
            The French at Fort Duquesne will want revenge, and they badly
            outnumber you. Your commanding officer has died in an accident, so
            now you're in charge of the whole expedition. More troops are on
            the way.
        """,
        "question": "What now, Colonel?",
        "options": [
            {
                "text": "Retreat to Virginia before the French strike back.",
                "short": "Retreat to Virginia",
                "style": "cautious",
                "historical": False,
                "outcome": """
                    You make it home safely, but it looks like you attacked and
                    then ran away. Virginia's claim to the Ohio Valley
                    collapses.
                """,
            },
            {
                "text": "Write to the French explaining your side, hoping to "
                        "avoid a war.",
                "short": "Explain yourself to the French",
                "style": "diplomatic",
                "historical": False,
                "outcome": """
                    The French read your letter as a confession. Nothing you
                    write will change their minds, and their army is already
                    marching.
                """,
            },
            {
                "text": "Stand your ground. Build a fort and wait for "
                        "reinforcements.",
                "short": "Build a fort and stand your ground",
                "style": "bold",
                "historical": True,
                "outcome": """
                    Your men build a small fort in an open meadow. You name it
                    Fort Necessity.
                """,
            },
        ],
        "history": """
            Washington stood his ground and built Fort Necessity. One problem:
            it sat in a low, swampy meadow, with wooded hills close enough for
            enemies to shoot into the fort from cover.
        """,
        "think": "What problems can you spot with Fort Necessity's location?",
    },

    # ---------------------------------------------------------------- 5
    {
        "title": "The Battle of Fort Necessity",
        "when": "July 3, 1754",
        "where": "Fort Necessity",
        "setup": """
            About 700 French soldiers and Native warriors arrive. Their
            commander is Jumonville's older brother, and he wants revenge.

            They fire down from the trees. Then heavy rain floods your trenches
            and soaks your gunpowder. By evening, about 30 of your men are dead
            and 70 are wounded. Then the French call out: they want to talk.
        """,
        "question": "What do you decide?",
        "options": [
            {
                "text": "Break out in the dark and escape through the woods.",
                "short": "Break out at night",
                "style": "cautious",
                "historical": False,
                "outcome": """
                    You'd have to leave 70 wounded men behind, and the enemy
                    knows these woods far better than you. Few would make it
                    home.
                """,
            },
            {
                "text": "Negotiate. Hear what the French are offering.",
                "short": "Negotiate surrender terms",
                "style": "diplomatic",
                "historical": True,
                "outcome": """
                    Your officers return with the French terms. They're
                    surprisingly generous.
                """,
            },
            {
                "text": "Refuse. Fight to the last man!",
                "short": "Fight to the last man",
                "style": "bold",
                "historical": False,
                "outcome": """
                    With soaked gunpowder, more fighting means a massacre.
                    Washington would likely die at 22 -- and there would be no
                    President Washington.
                """,
            },
        ],
        "history": """
            Washington negotiated. His men could march home with their flags
            and muskets if they abandoned the fort. The French didn't want to
            start a full-scale war by wiping out a British force.

            There was just one catch: Washington had to sign the surrender
            papers.
        """,
        "think": "Was surrendering the right choice?",
    },

    # ---------------------------------------------------------------- 6
    {
        "title": "The Surrender Document",
        "when": "Near midnight, July 3, 1754",
        "where": "Fort Necessity",
        "setup": """
            The surrender terms are in French, and you can't read French. By
            candlelight in the rain, your translator reads them aloud in shaky
            English. One line mentions the "death" of Jumonville. Your
            translator seems unsure what it means.

            Your men are exhausted. The French are waiting.
        """,
        "question": "What do you do with the pen in your hand?",
        "options": [
            {
                "text": "Refuse to sign until every word is translated perfectly.",
                "short": "Demand a perfect translation",
                "style": "diplomatic",
                "historical": False,
                "outcome": """
                    The French commander is losing patience, and there's no
                    better translator for miles. Push too hard, and the
                    fighting could start again.
                """,
            },
            {
                "text": "Cross out the part about Jumonville, then sign.",
                "short": "Cross out the Jumonville part",
                "style": "bold",
                "historical": False,
                "outcome": """
                    The French commander refuses. His brother is dead, and he
                    blames you. Sign it as written, or keep fighting.
                """,
            },
            {
                "text": "Sign it. Your men need to get out of here.",
                "short": "Sign the document",
                "style": "cautious",
                "historical": True,
                "outcome": """
                    You sign your name. Tomorrow, your men march home.
                """,
            },
        ],
        "history": """
            Washington signed. But the French word didn't mean "death." It was
            "l'assassinat" -- ASSASSINATION. Washington seemed to confess, in
            writing, to murdering a French diplomat.

            The French spread the document across Europe as proof that Britain
            started the conflict. It was the only time Washington ever
            surrendered to an enemy.
        """,
        "think": "How did one word turn a small frontier fight into an "
                 "international crisis?",
    },
]


# =========================================================================
# STORY CONTENT: EPILOGUE
# =========================================================================
EPILOGUE = [
    ("What Happened Next", """
        The fighting in the Ohio Valley grew into a world war, called the
        Seven Years' War in Europe. Britain won in 1763 and took Canada and the
        land east of the Mississippi. Native nations lost France as an ally
        against British settlers.

        But winning cost a fortune, so Britain began taxing the colonies. It
        also banned settlement west of the Appalachians -- the very land
        Virginia had fought for. Colonists were furious. The road to the
        American Revolution had begun.

        About twenty years after surrendering to the French, George Washington
        would lead an army against the British. As one British writer put it,
        a shot fired by "a young Virginian in the backwoods of America set the
        world on fire."
    """),
]


# =========================================================================
# STORY CONTENT: RESULTS
# =========================================================================
PROFILES = {
    "bold": ("THE RISK-TAKER", """
        You charge ahead, even when the odds are against you. So did young
        Washington -- and it led him straight into a trap at Fort Necessity.
    """),
    "cautious": ("THE CAREFUL STRATEGIST", """
        You weigh the risks and protect your people. That's the kind of leader
        Washington BECAME during the Revolution, when he often retreated to
        fight another day.
    """),
    "diplomatic": ("THE DIPLOMAT", """
        You prefer talking to fighting. Young Washington struggled here -- he
        lost his Native allies partly because he didn't listen to them.
    """),
    "balanced": ("THE BALANCED LEADER", """
        You mix boldness, caution, and diplomacy depending on the situation.
        It took young Washington years of hard lessons to learn that balance.
    """),
}


# =========================================================================
# DISPLAY HELPERS
# =========================================================================
def format_block(text):
    """Wrap text: blank lines separate paragraphs; '- ' lines become bullets."""
    text = textwrap.dedent(text).strip()
    blocks = []
    for para in text.split("\n\n"):
        lines = [ln.strip() for ln in para.strip().splitlines() if ln.strip()]
        if not lines:
            continue
        if all(ln.startswith("- ") for ln in lines):
            bullets = [textwrap.fill(ln, WIDTH, subsequent_indent="  ") for ln in lines]
            blocks.append("\n".join(bullets))
        else:
            blocks.append(textwrap.fill(" ".join(lines), WIDTH))
    return "\n\n".join(blocks)


def type_out(text):
    """Print text, with an optional typewriter effect."""
    if TYPEWRITER:
        for ch in text:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(TYPE_SPEED)
        sys.stdout.write("\n")
        sys.stdout.flush()
    else:
        print(text)


def show(text):
    type_out(format_block(text))
    print()


def pause(msg="Press ENTER to continue"):
    input(f"   [{msg}] ")
    print()


def banner(*lines):
    print("\n" + "=" * WIDTH)
    for line in lines:
        print(line.center(WIDTH))
    print("=" * WIDTH + "\n")


def heading(text):
    print("\n" + "-" * WIDTH)
    print(" " + text.upper())
    print("-" * WIDTH + "\n")


def ask_choice(options):
    """Show numbered options and return the index the student picks."""
    for i, opt in enumerate(options, 1):
        print(textwrap.fill(opt["text"], WIDTH,
                            initial_indent=f"  {i}) ", subsequent_indent="     "))
        print()
    while True:
        ans = input(f"Type the number of your choice (1-{len(options)}): ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(options):
            idx = int(ans) - 1
            if not CONFIRM_CHOICES:
                return idx
            confirm = input(f'You chose: "{options[idx]["short"]}". '
                            f"Lock it in? (Y/n): ").strip().lower()
            if not confirm.startswith("n"):
                return idx
            print("\nOkay, think it over and choose again.\n")
        else:
            print(f"  Please type a number from 1 to {len(options)}.")


# =========================================================================
# GAME FLOW
# =========================================================================
def title_screen():
    banner("B E   W A S H I N G T O N",
           "",
           "The Beginnings of the French and Indian War",
           "1753 - 1754")
    show("""
        Make six real decisions young George Washington faced in 1754. After
        each one, find out what really happened. There are no right answers --
        you don't know how the story ends.
    """)


def get_student_name():
    while True:
        name = input("Before we begin, type your first and last name: ").strip()
        if name:
            print()
            return name
        print("  Please enter your name.")


def play_intro():
    for i, (title, text) in enumerate(INTRO_SECTIONS):
        heading(title)
        show(text)
        if i < len(INTRO_SECTIONS) - 1:
            pause()
    pause("Press ENTER to begin your first decision")


def play_decision(number, total, d):
    banner(f"DECISION {number} OF {total}", d["title"].upper())
    print(f"  WHEN:  {d['when']}")
    print(f"  WHERE: {d['where']}\n")
    show(d["setup"])
    print(d["question"].upper() + "\n")

    idx = ask_choice(d["options"])
    chosen = d["options"][idx]
    actual = next(o for o in d["options"] if o["historical"])

    heading("Your Decision: " + chosen["short"])
    show(chosen["outcome"])
    pause("Press ENTER to see what Washington actually did")

    heading("What Really Happened")
    if chosen["historical"]:
        type_out(">> You made the same choice as Washington! <<\n")
    else:
        type_out(f'>> Washington chose differently: "{actual["short"]}" <<\n')
    show(d["history"])

    heading("Think About It")
    show(d["think"])
    pause()

    return {
        "title": d["title"],
        "student": chosen["short"],
        "washington": actual["short"],
        "matched": chosen["historical"],
        "style": chosen["style"],
    }


def play_epilogue():
    banner("EPILOGUE", "What Happened Next")
    for title, text in EPILOGUE:
        heading(title)
        show(text)
        pause()


def leadership_profile(records):
    counts = {"bold": 0, "cautious": 0, "diplomatic": 0}
    for r in records:
        counts[r["style"]] += 1
    top = max(counts.values())
    leaders = [s for s, c in counts.items() if c == top]
    key = leaders[0] if len(leaders) == 1 else "balanced"
    return key, counts


def washington_style_counts():
    counts = {"bold": 0, "cautious": 0, "diplomatic": 0}
    for d in DECISIONS:
        for o in d["options"]:
            if o["historical"]:
                counts[o["style"]] += 1
    return counts


def match_comment(matches, total):
    if matches == total:
        return "You think EXACTLY like young Washington! (Is that a good thing?)"
    if matches >= total - 2:
        return "You think a lot like young Washington."
    if matches >= total // 3:
        return "You and Washington saw things differently at key moments."
    return ("You would have taken a very different path. Would history have "
            "turned out better... or worse?")


def show_results(name, records):
    total = len(records)
    matches = sum(r["matched"] for r in records)
    key, counts = leadership_profile(records)
    gw = washington_style_counts()
    profile_title, profile_text = PROFILES[key]

    banner("YOUR RESULTS", name)
    for i, r in enumerate(records, 1):
        mark = "MATCH" if r["matched"] else "DIFFERENT"
        print(f"  {i}. {r['title']}  [{mark}]")
        print(f"       You:        {r['student']}")
        print(f"       Washington: {r['washington']}\n")

    print(f"  You matched Washington on {matches} of {total} decisions.")
    print("  " + match_comment(matches, total) + "\n")

    heading("Your Leadership Style: " + profile_title)
    print(f"  Your choices:        {counts['bold']} bold, {counts['cautious']} "
          f"cautious, {counts['diplomatic']} diplomatic")
    print(f"  Young Washington's:  {gw['bold']} bold, {gw['cautious']} "
          f"cautious, {gw['diplomatic']} diplomatic\n")
    show(profile_text)
    pause("Press ENTER for your summary report")
    return matches, total, key, counts


def build_report(name, records, matches, total, key, counts):
    lines = [
        "BE WASHINGTON: The Beginnings of the French and Indian War",
        f"Student: {name}",
        f"Completed: {time.strftime('%B %d, %Y at %I:%M %p')}",
        "",
        "DECISIONS",
    ]
    for i, r in enumerate(records, 1):
        mark = "MATCH" if r["matched"] else "DIFFERENT"
        lines.append(f"{i}. {r['title']} [{mark}]")
        lines.append(f"   Me: {r['student']}")
        lines.append(f"   Washington: {r['washington']}")
    lines += [
        "",
        f"Matched Washington: {matches} of {total}",
        f"Leadership style: {PROFILES[key][0]} "
        f"({counts['bold']} bold, {counts['cautious']} cautious, "
        f"{counts['diplomatic']} diplomatic)",
    ]
    return "\n".join(lines)


def save_report(name, report):
    safe = "".join(c for c in name if c.isalnum() or c in " -_").strip()
    filename = f"Be_Washington_{safe.replace(' ', '_') or 'student'}.txt"
    if sys.platform == "emscripten":
        # Web version: don't save or download anything. Instead, put the
        # report in a box below the game with a "Copy report" button.
        try:
            from pyscript import document
            document.getElementById("report-text").value = report
            document.getElementById("report").hidden = False
            print("  Your report is also in a box BELOW this game window.")
            print("  Scroll down, click 'Copy report', then paste it into Canvas.")
        except Exception:
            pass
        return
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"  Your report was saved as: {os.path.abspath(filename)}")
    except OSError:
        print("  (This computer would not let the report be saved as a file.)")


def main():
    title_screen()
    name = get_student_name()
    play_intro()

    records = []
    for n, d in enumerate(DECISIONS, 1):
        records.append(play_decision(n, len(DECISIONS), d))

    play_epilogue()
    matches, total, key, counts = show_results(name, records)
    report = build_report(name, records, matches, total, key, counts)

    banner("YOUR SUMMARY REPORT",
           "Copy everything below and paste it into Canvas")
    print(report)
    print("=" * WIDTH)
    if SAVE_REPORT:
        save_report(name, report)
    print("\nThanks for playing, Colonel Washington!\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nSimulation ended. Run the program again to start over.\n")
