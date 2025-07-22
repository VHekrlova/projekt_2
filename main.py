import random  
import time

def print_intro():
    """"Vypise uvodni zpravu"""
    print("Hi there!")  
    print("-" * 47)  
    print("I've generated a random 4 digit number for you.")  
    print("Let's play a bulls and cows game.")  
    print("-" * 47) 


def generate_secret_number():
    """Vygeneruje 4mistny tajny kod"""
    first_digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first_digit = random.choice(first_digits)
    remaining_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    remaining_digits.remove(first_digit)
    other_digits = random.sample(remaining_digits, 3)
    secret_number = first_digit + other_digits[0] + other_digits[1] + other_digits[2]

    return secret_number 


def is_valid_guess(guess):
    """Overi platny vstup"""
    if not guess.isdigit():
        print("Invalid input: Not a number.") 
        return False

    if len(guess) != 4:
        print("Invalid input: Must be exactly 4 digits.")  
        return False

    if guess[0] == "0":
        print("Invalid input: Number cannot start with 0.")  
        return False

    unique_digits = set(guess)
    if len(unique_digits) != 4:
        print("Invalid input: Digits must be unique.") 
        return False

    return True 

def evaluate_guess(secret, guess):
    """Vyhodnoti pocer bulls a cows"""
    bulls = 0  
    cows = 0   

    for i in range(4):  
        if guess[i] == secret[i]:
            bulls += 1  
        elif guess[i] in secret:
            cows += 1  

    return bulls, cows  


def format_feedback(bulls, cows):
    """Vystup"""
    if bulls == 1:
        bull_str = "1 bull"
    else:
        bull_str = f"{bulls} bulls"

    if cows == 1:
        cow_str = "1 cow"
    else:
        cow_str = f"{cows} cows"
    return f"{bull_str}, {cow_str}"

def play_game():
    """Spusti hru"""
    print_intro()  

    secret = generate_secret_number()  
    attempts = 0
    start_time = time.time()  

    while True: 
        print("-" * 47)
        guess = input("Enter a number:\n>>> ")  

        guess = guess.strip()  

        if not is_valid_guess(guess):
            continue  

        attempts += 1  

        bulls, cows = evaluate_guess(secret, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number")
            if attempts == 1:
                print("in 1 guess!")  
            else:
                print(f"in {attempts} guesses!")  
            print("-" * 47)  
            print("That's amazing!")

            end_time = time.time()
            duration = end_time - start_time
            minutes = int(duration // 60)
            seconds = int(duration % 60)
            print(f"You solved it in {minutes} minute(s) and {seconds} second(s)!") 
            break  

        else:        
            feedback = format_feedback(bulls, cows)
            print(feedback)

if __name__ == "__main__":
    play_game()
    