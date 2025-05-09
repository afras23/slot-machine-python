
# Python Slot Machine 🎰

A terminal-based slot machine game built in Python. Players can deposit money, place bets on up to 3 lines, spin the reels, and win based on matching symbols. The game uses randomness, betting logic, and clean console output to simulate a real slot machine experience.

## Features

- Simulates a 3x3 slot machine
- Randomly spins symbols with weighted probability
- Betting system with configurable min/max limits
- Calculates winnings based on symbol values
- Real-time balance updates and multiple spins per session

---

## How to Run

1. Clone the repository or download the script.

```bash
git clone https://github.com/yourusername/slot-machine.git
cd slot-machine
python slot_machine.py
```

## Example Output

```pgsql
How much would you like to deposit o start betting? £100
How many lines would you like to bet on (1 -3)? 3
How much would you like to bet on each line? £10
You are betting £10 on 3 lines. Total bet is £30

A | B | C
C | D | A
B | C | D

You won 20
You won on lines: 2
```
## Tests

- Basic functional test to validate spin result dimensions and symbol constraints.

```python
from slot_machine import get_slot_machine_spin, symbol_count, ROW, COL

def test_slot_output_structure():
    spin = get_slot_machine_spin(ROW, COL, symbol_count)
    assert len(spin) == COL, "Number of columns is incorrect"
    for column in spin:
        assert len(column) == ROW, "Each column must have correct number of rows"
        for symbol in column:
            assert symbol in symbol_count, f"Unexpected symbol: {symbol}"
    print("All slot structure tests passed.")

if __name__ == "__main__":
    test_slot_output_structure()
```

---

### 🧪 `test_slot_machine.py`

```python
from slot_machine import get_slot_machine_spin, symbol_count, ROW, COL

def test_slot_output_structure():
    spin = get_slot_machine_spin(ROW, COL, symbol_count)
    assert len(spin) == COL, "Number of columns is incorrect"
    for column in spin:
        assert len(column) == ROW, "Each column must have correct number of rows"
        for symbol in column:
            assert symbol in symbol_count, f"Unexpected symbol: {symbol}"
    print("All slot structure tests passed.")

if __name__ == "__main__":
    test_slot_output_structure()
    ```
    
## Author

Anesah Fraser
