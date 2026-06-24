

## How it works

### Step 1: Create the board

```python
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
```

Think of the board like this:

```
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

Each list position stores either:

* `" "` (empty)
* `"X"` (player)
* `"O"` (computer)

---

### Step 2: Print the board

The `print_board()` function simply displays the list in a Tic-Tac-Toe shape.

---

### Step 3: Check for a winner

The `check_winner(player)` function checks:

* all 3 rows
* all 3 columns
* both diagonals

If any of them contain three of the same symbol, it returns `True`.

---

### Step 4: Player turn

```python
move = int(input("Choose a spot (1-9): ")) - 1
```

The user types a number from **1–9**.

We subtract 1 because Python lists start at **0**, not **1**.

---

### Step 5: Computer turn

First, we make a list of every empty square.

```python
empty_spots = []

for i in range(9):
    if board[i] == " ":
        empty_spots.append(i)
```

For example, if the board looks like

```
X | O | X
---------
  | O |
---------
X |   |
```

then

```python
empty_spots
```

would become

```python
[3, 5, 7, 8]
```

---

Then the computer randomly chooses one.

```python
computer_move = random.choice(empty_spots)
```

If `empty_spots` is

```python
[3, 5, 7, 8]
```

the computer might choose

```python
7
```

or

```python
5
```

or any of the others.

---

### Step 6: Repeat

The loop

```python
for turn in range(9):
```

runs at most **9 times**, because there are only 9 squares.

After every move, the program checks if someone has won. If nobody wins after all 9 turns, it's a tie.

---

This version intentionally avoids advanced ideas like classes, dictionaries, or complex AI so that a beginner can understand it after learning just:

* variables
* lists
* `for` loops
* `if` statements
* functions
* `random.choice()`
* user input
