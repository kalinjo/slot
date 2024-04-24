import random

MAX_LINES = 3                          
MAX_BET = 1000                         
MIN_BET = 1                            

ROWS = 3
COLS = 3

symbol_count = {                       
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {                       
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}



def deposit():                          
    while True:
        amount = input("Place your deposit!(Minimum $1) $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

    return amount


def get_num_of_lines():                 
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


def get_bet():                            
        while True:
            amount = input(f"What would you like to bet?({MIN_BET} - {MAX_BET}) $")
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
    
    columns = []                                         
    for _ in range(cols):                                
        column = []                 
        current_symbols = all_symbols[:]                 
        for _ in range(rows):                            
            value = random.choice(current_symbols)       
            current_symbols.remove(value)                
            column.append(value)                         

        columns.append(column)  
                            
    return columns


def print_slot(columns):
    for row in range(len(columns[0])):                  
        for i, column in enumerate(columns):            
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end = "")            

        print()


def check_win(columns, lines, bet, values):             
    winnings = 0            
    winning_lines = []                                  
    for line in range(lines):                           
        symbol = columns[0][line]                          
        for column in columns:                          
            symbol_to_check = column[line]              
            if symbol != symbol_to_check:               
                break
        else:                                           
            winnings += values[symbol] * bet             
            winning_lines.append(lines)                 

    return winnings, winning_lines                      


def spin(balance):                                      
    lines = get_num_of_lines()                          
    while True:
        bet = get_bet()                                 
        total_bet = bet * lines                         

        if total_bet > balance:                         
            print(f"Insufficient funds! Please add money to your balance. Your current ballance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines", * winning_lines)         
    return winnings - total_bet                         

    #print(balance, lines)


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")     
        answer = input("Press ENTER to play or Q to quit!" )        
        if answer == "q" :                                           
            break        
        if answer == "Q" :
            break                         
        balance += spin(balance)                    

    print(f"You left with ${balance}")              

main()





