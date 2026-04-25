# Test of tts graph to viseme implemntation
import sys
import time
import os

# ANSI escape code to reset cursor to top-left corner
RESET_CURSOR = "\033[H"
# Hide the blinking cursor 
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"


VISEMES = {
    "CLOSED":  "       [  XXXXXXXXXXX  ]       ",
    "LABIO":   "       [  I_I_I_I_I_I  ]       ",
    "OPEN":    "       [               ]       ",
    "ROUND":   "       [     (   )     ]       ",
    "DENTAL":  "       [  -----------  ]       ",
    "REST":    "       [  ___________  ]       "
}

# Simple mapping logic
def get_viseme(char):
    c = char.lower()
    if c in ['m', 'p', 'b']: return "CLOSED"
    if c in ['f', 'v']: return "LABIO"
    if c in ['a', 'i', 'e', 'u', 'o']: return "OPEN"
    if c in ['w', 'r']: return "ROUND"
    if c in ['t', 'd', 's', 'z']: return "DENTAL"
    return "REST"

def speak(text):
    sys.stdout.write(HIDE_CURSOR)  # Hide cursor
    try:
         for char in text:
            viseme = get_viseme(char)
            # move cursor to top
            sys.stdout.write(RESET_CURSOR)
            # print the frame and current letter
            sys.stdout.write(f"Speaking: '{char}'\n")
            sys.stdout.write("\033[32m" + VISEMES[viseme] + "\033[0m")  # Green color for viseme
            # force terminal to update
            sys.stdout.flush()
            # space between phonemes
            time.sleep(0.5)  # Simulate time taken for each phoneme
    finally:
        sys.stdout.write(SHOW_CURSOR)  # Show cursor again
speak("For the Omnissiah")