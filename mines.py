import random

# Size of grid (adjust as needed)
n = 5

# Number of mines (adjust as needed)
mines_no = 5

# The actual values of the grid (initialize with zeros)
numbers = [[0 for y in range(n)] for x in range(n)]

# The apparent values of the grid (initialize with spaces)
mine_values = [[' ' for y in range(n)] for x in range(n)]

# Function for setting up mines randomly
def set_mines():
    for _ in range(mines_no):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        while numbers[row][col] == 'M':
            row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        numbers[row][col] = 'M'

# Printing the Minesweeper Layout
def print_mines_layout():
    print("\t\t\tSTAKE MINES\n")
    header = "   " + "     ".join(str(i + 1) for i in range(n))
    print(header)
    for r in range(n):
        row_line = "     "
        if r == 0:
            row_line += "______" * n
            print(row_line)
        row_line = "     "
        for col in range(n):
            row_line += f"|  {mine_values[r][col]}  "
        print(row_line + "|")
        row_line = f"  {r + 1}  "
        for col in range(n):
            row_line += f"|  {numbers[r][col]}  "
        print(row_line + "|")
        row_line = "     "
        row_line += "|_____" * n
        print(row_line + '|')
    print()

if __name__ == "__main__":
    set_mines()
    print_mines_layout()
              
