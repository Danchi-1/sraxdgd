"""
Exercise: Simple Number Guessing Game
Objective: Create a simple number guessing game where the user has to guess a secret number between 1 and 10.

Instructions:
Set Up the Secret Number:

Use a variable to store a secret number (e.g., secret_number = 7).
Ask for User Input:

Use the input() function to ask the user to guess the number. Convert the input to an integer.
Check the Guess:

Use an if statement to check if the user's guess matches the secret number.
If the guess is correct, print a congratulatory message.
If the guess is incorrect, use an else statement to print a message saying the guess is wrong.
Add a Loop for Multiple Guesses:

Use a for loop to allow the user to guess up to 3 times.
If the user guesses correctly within 3 attempts, print a success message and exit the loop.
If the user fails to guess correctly after 3 attempts, print a message revealing the secret number.

Example Output:
Guess the secret number (between 1 and 10): 5
Wrong guess! Try again.
Guess the secret number (between 1 and 10): 7
Congratulations! You guessed the secret number!
"""
secret_number = 5
for attempt in range(3):
    player_input = int(input("Guess is the secret number "))
    if player_input == secret_number:
        print("Congratulations! You have got the secret number")
        break
    else:
        print("You did not get the secret the secret number")
    print(f"The right answer is {secret_number}")