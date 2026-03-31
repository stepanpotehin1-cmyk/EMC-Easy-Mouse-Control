#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMC (Easy Mouse Control) - Beautiful GUI Version
Control your mouse cursor using keyboard arrow keys!

Author: Stepan
Version: 1.1.0
"""

import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkSlider, CTkSwitch, CTkProgressBar
import pynput
from pynput import keyboard, mouse
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
import threading
import time
import sys
import tkinter as tk

# Theme Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Mouse Controller
mouse_controller = MouseController()

# Settings
DEFAULT_SPEED = 10
MIN_SPEED = 1
MAX_SPEED = 50
current_speed = DEFAULT_SPEED

# State Flags
running = True
is_active = False
ctrl_pressed = False
keys_pressed = {'up': False, 'down': False, 'left': False, 'right': False}

# Colors
COLORS = {
    'bg': '#1a1a2e',
    'card': '#16213e',
    'accent': '#0f3460',
    'highlight': '#e94560',
    'text': '#eaeaea',
    'success': '#00d9ff',
    'warning': '#ffc107'
}


class EMCApp(CTk):
    def __init__(self):
        super().__init__()
        
        # Window Setup
        self.title("🖱️ EMC - Easy Mouse Control")
        self.geometry("500x650")
        self.resizable(False, False)
        self.configure(fg_color=COLORS['bg'])
        
        # Icon (create simple one)
        self.create_icon()
        
        # Variables
        self.current_speed = ctk.DoubleVar(value=DEFAULT_SPEED)
        self.is_running = False
        self.move_thread = None
        self.keyboard_listener = None
        
        # Build UI
        self.build_ui()
        
        # Protocol
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def create_icon(self):
        """Create a simple icon for the window."""
        pass  # Icon creation skipped for compatibility
    
    def build_ui(self):
        """Build the beautiful user interface."""
        # Main Container
        self.main_frame = CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = CTkLabel(
            self.main_frame,
            text="🖱️ Easy Mouse Control",
            font=ctk.CTkFont(family="Helvetica", size=28, weight="bold"),
            text_color=COLORS['text']
        )
        self.title_label.pack(pady=(0, 5))
        
        # Subtitle
        self.subtitle_label = CTkLabel(
            self.main_frame,
            text="Control your cursor with keyboard arrows",
            font=ctk.CTkFont(family="Helvetica", size=12),
            text_color="#888888"
        )
        self.subtitle_label.pack(pady=(0, 20))
        
        # Status Card
        self.status_card = self.create_card("Status")
        self.status_card.pack(fill="x", pady=10)
        
        self.status_indicator = CTkLabel(
            self.status_card,
            text="⏸️ STOPPED",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"),
            text_color="#ff6b6b"
        )
        self.status_indicator.pack(pady=10)
        
        self.status_text = CTkLabel(
            self.status_card,
            text="Press START to activate mouse control",
            font=ctk.CTkFont(family="Helvetica", size=11),
            text_color="#aaaaaa"
        )
        self.status_text.pack(pady=(0, 5))
        
        # Speed Control Card
        self.speed_card = self.create_card("Speed Control")
        self.speed_card.pack(fill="x", pady=10)
        
        self.speed_value_label = CTkLabel(
            self.speed_card,
            text=f"Speed: {int(self.current_speed.get())} px",
            font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"),
            text_color=COLORS['success']
        )
        self.speed_value_label.pack(pady=5)
        
        self.speed_slider = CTkSlider(
            self.speed_card,
            from_=MIN_SPEED,
            to=MAX_SPEED,
            variable=self.current_speed,
            command=self.on_speed_change,
            progress_color=COLORS['highlight'],
            button_color=COLORS['highlight'],
            button_hover_color="#ff2e63"
        )
        self.speed_slider.pack(fill="x", padx=20, pady=10)
        
        # Speed Buttons
        self.speed_buttons_frame = CTkFrame(self.speed_card, fg_color="transparent")
        self.speed_buttons_frame.pack(fill="x", padx=20, pady=5)
        
        self.btn_slower = CTkButton(
            self.speed_buttons_frame,
            text="➖ Slower",
            command=self.decrease_speed,
            fg_color=COLORS['accent'],
            hover_color=COLORS['highlight'],
            font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
            width=100
        )
        self.btn_slower.pack(side="left", padx=5)
        
        self.btn_faster = CTkButton(
            self.speed_buttons_frame,
            text="➕ Faster",
            command=self.increase_speed,
            fg_color=COLORS['accent'],
            hover_color=COLORS['highlight'],
            font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
            width=100
        )
        self.btn_faster.pack(side="right", padx=5)
        
        # Controls Card
        self.controls_card = self.create_card("Keyboard Controls")
        self.controls_card.pack(fill="x", pady=10)
        
        controls_text = """
⬆️⬇️⬅️➡️ Arrow Keys     → Move cursor

⏎ Enter                   → Left click

⌨️ Ctrl + Enter           → Right click

➕ Plus / Equals          → Increase speed

➖ Minus                  → Decrease speed

⎋ Escape                 → Stop program
        """
        
        self.controls_label = CTkLabel(
            self.controls_card,
            text=controls_text,
            font=ctk.CTkFont(family="Consolas", size=11),
            text_color="#cccccc",
            justify="left"
        )
        self.controls_label.pack(pady=10, padx=10)
        
        # Main Action Button
        self.btn_main = CTkButton(
            self.main_frame,
            text="▶️  START",
            command=self.toggle_control,
            fg_color="#00d9ff",
            hover_color="#00a8cc",
            text_color="#000000",
            font=ctk.CTkFont(family="Helvetica", size=20, weight="bold"),
            height=50,
            corner_radius=10
        )
        self.btn_main.pack(fill="x", pady=20)
        
        # Footer
        self.footer = CTkLabel(
            self.main_frame,
            text="Made with ❤️ by Stepan  •  EMC v1.1.0",
            font=ctk.CTkFont(family="Helvetica", size=10),
            text_color="#666666"
        )
        self.footer.pack(pady=(10, 0))
    
    def create_card(self, title):
        """Create a styled card frame."""
        card = CTkFrame(self.main_frame, fg_color=COLORS['card'], corner_radius=15)
        
        title_label = CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"),
            text_color=COLORS['highlight']
        )
        title_label.pack(anchor="w", padx=15, pady=(10, 0))
        
        return card
    
    def on_speed_change(self, value):
        """Handle speed slider change."""
        global current_speed
        current_speed = int(value)
        self.speed_value_label.configure(text=f"Speed: {current_speed} px")
    
    def increase_speed(self):
        """Increase cursor speed."""
        global current_speed
        current_speed = min(current_speed + 2, MAX_SPEED)
        self.current_speed.set(current_speed)
        self.speed_value_label.configure(text=f"Speed: {current_speed} px")
    
    def decrease_speed(self):
        """Decrease cursor speed."""
        global current_speed
        current_speed = max(current_speed - 2, MIN_SPEED)
        self.current_speed.set(current_speed)
        self.speed_value_label.configure(text=f"Speed: {current_speed} px")
    
    def toggle_control(self):
        """Toggle mouse control on/off."""
        if not self.is_running:
            self.start_control()
        else:
            self.stop_control()
    
    def start_control(self):
        """Start mouse control."""
        global running, is_active, keys_pressed
        
        running = True
        is_active = True
        self.is_running = True
        
        # Reset keys
        keys_pressed = {'up': False, 'down': False, 'left': False, 'right': False}
        
        # Update UI
        self.status_indicator.configure(text="▶️ ACTIVE", text_color="#00ff88")
        self.status_text.configure(text="Use arrow keys to control cursor")
        self.btn_main.configure(
            text="⏹️  STOP",
            fg_color="#ff6b6b",
            hover_color="#ee5a5a"
        )
        
        # Start movement thread
        self.move_thread = threading.Thread(target=self.move_mouse_loop, daemon=True)
        self.move_thread.start()
        
        # Start keyboard listener
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        )
        self.keyboard_listener.start()
    
    def stop_control(self):
        """Stop mouse control."""
        global running, is_active
        
        running = False
        is_active = False
        self.is_running = False
        
        # Stop listener
        if self.keyboard_listener:
            self.keyboard_listener.stop()
            self.keyboard_listener = None
        
        # Update UI
        self.status_indicator.configure(text="⏸️ STOPPED", text_color="#ff6b6b")
        self.status_text.configure(text="Press START to activate mouse control")
        self.btn_main.configure(
            text="▶️  START",
            fg_color="#00d9ff",
            hover_color="#00a8cc",
            text_color="#000000"
        )
    
    def move_mouse_loop(self):
        """Main loop for moving mouse cursor."""
        global running, current_speed
        
        while running:
            dx = 0
            dy = 0
            
            if keys_pressed['up']:
                dy -= current_speed
            if keys_pressed['down']:
                dy += current_speed
            if keys_pressed['left']:
                dx -= current_speed
            if keys_pressed['right']:
                dx += current_speed
            
            if dx != 0 or dy != 0:
                try:
                    current_x, current_y = mouse_controller.position
                    mouse_controller.position = (current_x + dx, current_y + dy)
                except:
                    pass
            
            time.sleep(0.01)
    
    def on_key_press(self, key):
        """Handle key press events."""
        global ctrl_pressed, current_speed, running
        
        try:
            # Track Ctrl key
            if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                ctrl_pressed = True
            
            # Arrow keys
            if key == keyboard.Key.up:
                keys_pressed['up'] = True
            elif key == keyboard.Key.down:
                keys_pressed['down'] = True
            elif key == keyboard.Key.left:
                keys_pressed['left'] = True
            elif key == keyboard.Key.right:
                keys_pressed['right'] = True
            
            # Speed control with +/-/=
            elif hasattr(key, 'char'):
                if key.char in ['+', '=']:
                    self.increase_speed()
                elif key.char == '-':
                    self.decrease_speed()
            
            # Mouse clicks
            elif key == keyboard.Key.enter:
                if ctrl_pressed:
                    mouse_controller.click(Button.right)
                else:
                    mouse_controller.click(Button.left)
            
            # Exit on Escape
            elif key == keyboard.Key.esc:
                self.after(0, self.stop_control)
                
        except AttributeError:
            pass
    
    def on_key_release(self, key):
        """Handle key release events."""
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
    
    def on_close(self):
        """Clean up and close application."""
        self.stop_control()
        self.destroy()
        sys.exit(0)


def main():
    """Main entry point."""
    print("🖱️ EMC - Easy Mouse Control v1.1.0")
    print("Launching GUI...")
    
    app = EMCApp()
    app.mainloop()


if __name__ == "__main__":
    main()
