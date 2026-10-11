# ============================================================
#                    PYTHON DESKTOP AI
#              A mini personal assistant 🤖
# ============================================================

import os
import random
import math
import datetime
import json
import webbrowser
import secrets
import string
import ast
import operator


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
BLUE = "\033[94m"


# ============================================================
# FILES
# ============================================================

NOTES_FILE = "my_notes.json"


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4)


notes = load_notes()


# ============================================================
# SAFE CALCULATOR
# ============================================================

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg
}


def calculate(expression):

    def solve(node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            left = solve(node.left)
            right = solve(node.right)

            operation = operators[type(node.op)]

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            return operators[type(node.op)](solve(node.operand))

        raise ValueError

    try:
        tree = ast.parse(expression, mode="eval")
        result = solve(tree.body)
        return result

    except:
        return None


# ============================================================
# PASSWORD GENERATOR
# ============================================================

def generate_password(length=16):

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-=[]{}"
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


# ============================================================
# BANNER
# ============================================================

def banner():

    os.system("cls" if os.name == "nt" else "clear")

    print(CYAN + r"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║              ██████╗ ██╗   ██╗████████╗██╗  ██╗          ║
║              ██╔══██╗██║   ██║╚══██╔══╝██║  ██║          ║
║              ██████╔╝██║   ██║   ██║   ███████║          ║
║              ██╔═══╝ ██║   ██║   ██║   ██╔══██║          ║
║              ██║     ╚██████╔╝   ██║   ██║  ██║          ║
║              ╚═╝      ╚═════╝    ╚═╝   ╚═╝  ╚═╝          ║
║                                                            ║
║                 PERSONAL PYTHON AI 🤖                     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""" + RESET)

    print(YELLOW + "Type 'help' to see what I can do.\n" + RESET)


# ============================================================
# HELP
# ============================================================

def show_help():

    print(CYAN + """
╔════════════════════ COMMANDS ══════════════════════════════╗

  help
      Show this menu.

  time
      Show current time.

  date
      Show today's date.

  calc 25 * 17
      Powerful calculator.

  password
      Generate a secure password.

  note buy milk
      Save a note permanently.

  notes
      Show all saved notes.

  clear
      Clear the terminal.

  google Python
      Search Google.

  youtube music
      Search YouTube.

  joke
      Tell a random joke.

  about
      Show information about this program.

  exit
      Close the AI.

╚════════════════════════════════════════════════════════════╝
""" + RESET)


# ============================================================
# JOKES
# ============================================================

jokes = [
    "Why do programmers hate nature? It has too many bugs. 🐛",
    "I told Python I needed space. It gave me indentation. 😂",
    "There are only 10 types of people: those who understand binary and those who don't.",
    "A programmer's favorite place? The terminal. 😎",
    "Why was the computer cold? It left its Windows open."
]


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process(command):

    global notes

    command = command.strip()

    if not command:
        return True

    lower = command.lower()

    # EXIT
    if lower in ["exit", "quit", "bye"]:

        print(GREEN + "\nAI: See you later, developer. 👋\n" + RESET)

        return False


    # HELP
    elif lower == "help":

        show_help()


    # TIME
    elif lower == "time":

        now = datetime.datetime.now()

        print(
            GREEN +
            f"\nAI: Current time → {now.strftime('%I:%M:%S %p')}\n"
            + RESET
        )


    # DATE
    elif lower == "date":

        now = datetime.datetime.now()

        print(
            GREEN +
            f"\nAI: Today is → {now.strftime('%A, %d %B %Y')}\n"
            + RESET
        )


    # CALCULATOR
    elif lower.startswith("calc "):

        expression = command[5:]

        result = calculate(expression)

        if result is None:

            print(RED + "\nAI: I couldn't calculate that.\n" + RESET)

        else:

            print(
                GREEN +
                f"\nAI: {expression} = {result}\n"
                + RESET
            )


    # PASSWORD
    elif lower.startswith("password"):

        parts = command.split()

        length = 16

        if len(parts) == 2:

            try:
                length = int(parts[1])
            except:
                pass

        if length < 6:
            length = 6

        password = generate_password(length)

        print(
            GREEN +
            f"\nAI: Your secure password:\n\n"
            f"     {password}\n\n"
            + RESET
        )


    # NOTE
    elif lower.startswith("note "):

        text = command[5:].strip()

        if text:

            notes.append({
                "text": text,
                "time": datetime.datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            })

            save_notes(notes)

            print(
                GREEN +
                "\nAI: Note saved permanently. 📝\n"
                + RESET
            )


    # SHOW NOTES
    elif lower == "notes":

        if not notes:

            print(YELLOW + "\nAI: You have no notes.\n" + RESET)

        else:

            print(CYAN + "\nYOUR NOTES\n" + RESET)

            for i, note in enumerate(notes, 1):

                print(
                    f"{i}. {note['text']}"
                    f"  [{note['time']}]"
                )

            print()


    # CLEAR
    elif lower == "clear":

        banner()


    # GOOGLE
    elif lower.startswith("google "):

        query = command[7:]

        print(
            GREEN +
            f"\nAI: Opening Google for '{query}'...\n"
            + RESET
        )

        webbrowser.open(
            "https://www.google.com/search?q=" +
            query.replace(" ", "+")
        )


    # YOUTUBE
    elif lower.startswith("youtube "):

        query = command[8:]

        print(
            GREEN +
            f"\nAI: Opening YouTube for '{query}'...\n"
            + RESET
        )

        webbrowser.open(
            "https://www.youtube.com/results?search_query=" +
            query.replace(" ", "+")
        )


    # JOKE
    elif lower == "joke":

        print(
            YELLOW +
            "\nAI: " +
            random.choice(jokes) +
            "\n" +
            RESET
        )


    # ABOUT
    elif lower == "about":

        print(CYAN + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  PERSONAL PYTHON AI                                        ║
║                                                            ║
║  Built using Python standard library.                      ║
║                                                            ║
║  Features:                                                 ║
║  • File handling                                           ║
║  • JSON database                                           ║
║  • Secure password generation                              ║
║  • Calculator                                              ║
║  • Browser automation                                      ║
║  • Date/time                                               ║
║  • Randomization                                           ║
║  • Command processing                                      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""" + RESET)


    # GREETINGS
    elif lower in ["hi", "hello", "hey", "namaste"]:

        responses = [
            "Hello developer! 👨‍💻",
            "Hey! What are we building today? 🔥",
            "Namaste! Python is ready. 🐍",
            "What's up? Let's code something crazy. 🚀"
        ]

        print(GREEN + "\nAI: " + random.choice(responses) + "\n" + RESET)


    # UNKNOWN
    else:

        print(
            RED +
            "\nAI: I don't understand that command.\n"
            +YELLOW +
            "Type 'help' to see available commands.\n"
            + RESET
        )

    return True


# ============================================================
# START
# ============================================================

banner()

running = True

while running:

    try:

        command = input(
            CYAN +
            "YOU ❯ " +
            RESET
        )

        running = process(command)

    except KeyboardInterrupt:

        print(
            "\n\n" +
            YELLOW +
            "AI: Interrupted. Bye! 👋\n" +
            RESET
        )

        break

    except Exception as error:

        print(
            RED +
            f"\nSomething went wrong: {error}\n" +
            RESET
        )