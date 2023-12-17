import random 
import pyautogui as pg
import time
import pyperclip as clipboard

# Create a list of animals
animal = ('Elephant','Donkey','Dog','Monkey')

# Let the game initialize for a few seconds
time.sleep(8)

for i in range(500):
    a = random.choice(animal)

    # Simulate the act of typing into the search bar
    for char in a:
        pg.press(char)
        time.sleep(random.uniform(0.01, 0.05)) # Add a small random delay

    # Paste the selected animal into the search bar
    clipboard.copy(a)
    pg.hotkey('ctrl', 'v')

    # Press 'enter' to submit the search
    pg.press('enter')
    
