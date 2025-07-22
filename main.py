import random  # Importujeme modul random pro generování náhodných čísel

# Funkce pro vypsání úvodní zprávy
def print_intro():
    print("Hi there!")  # Přivítání
    print("-" * 47)  # Oddělovač (47 pomlček)
    print("I've generated a random 4 digit number for you.")  # Info o vygenerování čísla
    print("Let's play a bulls and cows game.")  # Pozvání ke hře
    print("-" * 47)  # Oddělovač

# Funkce pro vygenerování tajného 4místného čísla s unikátními ciframi, nezačínající nulou
def generate_secret_number():
    digits = list("123456789")  # Seznam číslic, které mohou být na první pozici (bez nuly)
    first_digit = random.choice(digits)  # Náhodně vybereme první číslici (není 0)
    digits.remove(first_digit)  # Odebereme ji, abychom ji znovu nepoužili

    remaining_digits = list("0123456789")  # Všechny číslice (včetně 0) pro zbývající pozice
    remaining_digits.remove(first_digit)  # Odebereme první číslici, už ji máme
    # Vybereme 3 unikátní číslice pro zbytek čísla a spojíme s první číslicí
    secret = first_digit + ''.join(random.sample([d for d in remaining_digits if d != first_digit], 3))
    return secret  # Vracíme vygenerované tajné číslo jako řetězec

# Funkce pro ověření správnosti uživatelského vstupu
def is_valid_guess(guess):
    if not guess.isdigit():  # Kontrola, jestli jsou všechny znaky číslice
        print("Invalid input: Not a number.")  # Chybová zpráva
        return False
    if len(guess) != 4:  # Kontrola délky čísla
        print("Invalid input: Must be exactly 4 digits.")  # Chybová zpráva
        return False
    if guess[0] == '0':  # Kontrola, zda číslo nezačíná nulou
        print("Invalid input: Number cannot start with 0.")  # Chybová zpráva
        return False
    if len(set(guess)) != 4:  # Kontrola duplicity (musí být 4 různé číslice)
        print("Invalid input: Digits must be unique.")  # Chybová zpráva
        return False
    return True  # Vstup je platný

# Funkce pro vyhodnocení bull/cow výsledku
def evaluate_guess(secret, guess):
    # Bull = správná číslice na správném místě
    bulls = sum(s == g for s, g in zip(secret, guess))  # Porovnáváme tajné číslo a tip pozici po pozici
    # Cow = správná číslice, ale na špatném místě
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls  # Počet společných číslic minus bulls
    return bulls, cows  # Vrátíme počet bulls a cows

# Funkce pro správné zformátování výsledku (1 cow vs 2 cows atd.)
def format_feedback(bulls, cows):
    bull_str = f"{bulls} bull{'s' if bulls != 1 else ''}"  # Přidá "s" pokud není přesně 1 bull
    cow_str = f"{cows} cow{'s' if cows != 1 else ''}"  # Přidá "s" pokud není přesně 1 cow
    return f"{bull_str}, {cow_str}"  # Vrací výsledek ve formátu "x bulls, y cows"

# Hlavní funkce, která řídí průběh hry
def play_game():
    print_intro()  # Vypíšeme úvodní text
    secret = generate_secret_number()  # Vygenerujeme tajné číslo
    attempts = 0  # Počítadlo pokusů

    while True:  # Nekonečný cyklus – bude se opakovat, dokud hráč neuhodne
        print("-" * 47)  # Oddělovač
        guess = input("Enter a number:\n>>> ").strip()  # Vyzveme uživatele a odstraníme mezery kolem

        if not is_valid_guess(guess):  # Pokud není vstup validní, začneme další iteraci
            continue

        attempts += 1  # Zvětšíme počet pokusů o 1
        bulls, cows = evaluate_guess(secret, guess)  # Vyhodnotíme tip

        if bulls == 4:  # Hráč uhodl celé číslo správně
            print(f"Correct, you've guessed the right number\nin {attempts} guess{'es' if attempts != 1 else ''}!")  # Oznámení výhry
            print("-" * 47)  # Oddělovač
            print("That's amazing!")  # Gratulace
            break  # Ukončíme hru
        else:
            print(format_feedback(bulls, cows))  # Vypíšeme počet bulls a cows

# Spuštění hlavní funkce, pokud je soubor spuštěn jako hlavní skript
if __name__ == "__main__":
    play_game()  # Spuštění hry