# Python Calculator Walkthrough

In this walkthrough, we will create a simple calculator in Python.

The calculator will:

* Add two numbers
* Subtract two numbers
* Multiply two numbers
* Divide two numbers
* Find the remainder using modulo (`mod`)

## Step 1: Create a Function

First, we will create a function called `calculator`.

A function is a block of code that performs a specific task.

```python
def calculator(num1, num2, operation):
```

Our function takes in three pieces of information:

* `num1` — the first number
* `num2` — the second number
* `operation` — tells us what calculation to perform

## Step 2: Add the Addition Logic

We want to check if the user wants to add the two numbers.

We can use an `if` statement:

```python
if operation == "add":
    return num1 + num2
```

This means:

> If the operation is `"add"`, add the two numbers and return the answer.

The `return` statement sends the answer back from the function.

## Step 3: Add the Subtraction Logic

Next, we can check if the operation is `"subtract"`.

```python
elif operation == "subtract":
    return num1 - num2
```

`elif` means "else if."

This means:

> If the operation is `"subtract"`, subtract the second number from the first number.

## Step 4: Add the Multiplication Logic

Next, add multiplication:

```python
elif operation == "multiply":
    return num1 * num2
```

The `*` symbol is used for multiplication in Python.

## Step 5: Add the Division Logic

Next, add division:

```python
elif operation == "divide":
    return num1 / num2
```

The `/` symbol is used for division in Python.

## Step 6: Add the Modulo Logic

Finally, add modulo:

```python
elif operation == "mod":
    return num1 % num2
```

The `%` symbol is called the modulo operator.

It gives you the remainder after division.

For example:

```text
10 % 3 = 1
```

This is because 10 divided by 3 has a remainder of 1.

## Step 7: Handle an Invalid Operation

What if the user types an operation that our calculator does not understand?

We can use an `else` statement:

```python
else:
    return "Invalid operation"
```

This tells the program to return `"Invalid operation"` if none of the previous conditions were true.

## Step 8: Get the First Number

Now that we have created our function, we need to get information from the user.

We can ask the user for the first number:

```python
num1 = float(input("Enter the first number: "))
```

`input()` allows the user to type something.

`float()` converts the user's input into a number that can include decimals.

For example:

```text
10
10.5
3.14
```

## Step 9: Get the Second Number

Next, ask the user for the second number:

```python
num2 = float(input("Enter the second number: "))
```

Now we have two numbers stored in `num1` and `num2`.

## Step 10: Get the Operation

Next, ask the user which operation they want to perform:

```python
operation = input("Enter the operation (add, subtract, multiply, divide, mod): ")
```

The user can type one of the following:

```text
add
subtract
multiply
divide
mod
```

The operation they enter will be stored in the variable `operation`.

## Step 11: Call the Function

Now we can use our calculator function:

```python
result = calculator(num1, num2, operation)
```

This sends our three pieces of information to the function:

* The first number
* The second number
* The operation

The answer returned by the function is stored in the variable `result`.

## Step 12: Print the Result

Finally, we can display the answer:

```python
print("Result:", result)
```

This prints the word `"Result:"` followed by the answer.

## Step 13: Put Everything Together

Your complete program should look like this:

```python
def calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "mod":
        return num1 % num2
    else:
        return "Invalid operation"


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide, mod): ")

result = calculator(num1, num2, operation)

print("Result:", result)
```

## Step 14: Test Your Program

Run the program and enter:

```text
Enter the first number: 10
Enter the second number: 3
Enter the operation (add, subtract, multiply, divide, mod): add
```

The program should output:

```text
Result: 13.0
```

Try testing the other operations as well:

```text
subtract → 7.0
multiply → 30.0
divide → 3.3333333333333335
mod → 1.0
```

Congratulations! You have created a Python calculator that uses a function, `if` statements, user input, and basic mathematical operators.
