secret = 9

guess = None

while guess != secret:
    guess = int(input("Guess the number: "))
    
    if guess != secret:
        print("Wrong! Try again.")

print("Correct! You guessed it.")