# Test of tts graph to viseme implemntation
import time
import os

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

def animate_text(text):
    for char in text:
        viseme = get_viseme(char)
        print(VISEMES[viseme])
        time.sleep(0.5)  # Simulate time taken for each phoneme

animate_text("For the Omnissiah")