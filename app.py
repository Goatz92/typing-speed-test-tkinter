import tkinter as tk
from tkinter import ttk
import time
import random

class TypingSpeedTest:
    def __init__(self):
        # Initialize main window
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")

        # Initialize variable
        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is the art of telling another human what one wants the computer to do.",
            "Life is like riding a bicycle. To keep your balance, you must keep moving.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts."
        ]
        self.current_text = ""
        self.start_time = None
        self.is_test_active = False

        # Ui elements
        self.create_widgets()

    def create_widgets(self):
        instructions = "Type the text below as fast and accurately as you can!"
        self.instruction_label = tk.Label(
            self.root,
            text=instructions,
            font=("Helvetica", 12)
        )
        self.instruction_label.pack(pady=10)

        # Text to type
        self.text_to_type = tk.Label(
            self.root,
            text="Press 'Start Test' to begin",
            wraplength=700,
            font=("Helvetica", 14),
            bg="#f0f0f0",
            pady=10
        )
        self.text_to_type.pack(pady=20, padx=20, fill=tk.X)

        # Text input area
        self.text_input = tk.Text(
            self.root,
            height=5,
            font=("Helvetica", 12),
            state='disabled',
            wrap=tk.WORD
        )
        self.text_input.pack(pady=20, padx=20, fill=tk.X)

        # Stats
        stats_frame = ttk.Frame(self.root)
        stats_frame.pack(pady=10)

        self.wpm_label = tk.Label(
            stats_frame,
            text="WPM: 0",
            font=("Helvetica", 12)
        )
        self.wpm_label.pack(side=tk.LEFT, padx=10)

        self.accuracy_label = tk.Label(
            stats_frame,
            text="Accuracy: 0%",
            font=("Helvetica", 12)
        )
        self.accuracy_label.pack(side=tk.LEFT, padx=10)

        self.time_label = tk.Label(
            stats_frame,
            text="Time: 0s",
            font=("Helvetica", 12)
        )
        self.time_label.pack(side=tk.LEFT, padx=10)

        # Start button
        self.start_button = ttk.Button(
            self.root,
            text="Start Test",
            command=self.start_test
        )
        self.start_button.pack(pady=20)

    def start_test(self):
        pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TypingSpeedTest()
    app.run()