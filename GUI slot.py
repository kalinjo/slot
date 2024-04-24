import tkinter as tk
import random

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")

        # Create labels and buttons
        self.result_label = tk.Label(root, text="Spin the reels!", font=("Arial", 16))
        self.result_label.pack(pady=20)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin_reels)
        self.spin_button.pack()

    def spin_reels(self):
        # Simulate spinning the reels (you can replace this logic with your own)
        symbols = ["🍒", "🔔", "🍊", "🍀", "💎"]
        result = [random.choice(symbols) for _ in range(3)]

        # Update the result label
        self.result_label.config(text=f"{' '.join(result)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()