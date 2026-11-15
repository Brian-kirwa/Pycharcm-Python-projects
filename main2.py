#Rock paper Scissors game
import random

emojis={"rock":"🪨","paper":"📃","scissor":"✂️"}
choices=tuple(emojis.keys())

computer_choice = random.choice(choices)

is_running = True
while is_running:
    print("rock, paper, scissor")
    choice = input("Enter your choice (rock, paper, or scissor):").lower()
    if choice == "rock" and computer_choice == "paper":
        print("you loose!")
        print(f"Computer chose: {emojis[computer_choice]} and your chose: {emojis[choice]}")
    elif choice == "paper" and computer_choice == "scissor":
        print("you loose!")
        print(f"Computer chose: {emojis[computer_choice]} and your chose: {emojis[choice]}")
    elif choice == "scissor" and computer_choice == "rock":
        print("you loose!")
        print(f"Computer chose: {emojis[computer_choice]} and your chose: {emojis[choice]}")
    elif choice==computer_choice:
        print("It's a tie")
        print(f"Computer chose: {emojis[computer_choice]} and your chose: {emojis[choice]}")
    elif choice not in choices:
        print("Invalid choice")

    else:
        print("your Win!")
        print(f"Computer chose: {emojis[computer_choice]} and your chose: {emojis[choice]}")
    should_continue=input("Do your want to play again?(y/n)").lower()
    if should_continue=="n":
        is_running=False
    elif should_continue=="y":
        continue
    else:
        print("Invalid choice!!Enter y to continue or n to quit.")
print("Thank you for playing")

