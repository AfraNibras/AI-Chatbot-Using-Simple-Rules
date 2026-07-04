"""
chatbot.py
-----------
Main program for AI Chatbot Using Simple Rules.
"""

from colorama import Fore
from responses import RESPONSES
from utils import (
    display_banner,
    bot_print,
    get_current_time,
    get_current_date,
)


def chatbot():
    display_banner()

    while True:
        user_input = input(Fore.CYAN + "👤 You: ").strip().lower()

        # Greetings
        if (
            user_input == "hello"
            or user_input == "hi"
            or user_input == "hey"
            or user_input.startswith("hello ")
            or user_input.startswith("hi ")
            or user_input.startswith("hey ")
        ):
            bot_print(RESPONSES["greeting"])

        elif "good morning" in user_input:
            bot_print(RESPONSES["good_morning"])

        elif "good afternoon" in user_input:
            bot_print(RESPONSES["good_afternoon"])

        elif "good evening" in user_input:
            bot_print(RESPONSES["good_evening"])

        # Identity
        elif (
            "your name" in user_input
            or "what is your name" in user_input
            or "who are you" in user_input
            or user_input == "name"
            or user_input == "ur name"
        ):
            bot_print(RESPONSES["name"])

        elif "creator" in user_input or "who created you" in user_input:
            bot_print(RESPONSES["creator"])

        elif "what can you do" in user_input or "about yourself" in user_input:
            bot_print(RESPONSES["about"])

        # AI Topics
        elif (
            "machine learning" in user_input
            or user_input == "ml"
            or "what is machine learning" in user_input
        ):
            bot_print(RESPONSES["ml"])

        elif (
            "deep learning" in user_input
            or user_input == "dl"
            or "what is deep learning" in user_input
        ):
            bot_print(RESPONSES["dl"])

        elif (
            user_input == "ai"
            or "artificial intelligence" in user_input
            or "what is ai" in user_input
            or "explain ai" in user_input
        ):
            bot_print(RESPONSES["ai"])

        # Programming
        elif "python" in user_input or "what is python" in user_input:
            bot_print(RESPONSES["python"])

        elif "github" in user_input:
            bot_print(RESPONSES["github"])

        # Utilities
        elif "time" in user_input:
            bot_print(f"Current Time: {get_current_time()}")

        elif "date" in user_input:
            bot_print(f"Today's Date: {get_current_date()}")

        # Fun
        elif "joke" in user_input:
            bot_print(RESPONSES["joke"])

        elif "quote" in user_input or "motivate" in user_input:
            bot_print(RESPONSES["quote"])

        # Courtesy
        elif "thank" in user_input:
            bot_print(RESPONSES["thanks"])

        # Help
        elif "help" in user_input:
            bot_print(RESPONSES["help"])

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            bot_print(RESPONSES["bye"])
            break

        # Unknown Input
        else:
            bot_print(
                "Sorry, I couldn't understand your question.\n"
                "Type 'help' to see the available commands."
            )


if __name__ == "__main__":
    chatbot() 