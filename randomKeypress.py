from pynput.keyboard import Controller
from pynput.mouse import Controller as MouseController
import random
import time

# Création des contrôleurs clavier et souris
keyboard = Controller()
mouse = MouseController()
tryCounter = 0
count = 0

keys = ['z', 'q', 's', 'd']

# Fonction pour générer un mouvement de la souris aléatoire
def move_mouse_randomly():
    x_offset = random.randint(-100, 100)
    y_offset = random.randint(-100, 100)
    current_x, current_y = mouse.position
    mouse.position = (current_x + x_offset, current_y + y_offset)
    print(f"Souris déplacée à ({mouse.position[0]}, {mouse.position[1]})")

# Boucle infinie pour simuler des actions aléatoires
while True:
    if random.random() < 0.8:
        key = random.choice(keys)
        keyboard.press(key)
        time.sleep(random.uniform(0.3, 1.2))
        keyboard.release(key)
        print(f"Touche pressée : {key}")
        tryCounter += 1
        count += 1
        if tryCounter == 5:
            print(f"Il y'a eu {count} touches pressées")
            tryCounter = 0
    else:
        move_mouse_randomly()
    
    time.sleep(random.randint(120, 180))  # Attente aléatoire entre 2 et 3 minutes