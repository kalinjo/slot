import tkinter as tk
import random

MAX_LINES = 3                          #Zadavanje konstanti - maksimum linija na koje se moze kladiti
MAX_BET = 1000                         #                    - maksimalna uplata
MIN_BET = 1                            #                    - minimalna uplata

ROWS = 3
COLS = 3

symbol_count = {                       #dictionary, simbol string, broj simbola u svakom okretanju
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {                       #dictionary, vrednost simbola - kvota
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}



def deposit():                          #Funkcija dodaje novac za kladjenje
    while True:
        amount = input("Place your deposit! $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

    return amount


def get_num_of_lines():                 #Funkcija odredjuje broj linija na koje se kladimo
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines.")
        else: 
            print("Please enter a number.")

    return lines


def get_bet():                            #Funkcija odredjuje koliki ce biti uloga po liniji
        while True:
            amount = input("What would you like to bet? $")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(F"Amount must be between ${MIN_BET} - ${MAX_BET}.")
            else: 
                print("Please enter a number.")

        return amount


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []                                         #definisemo listu kolona
    for _ in range(cols):                                #generisemo kolonu medju kolonama
        column = []                 
        current_symbols = all_symbols[:]                 #trenutni simboli = kopija svih simbola
        for _ in range(rows):                            #loop kroz broj simbola koje treba generisati = broj redova 
            value = random.choice(current_symbols)       #uzima random vrednost iz liste
            current_symbols.remove(value)                #brise izabranu vrednost kako ne bi bila ponovo izabrana
            column.append(value)                         #dodaje izabranu vednost u kolonu

        columns.append(column)  
                            
    return columns


def print_slot(columns):
    for row in range(len(columns[0])):                  #prolazimo kroz svaki red koji imamo u raange-u kolona kojih ima minimum 1
        for i, column in enumerate(columns):            
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end = "")            #za svaku kolonu printamo trenutni red na kom se nalazimo

        print()


def check_win(columns, lines, bet, values):             #f-ja proverava da li ima pogodaka
    winnings = 0            
    winning_lines = []                                  #kreiranje prazne liste *1
    for line in range(lines):                           #proveravamo da li je svaki simbol u redu isti tj. prolazimo kroz svaki red i proveravamo opklade
        symbol = columns[0][line]                       #provera prvog simbola u odredjenom redu, i provera da li su preostali simboli isti       
        for column in columns:                          #proverom prvog simbola od ranije, prolazimo kroz svaku kolonu u potrazi za tim simbolom
            symbol_to_check = column[line]              
            if symbol != symbol_to_check:               #proveravamo da li su simboli razliciti, ako nisu - ide break, i proverava se sledeca linija(red)
                break
        else:                                           
            winnings += values[symbol] * bet            #ako su simboli u redu isti, racuna se pogodak i kolicina osvojenog novca 
            winning_lines.append(lines)                 #dodavanje pogodaka u gore kreiranu praznu listu *1

    return winnings, winning_lines                      #vraca dve vrednosti, kolicinu osvojenog novca + na kojim redovima smo ostvarili win

class SlotMachineGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine")

        # Initialize player's deposit (you can replace this with your own logic)
        self.deposit = 100

        # Initialize the bet amount
        self.bet_amount = MIN_BET

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Deposit label
        self.deposit_label = tk.Label(self.root, text=f"Deposit: ${self.deposit}")
        self.deposit_label.pack()

        # Bet amount label and entry
        self.bet_label = tk.Label(self.root, text="Bet Amount:")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(self.root)
        self.bet_entry.pack()
        self.bet_entry.insert(0, str(self.bet_amount))

        # Spin button
        self.spin_button = tk.Button(self.root, text="Spin", command=self.spin)
        self.spin_button.pack()

        # Result label
        self.result_label = tk.Label(self.root, text="Good luck!", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def spin(self):
        # Get the bet amount
        bet = self.bet_entry.get()
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                self.bet_amount = bet
            else:
                self.result_label.config(text=f"Bet must be between ${MIN_BET} and ${MAX_BET}")
                return
        else:
            self.result_label.config(text="Please enter a valid bet amount")
            return

        # Simulate the slot spin (you can replace this logic with your own)
        all_symbols = []
        for symbol, count in symbol_count.items():
            all_symbols.extend([symbol] * count)

        columns = []
        for _ in range(COLS):
            column = random.sample(all_symbols, ROWS)
            columns.append(column)

        # Display the result
        result_text = '\n'.join([' '.join(column) for column in zip(*columns)])
        self.result_label.config(text=result_text)

        # Placeholder for updating the deposit after the spin
        # self.deposit -= self.bet_amount
        # self.deposit_label.config(text=f"Deposit: ${self.deposit}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineGUI(root)
    root.mainloop()













def spin(balance):                                      #f-ja definise jedno vrtenje slot masine
    lines = get_num_of_lines()                          #
    while True:
        bet = get_bet()                                 #uzima ulog po liniji
        total_bet = bet * lines                         #ukupno ulozenog novca na svim linijama

        if total_bet > balance:                         #petlja koja nece dozvoliti da se igrac kladi u slucaju nedovoljno srestava na balansu
            print(f"Insufficient funds! Please add money to your balance. Your current ballance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines", * winning_lines)         #splat operator - stampa redove u kojima smo pobedili. 1 u slucaju jednog pogotka, ili vise u slucaju pogodaka u vise linija
    return winnings - total_bet                         #vraca vrednost - kolicinu novca u slucaju pogotka tj. kolicinu izgubljenog novca po opkladi 

    #print(balance, lines)


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")     #ispisivanje balansa racuna igracu
        answer = input("Press ENTER to play or Q to quit!" )        #poruka igracu, kako da nastavi igru ili prekine
        if answer == "q":                                           
            break                                   #prekid igre
        balance += spin(balance)                    #update balansa racuna, na osnovu svakog odigranog spina

    print(f"You left with ${balance}")              #poslednja poruka koja se ispisuje po napustanju igre

main()