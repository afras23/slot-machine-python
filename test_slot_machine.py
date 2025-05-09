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
