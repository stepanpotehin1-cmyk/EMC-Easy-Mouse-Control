#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programma dlya upravleniya myshkoy s pomoshch'yu strelokek na klaviature.

Upravleniye:
- Strelki          - dvizheniye kursora
- Enter            - klik levoy knopkoy myshi
- Ctrl + Enter     - klik pravoy knopkoy myshi
- + / =            - uvelichit' skorost'
- -                - umen'shit' skorost'
- Esc              - vykhod iz programmy
"""

import pynput
from pynput import keyboard, mouse
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Button, Controller
import threading
import time
import sys

# Kontroller myshi
mouse_controller = MouseController()

# Nachal'naya skorost' dvizheniya kursora (pikseley za odin shag)
MOVE_SPEED = 10
MIN_SPEED = 1
MAX_SPEED = 50

# Flag dlya ostanovki programmy
running = True
move_thread = None

# Flag dlya otslezhivaniya nazhatiya Ctrl
ctrl_pressed = False


def move_mouse():
    """Functsiya dlya nepreryvnogo dvizheniya myshi pri uderzhanii klavish."""
    global running
    
    while running:
        dx = 0
        dy = 0
        
        if keys_pressed['up']:
            dy -= MOVE_SPEED
        if keys_pressed['down']:
            dy += MOVE_SPEED
        if keys_pressed['left']:
            dx -= MOVE_SPEED
        if keys_pressed['right']:
            dx += MOVE_SPEED
        
        if dx != 0 or dy != 0:
            # Poluchaem tekushchuyu pozitsiyu i peremeshchaem mysh'
            current_x, current_y = mouse_controller.position
            mouse_controller.position = (current_x + dx, current_y + dy)
        
        time.sleep(0.01)  # Nebol'shaya zaderzhka dlya plavnosti
    
    # Potok zavershen
    print("[INFO] Potok dvizheniya myshi ostanovlen.")


def on_press(key):
    """Obrabotchik nazhatiya klavish."""
    global running, ctrl_pressed, MOVE_SPEED
    
    try:
        # Otslezhivanie Ctrl
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True
        
        # Upravleniye strelkami
        if key == keyboard.Key.up:
            keys_pressed['up'] = True
        elif key == keyboard.Key.down:
            keys_pressed['down'] = True
        elif key == keyboard.Key.left:
            keys_pressed['left'] = True
        elif key == keyboard.Key.right:
            keys_pressed['right'] = True
        
        # Upravleniye skorost'yu
        elif hasattr(key, 'char'):
            if key.char == '+' or key.char == '=':
                MOVE_SPEED = min(MOVE_SPEED + 2, MAX_SPEED)
                print(f"[INFO] Skorost' uvelichena: {MOVE_SPEED}")
            elif key.char == '-':
                MOVE_SPEED = max(MOVE_SPEED - 2, MIN_SPEED)
                print(f"[INFO] Skorost' umen'shena: {MOVE_SPEED}")
        
        # Klik levoy knopkoy (Enter bez Ctrl)
        elif key == keyboard.Key.enter:
            if ctrl_pressed:
                mouse_controller.click(mouse.Button.right)
                print("[+] Klik pravoy knopkoy")
            else:
                mouse_controller.click(mouse.Button.left)
                print("[+] Klik levoy knopkoy")
        
        # Vykhod iz programmy
        elif key == keyboard.Key.esc:
            print("\n[INFO] Vykhod iz programmy...")
            running = False
            return False  # Ostanavlivaem slushatel'
            
    except AttributeError:
        pass


def on_release(key):
    """Obrabotchik otpuksaniya klavish."""
    global ctrl_pressed
    
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = False
        elif key == keyboard.Key.up:
            keys_pressed['up'] = False
        elif key == keyboard.Key.down:
            keys_pressed['down'] = False
        elif key == keyboard.Key.left:
            keys_pressed['left'] = False
        elif key == keyboard.Key.right:
            keys_pressed['right'] = False
    except AttributeError:
        pass


def main():
    global running, move_thread, keys_pressed
    
    # Initsializatsiya flagov klavish
    keys_pressed = {
        'up': False,
        'down': False,
        'left': False,
        'right': False
    }
    
    print("=" * 50)
    print("Upravleniye myshkoy s klaviatury")
    print("=" * 50)
    print("Strelki              - dvizheniye kursora")
    print("Enter                - klik levoy knopkoy")
    print("Ctrl + Enter         - klik pravoy knopkoy")
    print("+ ili =              - uvelichit' skorost'")
    print("-                    - umen'shit' skorost'")
    print("Esc                  - vykhod")
    print("=" * 50)
    print(f"Tekushchaya skorost': {MOVE_SPEED}")
    print("Programma zapushchena! Ispol'zuyte strelki dlya upravleniya.")
    print()
    
    # Zapuskaem potok dlya dvizheniya myshi
    move_thread = threading.Thread(target=move_mouse)
    move_thread.daemon = True
    move_thread.start()
    
    # Slushaem klaviaturu
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    # Jdem zaversheniya potoka dvizheniya myshi (ne bolee 1 sekundy)
    if move_thread and move_thread.is_alive():
        move_thread.join(timeout=1.0)
    
    print("Programma zavershena.")
    sys.exit(0)


if __name__ == "__main__":
    main()
