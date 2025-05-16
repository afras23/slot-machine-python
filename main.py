import random


# Constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


class SlotMachine:
    def __init__(self, rows, cols, symbols, values):
        self.rows = rows
        self.cols = cols
        self.symbols = symbols
        self.values = values

    def spin(self):
        all_symbols = [sym for sym, count in self.symbols.items() for _ in range(count)]
        columns = []
        for _ in range(self.cols):
            current_symbols = all_symbols[:]
            column = []
            for _ in range(self.rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns

    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            if all(column[line] == symbol for column in columns):
                winnings += self.values[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines

    @staticmethod
    def print_columns(columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                end_char = " | " if i != len(columns) - 1 else ""
                print(column[row], end=end_char)
            print()


class Player:
    def __init__(self, balance):
        self.balance = balance

    def get_bet_lines(self):
        while True:
            choice = input(f"How many lines would you like to bet on (1-{MAX_LINES})? ")
            if choice.isdigit():
                lines = int(choice)
                if 1 <= lines <= MAX_LINES:
                    return lines
            print(f"Please enter a valid number between 1 and {MAX_LINES}.")

    def get_bet_amount(self):
        while True:
            choice = input(f"How much do you want to bet on each line (£{MIN_BET} - £{MAX_BET})? ")
            if choice.isdigit():
                amount = int(choice)
                if MIN_BET <= amount <= MAX_BET:
                    return amount
            print(f"Enter a valid number between £{MIN_BET} and £{MAX_BET}.")

    def can_place_bet(self, total_bet):
        return self.balance >= total_bet

    def update_balance(self, amount):
        self.balance += amount


def get_deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Please enter a valid positive amount.")


def main():
    print("🎰 Welcome to the Python Slot Machine! 🎰\n")
    balance = get_deposit()
    player = Player(balance)
    machine = SlotMachine(ROWS, COLS, SYMBOL_COUNT, SYMBOL_VALUE)

    while True:
        print(f"\n💰 Current Balance: £{player.balance}")
        choice = input("Press [Enter] to play or type 'q' to quit: ").lower()
        if choice == 'q':
            break

        lines = player.get_bet_lines()
        bet = player.get_bet_amount()
        total_bet = bet * lines

        if not player.can_place_bet(total_bet):
            print(f"Insufficient funds. You need £{total_bet} but only have £{player.balance}.")
            continue

        print(f"\nSpinning... Betting £{bet} on {lines} lines. Total: £{total_bet}\n")
        slots = machine.spin()
        SlotMachine.print_columns(slots)

        winnings, winning_lines = machine.check_winnings(slots, lines, bet)
        net_gain = winnings - total_bet
        player.update_balance(net_gain)

        print(f"\n🎉 You won £{winnings}!")
        if winning_lines:
            print("Winning lines:", ", ".join(str(line) for line in winning_lines))
        else:
            print("No winning lines this round.")
        print(f"💼 Updated Balance: £{player.balance}")

    print(f"\nThanks for playing! You're leaving with £{player.balance} 🤑")


if __name__ == "__main__":
    main()
