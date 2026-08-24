# Number Guessing Game

# Requirements:

# Secret number hardcoded rakho (e.g. 7)
# User guess kare
# Agar guess sahi:
# You Win!

# aur game end.

# Agar guess galat:
# Try Again
# while loop use karo.
# break use karo.
# Pseudocode First

# Sirf:

# 1.secret number hardcoded hoga user number guess krai ga
# 2.while loop mai condition i gi user guess number == secret nunber print you win loop khatam 
# 3.else no guess again

secret_number = 7
attempt = 1

while True:
    guess_number = int(input("Enter Your Number: "))

    if attempt <= 3:
        if guess_number != secret_number:
            print("Try Again!")``
            print(f"Attempt {attempt}")
        else:
            print("You Win!")
            break
    else:
        print("Game Over!")
        break    


    attempt = attempt + 1
