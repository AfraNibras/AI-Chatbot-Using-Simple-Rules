"""
utils.py
---------
Helper functions for the chatbot.
"""

from datetime import datetime
import time
from colorama import init, Fore, Style

init(autoreset=True)


def display_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "           AI CHATBOT USING SIMPLE RULES")
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "Type 'help' to see available commands.")
    print(Fore.YELLOW + "Type 'bye' to exit.\n")


def bot_print(message):
    print(Fore.GREEN + "🤖 Bot: ", end="", flush=True)

    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.02)

    print(Style.RESET_ALL)


def get_current_time():
    return datetime.now().strftime("%I:%M %p")


def get_current_date():
    return datetime.now().strftime("%d %B %Y")