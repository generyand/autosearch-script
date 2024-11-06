import tkinter as tk
from tkinter import ttk
import threading
from src.phrase_generator import PhraseGenerator
from src.typing_simulator import TypingSimulator
import time

class AutoTyperGUI:
    def __init__(self, master):
        self.master = master
        master.title("Auto Typer")
        master.geometry("400x480")  # Slightly increased height to accommodate the credit
        
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.configure_styles()
        self.create_widgets()

    def configure_styles(self):
        # Configure custom styles
        self.style.configure("TLabel", font=("Helvetica", 10), padding=5)
        self.style.configure("TEntry", font=("Helvetica", 10), padding=5)
        self.style.configure("TButton", font=("Helvetica", 10, "bold"), padding=10)
        self.style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), padding=10)
        self.style.configure("Status.TLabel", font=("Helvetica", 10), padding=10)
        self.style.configure("Credit.TLabel", font=("Helvetica", 8), padding=5, foreground="gray")

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Header
        ttk.Label(main_frame, text="Auto Typer", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Initial Delay
        ttk.Label(main_frame, text="Initial Delay (seconds):").grid(row=1, column=0, sticky=tk.W)
        self.initial_delay = ttk.Entry(main_frame, width=15)
        self.initial_delay.grid(row=1, column=1, pady=5, sticky=tk.E)
        self.initial_delay.insert(0, "5")

        # Phrase Count
        ttk.Label(main_frame, text="Phrase Count:").grid(row=2, column=0, sticky=tk.W)
        self.phrase_count = ttk.Entry(main_frame, width=15)
        self.phrase_count.grid(row=2, column=1, pady=5, sticky=tk.E)
        self.phrase_count.insert(0, "10")

        # Windows Open
        ttk.Label(main_frame, text="Windows Open:").grid(row=3, column=0, sticky=tk.W)
        self.windows_open = ttk.Entry(main_frame, width=15)
        self.windows_open.grid(row=3, column=1, pady=5, sticky=tk.E)
        self.windows_open.insert(0, "2")
        self.windows_open.bind("<KeyRelease>", self.update_recommended_delay)

        # Delay Between Windows
        ttk.Label(main_frame, text="Delay Between Windows (s):").grid(row=4, column=0, sticky=tk.W)
        self.delay_between_windows = ttk.Entry(main_frame, width=15)
        self.delay_between_windows.grid(row=4, column=1, pady=5, sticky=tk.E)
        self.delay_between_windows.insert(0, "3.0")

        # Recommended Delay Label
        self.recommended_delay_label = ttk.Label(main_frame, text="Recommended: 3.0")
        self.recommended_delay_label.grid(row=5, column=0, columnspan=2, pady=(5, 20))

        # Start Button
        self.start_button = ttk.Button(main_frame, text="Start Typing", command=self.start_typing)
        self.start_button.grid(row=6, column=0, pady=(0, 20))

        # Stop Button
        self.stop_button = ttk.Button(main_frame, text="Stop Typing", command=self.stop_typing, state="disabled")
        self.stop_button.grid(row=6, column=1, pady=(0, 20))

        # Status Label
        self.status_label = ttk.Label(main_frame, text="Ready", style="Status.TLabel")
        self.status_label.grid(row=7, column=0, columnspan=2)

        # Credit Label
        credit_label = ttk.Label(main_frame, text="Made by Exploiter ni Sah", style="Credit.TLabel")
        credit_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))

        # Configure grid weights
        for i in range(9):  # Increased to 9 to accommodate the credit label
            main_frame.rowconfigure(i, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def update_recommended_delay(self, event=None):
        try:
            windows = int(self.windows_open.get())
            recommended_delay = round(6 / windows, 2)
            self.recommended_delay_label.config(text=f"Recommended: {recommended_delay}")
            self.delay_between_windows.delete(0, tk.END)
            self.delay_between_windows.insert(0, str(recommended_delay))
        except ValueError:
            pass

    def start_typing(self):
        # Disable the start button, enable the stop button, and update status
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.status_label.config(text="Typing in progress...")

        # Reset the stop flag
        self.stop_flag.clear()

        # Get values from entries
        initial_delay = float(self.initial_delay.get())
        phrase_count = int(self.phrase_count.get())
        delay_between_windows = float(self.delay_between_windows.get())
        windows_open = int(self.windows_open.get())

        # Start typing in a separate thread
        self.typing_thread = threading.Thread(target=self.run_typing_simulation, args=(
            initial_delay, phrase_count, delay_between_windows, windows_open))
        self.typing_thread.start()

    def stop_typing(self):
        if self.typing_thread and self.typing_thread.is_alive():
            self.stop_flag.set()
            self.status_label.config(text="Stopping...")
            self.stop_button.config(state="disabled")

    def run_typing_simulation(self, initial_delay, phrase_count, delay_between_windows, windows_open):
        phrase_generator = PhraseGenerator()
        typing_simulator = TypingSimulator()

        time.sleep(initial_delay)

        for _ in range(phrase_count):
            if self.stop_flag.is_set():
                break
            for _ in range(windows_open):
                if self.stop_flag.is_set():
                    break
                phrase = phrase_generator.generate_phrase()
                typing_simulator.type_phrase(phrase)
                typing_simulator.alt_tab()
                time.sleep(delay_between_windows)

        # Re-enable the start button, disable the stop button, and update status
        self.master.after(0, self.update_ui_after_completion)

    def update_ui_after_completion(self):
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.status_label.config(text="Typing completed!" if not self.stop_flag.is_set() else "Typing stopped.")
        self.stop_flag.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperGUI(root)
    root.mainloop()
