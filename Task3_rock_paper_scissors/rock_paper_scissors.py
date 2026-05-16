import random

# Display game title

print("===== Rock Paper Scissors Game =====")

# Store scores

user_score = 0
computer_score = 0

# Run game until user quits

while True:
    print("\nChoose one option:")
    print("1. rock")
    print("2. paper")
    print("3. scissors")

    # Take user input and convert to lowercase
    
    user_choice = input("\nEnter your choice: ").lower()

    # Possible choices for computer
    
    options = ["rock","paper","scissors"]

    # Computer selects randomly
    
    computer_choice = random.choice(options)
    print("\nYour choice:", user_choice)
    print("Computer choice:",computer_choice)

  # Check if both choices are same
   
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    # Conditions where user wins
    
    elif ((user_choice == "rock"and computer_choice == "scissors")or(user_choice == "paper"and computer_choice == "rock")or(user_choice == "scissors"and computer_choice == "paper")):

        print("Result: You Win!")
        user_score += 1

    # If user input is valid but user loses
    
    elif user_choice in options:
        print("Result: Computer Wins!")
        computer_score += 1

    # Invalid input handling
    
    else:
        print("Invalid choice. Try again.")
        continue

    # Display current scores

    print("\n===== Score Board =====")
    print("Your Score:",user_score)
    print("Computer Score:",computer_score)

    # Ask user if they want another round
    
    play_again = input("\nPlay again? (yes/no): ").lower()

    # Stop game if user enters anything except yes
    
    if play_again != "yes":
        print("\n===== Game Over =====")
        print("Final Score")
        print("You:",user_score)
        print("Computer:",computer_score)
        print("\nThanks for playing!")
        break