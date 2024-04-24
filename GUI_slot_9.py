import tkinter as tk
import random

class SlotMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")
        self.root.geometry("300x300")

        self.deposit = tk.IntVar()
        self.deposit.set(1)

        self.bet_amount = tk.IntVar()
        self.bet_amount.set(1)

        self.bet_lines = tk.IntVar()
        self.bet_lines.set(1)

        self.result = tk.StringVar()
        self.result.set("")

        self.reels = tk.StringVar()
        self.reels.set("")

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.root.title("Welcome to Slot Machine")

        tk.Label(self.root, text="Welcome to Slot Machine!").pack()
        tk.Label(self.root, text="Please enter your deposit:").pack()
        tk.Entry(self.root, textvariable=self.deposit).pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack()

    def start_game(self):
        if self.deposit.get() < 1:
            self.result.set("Deposit must be greater than 0.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.create_game_screen()

    def create_game_screen(self):
        self.root.title("Slot Machine")

        tk.Label(self.root, text="Current Deposit:").pack()
        tk.Label(self.root, textvariable=self.deposit, text="$" + str(self.deposit.get())).pack()

        tk.Label(self.root, text="Bet Amount:").pack()
        tk.Entry(self.root, textvariable=self.bet_amount).pack()

        tk.Label(self.root, text="Bet Lines (1-3):").pack()
        tk.Entry(self.root, textvariable=self.bet_lines).pack()

        tk.Button(self.root, text="Spin", command=self.spin).pack()

        tk.Label(self.root, textvariable=self.reels).pack()
        tk.Label(self.root, textvariable=self.result).pack()

    def spin(self):
        if self.bet_amount.get() < 1 or self.bet_amount.get() > self.deposit.get():
            self.result.set(f"Invalid bet amount. Please enter a value between 1 and ${self.deposit.get()}.")
            return

        if self.bet_lines.get() < 1 or self.bet_lines.get() > 3:
            self.result.set("Invalid number of bet lines. Please enter a value between 1 and 3.")
            return

        if self.bet_amount.get() * self.bet_lines.get() > self.deposit.get():
            self.result.set("Insufficient funds. Please deposit more money.")
            return

        self.deposit.set(self.deposit.get() - self.bet_amount.get() * self.bet_lines.get())

        symbols = ["A", "B", "C", "D", "E", "F", "G"]
        symbol_values = {"A": 2, "B": 3, "C": 4, "D": 5, "E": 6, "F": 7, "G": 8}
        slots = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]

        reels = "\n".join([" ".join(row) for row in slots])
        self.reels.set(reels)

        for i in range(self.bet_lines.get()):
            if len(set(slots[i])) == 1:
                symbol = slots[i][0]
                win_amount = self.bet_amount.get() * symbol_values[symbol]
                self.result.set(f"You won on line {i+1}! Three {symbol} in a row!\nYou won ${win_amount}!")
                self.deposit.set(self.deposit.get() + win_amount)
                return

        self.result.set("You lost. Try again.")

root = tk.Tk()
app = SlotMachine(root)
root.mainloop()
