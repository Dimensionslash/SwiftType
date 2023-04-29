import tkinter as tk
import pyautogui
import time
from tkinter import messagebox


class Typer:

    def __init__(self):
        self.start_time = 0
        self.text = ""
        self.typing_speed = 20
        self.startup_delay = 3

    def set_startup_delay(self, value):
        self.startup_delay = value

    def set_typing_speed(self, value):
        self.typing_speed = value

    def set_text(self, text):
        self.text = text

    def print_text(self):
        time.sleep(self.startup_delay)
        pyautogui.typewrite(self.text, interval=1 / self.typing_speed)

    def on_key(self, event):
        if event.char == '\x1b':
            root.destroy()
        elif event.char == '0':
            if time.time() - self.start_time < 4:
                self.print_text()
            else:
                messagebox.showwarning(
                    "Time Limit Exceeded",
                    "Sorry, the time limit has been exceeded.")

    def start(self):
        self.set_startup_delay(delay_scale.get())
        self.set_typing_speed(speed_scale.get())
        self.set_text(text_entry.get("1.0", tk.END))
        self.print_text()


def start_program():
    global root
    root = tk.Tk()
    root.title("Text Typer")
    root.geometry("400x400")
    root.configure(bg="#f7f7f7")

    text_label = tk.Label(root,
                          text="Enter text to type:",
                          font=("Arial", 12),
                          bg="#f7f7f7")
    text_label.pack(pady=10)

    global text_entry, speed_scale, delay_scale
    text_entry = tk.Text(root,
                         font=("Arial", 12),
                         height=15,
                         wrap="word",
                         bd=2)
    text_entry.pack(pady=10)

    speed_label = tk.Label(root,
                           text="Typing Speed:",
                           font=("Arial", 12),
                           bg="#f7f7f7")
    speed_label.pack(pady=10)

    speed_scale = tk.Scale(root, from_=20, to=120, orient="horizontal")
    speed_scale.set(60)
    speed_scale.pack(pady=10)

    delay_label = tk.Label(root,
                           text="Startup Delay:",
                           font=("Arial", 12),
                           bg="#f7f7f7")
    delay_label.pack(pady=10)

    delay_scale = tk.Scale(root, from_=0, to=10, orient="horizontal")
    delay_scale.set(3)
    delay_scale.pack(pady=10)

    button_frame = tk.Frame(root, bg="#f7f7f7")
    button_frame.pack(pady=10)

    start_button = tk.Button(button_frame,
                             text="Start",
                             font=("Arial", 12),
                             command=Typer().start,
                             bg="#4caf50",
                             fg="white",
                             bd=0,
                             padx=20,
                             pady=10)
    start_button.pack(side="left", padx=10)

    exit_button = tk.Button(button_frame,
                            text="Exit",
                            font=("Arial", 12),
                            command=root.destroy,
                            bg="#f44336",
                            fg="white",
                            bd=0,
                            padx=20,
                            pady=10)
    exit_button.pack(side="right", padx=10)

    typer = Typer()
    root.bind('<Key>', typer.on_key)
    root.mainloop()


if __name__ == "__main__":
    start_program()
