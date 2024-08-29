import random

def get_top_of_range():
    while True:
        top_of_range = input("Type a number: ")
        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            if top_of_range > 0:
                return top_of_range
            else:
                print("Your number should be larger than zero.")
        else:
            print("Please type a valid number.")

b = get_top_of_range()

random_number = random.randint(0, b)

while True:
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == random_number:
            print("You win!")
            break
        else:
            print("It is wrong, try again.")
    else:
        print("Please enter a valid number.")
