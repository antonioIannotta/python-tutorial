secret_word = "giraffe"
guess = ""
number_attempts = 0
limits = 3
out_of_guesses = False

while guess != secret_word and out_of_guesses.__eq__(False):
    if number_attempts < limits:
        guess = input("Enter guess: ")
        number_attempts += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("You win!")
