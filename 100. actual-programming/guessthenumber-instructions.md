## How It Works

### Step 1: Import the random module

```python
import random
```

This lets Python generate random numbers.

---

### Step 2: Pick a random number

```python
secret_number = random.randint(1, 10)
```

`random.randint(1, 10)` picks a whole number from **1 through 10**.

For example, it might choose:

```
3
```

or

```
9
```

The player doesn't know what number was chosen.

---

### Step 3: Give instructions

```python
print("Welcome to Guess the Number!")
print("I am thinking of a number between 1 and 10.")
```

These messages tell the player what to do.

---

### Step 4: Create a starting guess

```python
guess = 0
```

We set `guess` to `0` so the loop has a value to compare before the player enters anything.

---

### Step 5: Repeat until correct

```python
while guess != secret_number:
```

This loop keeps running as long as the guess is **not** the secret number.

---

### Step 6: Ask for input

```python
guess = int(input("Enter your guess: "))
```

* `input()` reads what the user types.
* `int()` converts it from text to a whole number.

---

### Step 7: Give a hint

```python
if guess < secret_number:
    print("Too low!")

elif guess > secret_number:
    print("Too high!")

else:
    print("You guessed it!")
```

* If the guess is too small, the program says **"Too low!"**
* If it's too big, it says **"Too high!"**
* Otherwise, the guess must be correct.

---

## A Fun Challenge for Students

Once students finish this version, ask them to add one feature at a time:

1. Count how many guesses the player takes.
2. Let the player choose the maximum number (for example, 1–100).
3. Give the player only 5 guesses.
4. Ask if they want to play again.
5. Keep track of their best (fewest) number of guesses.

These extensions reinforce the same core concepts without introducing too much new syntax at once.
