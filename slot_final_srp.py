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
        amount = input("Uplatite depozit $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Vrednost mora biti veca od 0.")
        else: 
            print("Molimo upisite broj.")

    return amount


def get_num_of_lines():                 #Funkcija odredjuje broj linija na koje se kladimo
    while True:
        lines = input("Unesite broj linija na koje se kladite (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Unesite validan broj linija.")
        else: 
            print("Molimo unesite broj.")

    return lines


def get_bet():                            #Funkcija odredjuje koliki ce biti uloga po liniji
        while True:
            amount = input("Koliko zelite da ulozite? $")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(F"Vrednost mora biti izmedju ${MIN_BET} - ${MAX_BET}.")
            else: 
                print("Molimo unesite broj.")

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


def spin(balance):                                      #f-ja definise jedno vrtenje slot masine
    lines = get_num_of_lines()                          #
    while True:
        bet = get_bet()                                 #uzima ulog po liniji
        total_bet = bet * lines                         #ukupno ulozenog novca na svim linijama

        if total_bet > balance:                         #petlja koja nece dozvoliti da se igrac kladi u slucaju nedovoljno srestava na balansu
            print(f"Nedovoljno sredstava! Molimo dodajte novac na racun. Trenutno stanje Vaseg racuna je: ${balance}")
        else:
            break
        
    print(f"Ulozili ste ${bet} na ${lines} linije. Ukupna vrednost uloga: ${total_bet}")
    
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
        print(f"Na vasem stanju se nalazi ${balance}")     #ispisivanje balansa racuna igracu
        answer = input("Pritisnite ENTER za nastavak ili Q za izlaz!" )        #poruka igracu, kako da nastavi igru ili prekine
        if answer == "q":                                           
            break                                   #prekid igre
        balance += spin(balance)                    #update balansa racuna, na osnovu svakog odigranog spina

    print(f"Napustili se igru sa ${balance}")              #poslednja poruka koja se ispisuje po napustanju igre

main()