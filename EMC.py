#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMC (Easy Mouse Control) v1.2.0
Control your mouse cursor using keyboard arrow keys!
"""

import customtkinter as ctk
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput import keyboard
import threading
import time
import sys

# Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

mouse_controller = MouseController()

DEFAULT_SPEED = 10
MIN_SPEED = 1
MAX_SPEED = 50

current_speed = DEFAULT_SPEED
running = False
ctrl_pressed = False
keys_pressed = {'up': False, 'down': False, 'left': False, 'right': False}


class EMCApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("EMC - Easy Mouse Control v1.2.0")
        self.geometry("480x720")
        self.resizable(False, False)
        self.configure(fg_color="#1a1a2e")
        
        self.current_speed = ctk.IntVar(value=DEFAULT_SPEED)
        self.is_running = False
        self.move_thread = None
        self.keyboard_listener = None
        
        self.build_ui()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def build_ui(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Title
        ctk.CTkLabel(
            self.main_frame,
            text="EMC",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color="#e94560"
        ).pack()
        
        ctk.CTkLabel(
            self.main_frame,
            text="Easy Mouse Control",
            font=ctk.CTkFont(size=14),
            text_color="#888888"
        ).pack(pady=(0, 15))
        
        # Status Frame
        status_frame = ctk.CTkFrame(self.main_frame, fg_color="#16213e", corner_radius=12)
        status_frame.pack(fill="x", pady=8)
        
        ctk.CTkLabel(
            status_frame,
            text="STATUS",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#e94560"
        ).pack(anchor="w", padx=15, pady=(10, 0))
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="STOPPED",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#ff6b6b"
        )
        self.status_label.pack(pady=10)
        
        # Speed Frame
        speed_frame = ctk.CTkFrame(self.main_frame, fg_color="#16213e", corner_radius=12)
        speed_frame.pack(fill="x", pady=8)
        
        ctk.CTkLabel(
            speed_frame,
            text="SPEED CONTROL",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#e94560"
        ).pack(anchor="w", padx=15, pady=(10, 0))
        
        self.speed_text = ctk.CTkLabel(
            speed_frame,
            text="Speed: 10 px",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#00d9ff"
        )
        self.speed_text.pack(pady=8)
        
        self.speed_slider = ctk.CTkSlider(
            speed_frame,
            from_=MIN_SPEED,
            to=MAX_SPEED,
            variable=self.current_speed,
            command=self.on_speed_change,
            progress_color="#e94560",
            button_color="#e94560"
        )
        self.speed_slider.pack(fill="x", padx=15, pady=5)
        
        # Speed buttons
        btn_frame = ctk.CTkFrame(speed_frame, fg_color="transparent")
        btn_frame.pack(fill="x", padx=15, pady=10)
        
        ctk.CTkButton(
            btn_frame,
            text="- Slower",
            command=self.decrease_speed,
            fg_color="#0f3460",
            hover_color="#e94560",
            width=100
        ).pack(side="left", padx=5)
        
        ctk.CTkButton(
            btn_frame,
            text="+ Faster",
            command=self.increase_speed,
            fg_color="#0f3460",
            hover_color="#e94560",
            width=100
        ).pack(side="right", padx=5)
        
        # Controls Frame
        controls_frame = ctk.CTkFrame(self.main_frame, fg_color="#16213e", corner_radius=12)
        controls_frame.pack(fill="x", pady=8)
        
        ctk.CTkLabel(
            controls_frame,
            text="CONTROLS",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#e94560"
        ).pack(anchor="w", padx=15, pady=(10, 0))
        
        controls_text = """Arrow Keys  - Move cursor
Enter       - Left click
Ctrl+Enter  - Right click
+ or =      - Increase speed
-           - Decrease speed
Esc         - Stop / Exit"""
        
        ctk.CTkLabel(
            controls_frame,
            text=controls_text,
            font=ctk.CTkFont(family="Courier New", size=12),
            text_color="#cccccc",
            justify="left"
        ).pack(pady=15, padx=15)
        
        # BIG START/STOP BUTTON
        self.main_btn = ctk.CTkButton(
            self.main_frame,
            text="START",
            command=self.toggle,
            fg_color="#00d9ff",
            hover_color="#00a8cc",
            text_color="#000000",
            font=ctk.CTkFont(size=24, weight="bold"),
            height=60,
            corner_radius=15
        )
        self.main_btn.pack(fill="x", pady=20)
        
        # Footer
        ctk.CTkLabel(
            self.main_frame,
            text="Made by Stepan | EMC v1.2.0",
            font=ctk.CTkFont(size=10),
            text_color="#666666"
        ).pack()
    
    def on_speed_change(self, val):
        global current_speed
        current_speed = int(val)
        self.speed_text.configure(text=f"Speed: {current_speed} px")
    
    def increase_speed(self):
        global current_speed
        current_speed = min(current_speed + 2, MAX_SPEED)
        self.current_speed.set(current_speed)
        self.speed_text.configure(text=f"Speed: {current_speed} px")
    
    def decrease_speed(self):
        global current_speed
        current_speed = max(current_speed - 2, MIN_SPEED)
        self.current_speed.set(current_speed)
        self.speed_text.configure(text=f"Speed: {current_speed} px")
    
    def toggle(self):
        if not self.is_running:
            self.start()
        else:
            self.stop()
    
    def start(self):
        global running, keys_pressed
        running = True
        self.is_running = True
        keys_pressed = {'up': False, 'down': False, 'left': False, 'right': False}
        
        self.status_label.configure(text="ACTIVE", text_color="#00ff88")
        self.main_btn.configure(
            text="STOP",
            fg_color="#ff6b6b",
            hover_color="#ee5a5a",
            text_color="#ffffff"
        )
        
        self.move_thread = threading.Thread(target=self.move_loop, daemon=True)
        self.move_thread.start()
        
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        )
        self.keyboard_listener.start()
    
    def stop(self):
        global running
        running = False
        self.is_running = False
        
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        
        self.status_label.configure(text="STOPPED", text_color="#ff6b6b")
        self.main_btn.configure(
            text="START",
            fg_color="#00d9ff",
            hover_color="#00a8cc",
            text_color="#000000"
        )
    
    def move_loop(self):
        global running, current_speed
        while running:
            dx = dy = 0
            if keys_pressed['up']: dy -= current_speed
            if keys_pressed['down']: dy += current_speed
            if keys_pressed['left']: dx -= current_speed
            if keys_pressed['right']: dx += current_speed
            
            if dx != 0 or dy != 0:
                try:
                    x, y = mouse_controller.position
                    mouse_controller.position = (x + dx, y + dy)
                except:
                    pass
            time.sleep(0.01)
    
    def on_key_press(self, key):
        global ctrl_pressed, current_speed, running
        
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True
        elif key == keyboard.Key.up:
            keys_pressed['up'] = True
        elif key == keyboard.Key.down:
            keys_pressed['down'] = True
        elif key == keyboard.Key.left:
            keys_pressed['left'] = True
        elif key == keyboard.Key.right:
            keys_pressed['right'] = True
        elif hasattr(key, 'char'):
            if key.char in ['+', '=']:
                self.increase_speed()
            elif key.char == '-':
                self.decrease_speed()
        elif key == keyboard.Key.enter:
            mouse_controller.click(Button.right if ctrl_pressed else Button.left)
        elif key == keyboard.Key.esc:
            self.after(0, self.stop)
    
    def on_key_release(self, key):
        global ctrl_pressed
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
    
    def on_close(self):
        self.stop()
        self.destroy()
        sys.exit(0)


if __name__ == "__main__":
    app = EMCApp()
    app.mainloop()
