import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Add maximum attempts limit
    
    while attempts < max_attempts:
        try:
            remaining = max_attempts - attempts
            print(f"\nYou have {remaining} attempts remaining.")
            
            # Ask user for a guess
            guess = int(input("Enter your guess (1-100): "))
            
            # Validate input range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
                
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nGame Over! The number was {number_to_guess}")
    return False

if __name__ == "__main__":
    number_guessing_game()

