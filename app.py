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
        # Reset and start new test
        self.is_test_active = True
        self.current_text = random.choice(self.sample_texts)
        self.text_to_type.config(text=self.current_text)
        self.text_input.config(state='normal')
        self.text_input.delete('1.0', tk.END)
        self.start_time = time.time()
        
        # Reset stats
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 0%")
        self.time_label.config(text="Time: 0s")
        
        # Start timer
        self.update_timer()
        
        # Bind the key release event
        self.text_input.bind('<KeyRelease>', self.check_progress)
    
    def update_timer(self):
        if self.is_test_active and self.start_time:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text=f"Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)
    
    def check_progress(self, event=None):
        if not self.is_test_active:
            return
            
        # Get current input
        current_input = self.text_input.get('1.0', 'end-1c')
        
        # Calculate current statistics
        self.calculate_stats(current_input)
        
        # Check if test is complete
        if current_input == self.current_text:
            self.finish_test()
    
    def calculate_stats(self, current_input):
        # Calculate accuracy
        correct_chars = sum(1 for i, c in enumerate(current_input) 
                          if i < len(self.current_text) and c == self.current_text[i])
        accuracy = (correct_chars / len(self.current_text)) * 100 if self.current_text else 0
        
        # Calculate WPM (time in minutes)
        elapsed_time = time.time() - self.start_time
        minutes = elapsed_time / 60
        word_count = len(current_input.split()) if current_input else 0
        wpm = int(word_count / minutes) if minutes > 0 else 0
        
        # Update labels
        self.wpm_label.config(text=f"WPM: {wpm}")
        self.accuracy_label.config(text=f"Accuracy: {accuracy:.1f}%")
    
    def finish_test(self):
        self.is_test_active = False
        self.text_input.config(state='disabled')
        self.text_input.unbind('<KeyRelease>')
        self.start_button.config(text="Try Again")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TypingSpeedTest()
    app.run()