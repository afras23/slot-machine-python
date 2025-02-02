import random

#HERE, WE DEFINE CONSTANTS. THERE IS NO CONST DATA TYPE IN PYTHON SO WE USE CAPITAL LETTERS AS CONVENTION - THESE VALUES CAN BE CHANGED
MAX_LINES = 3 
MIN_BET = 1
MAX_BET = 100

#BELOW WERE DESIGNING THE SLOT MACHINE ITSELF. 
#WE WILL ASSUME THE CLIENT WINS A LINE WHEN THEY GET 3 OF THE SAME SYMBOLS IN A ROW
ROW = 3
COL = 3

#EACH COLUMN WILL HAVE SYMBOLS,A ND EACH SYMBOL WILL JHAVE THEIR RESPECTIVE VALUES.
#THE SYMBILS NEED TO BE SELECTED AT RANDOM
#BELOW WE MAKE A DICTIONARY TO STORE OUR SYMBOLS

symbol_count = {
    #defines symbols and their count in each reel
    "A": 2, #e.g for each reel, we have 2 A symbols
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    #defines symbols and their respective values
    "A": 5, #e.g for each reel, we have 2 A symbols
    "B": 4,
    "C": 3,
    "D": 2
}

#now we will design a function to randomly generate the outcome of the slot machine based on symbol_count
#we need to generate what symbols will be in each column, based on the symbol_count dictionary above - need to randomly pick row values for each column
    #we will create a list containing all of the different values we could pissibly select, and randomly choose 3 of those values
    #once the values are chosen, they need to me removed from the list -  and choose again


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #looping through the lines the client has actually bet on
        #need to check that every symbol in the line client is betting on is the same
        symbol = columns[0][line] #need to access first column then check which line were on
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break #in this for else looop, if we break, the else statement doesnt run - if no break occurs within the for loop, the else statement executes
        else: #if we reach here then we got to the end of for loop without breaking and therefore all symbols are same therefore won
            winnings += values[symbol] * bet #the bet here is the bet on each line not the total bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(ROW, COL, symbols):
    all_symbols = [] #list
    #for loop to add symbols parm inputted in function, to the all_symbols list
    for symbol, symbol_count in symbols.items():#iterating through a dictionary --> .items() gives us both key and value associated with the dictionary
        for _ in range(symbol_count): #e.g adds A 2 times
            all_symbols.append(symbol)
    #now we need to select symbols that will go on each column

    columns = []#interiot of this list will be the values in our columns
    for _ in range(COL): # generate each column
        #for every column, we need to randomly generate values for each row in our column
        column = []
        #make a copy of all_symbols list so original one is unaffected
        current_symbols = all_symbols[:]
        for _ in range(ROW):
            value = random.choice(current_symbols)
            #one a certain value has been chosen, we should remove it from all_symbols list so we dont choose more than supposed to aka choose 3 As when theres only 2 in list 
            #.remove function will find the first instance of the value in the list, and remove it 
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    # Transposing the "columns" list so that rows appear vertically when printed.
    # Since "columns" is a nested list, each sublist represents a column.
    
    for row in range(len(columns[0])):  
        # The number of rows is determined by the number of elements in the first column.
        # We iterate over the row index to print each row separately.

        for i, column in enumerate(columns):  
            # Loop through each column. "enumerate" provides both the index (i) and the column (sublist).
            
            # Print the value at the current row index in each column.
            # Ensure the last column doesn't add an extra separator at the end.
            if i != len(columns) - 1:  
                print(column[row], "|", end=" ")  
                # The default end character is "\n" (new line), but here we use " " to stay on the same line.
            else:
                print(column[row], end="")  
                # No separator for the last column to keep formatting clean.

        print()  # Moves to the next line after printing all values in a row.

#function to collect bet amount from user
def deposit():
    #while loop to allow function to keep running till break - will ensure we get the correct values from the user
    while True:
        #here, by default, input function will return number as a string
        amount = input("How much would you like to deposit o start betting? £")

        if amount.isdigit(): #checks digits were inputted instead of characters
            #convert to int
            amount = int(amount)
            if amount > 0:
                break #stops the while loops and carry on in code
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    print("Thanks for depositing £", amount)
    return amount

#function below collects bet decision from the user
#logic: how much user wants to bet --> how many lines they want to bet on --> multiply bet by number of lines want to bet on
#first: ask how many lines they want to bet on
#second: ask how much they want to bet on each line

def get_number_of_lines():
    #number of lines will be between 1 and 3 as this matches the contraint for the number of columns
    # we also need a global constant, defined at top of code to set a constraint for number of lines
    #  logically, very similar to deposit() fucntion, just for lines instead
    while True:
        number_of_lines = input("How many lines would you like yo bet on (1 -" + str(MAX_LINES) + ")?")
        if  number_of_lines.isdigit(): #checks digits were inputted instead of characters
            #convert to int
            number_of_lines = int(number_of_lines)
            if 1 <= number_of_lines <= MAX_LINES:
                break
            else:
                print("Amount must be within specified range (1 -" + str(MAX_LINES)+ ")")
        else:
            print("Please enter a valid number.")

    print("You would like to bet on", number_of_lines)
    return number_of_lines

# function to get how much the user wants to bet on each line
def get_bet():
    while True:
        bet_amount = input("How much would you like to bet on each line? £")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between £{MIN_BET} and £{MAX_BET}.")
        else:
            print("Enter a valid number.")
    print(f"You will be betting £{bet_amount} on each line.")
    return bet_amount

#function to group operations that need to be done one after the other, rather than calling seperately everytime you qant to use the system

def spin(balance):
    #this executes one game for the purposes of repeating operations without having to rerun the program multiple times when operations need to be repeated aka rebetting on the same turn with remaining balance
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You dont have enough to bet that amount. Current Balance is {balance}")
        else:
            break
    print(f"You are betting £{bet} on {lines} lines. Total bet is £{total_bet}")
#once we detetmine what theyre betting, we can generate the slot machine
    slots = get_slot_machine_spin(ROW, COL, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won", winnings)
    print("You won on lines:", *winning_lines) # the astrix is the 'splat' or 'unpack' operator that passes every line from the winning_lines list to the print function
    return winnings - total_bet

def main():
    #we now want to be able to run this program mu;tiple times without having to press the run button 
    #balance will stay the same
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin_answer = input("Press enter to play (q to quit).")
        if spin_answer == 'q':
            break
        balance += spin(balance)

    print(f"You're left with ${balance}")

main()