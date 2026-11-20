# match case statements are introduced in python 3.10. It is similar to switch case statements in other programming languages. It is used to match the value of a variable with a case and execute the code block associated with that case.


# a = int(input("Enter a value for a:\n "))

# match a:
#     case 1:
#         print("The value of a is 1.")
#     case 2:
#         print("The value of a is 2.")
#     case 55:
#         print("The value of a is 55.")
#     case _:
#         print("The value of a is not defined in the cases.")


# Example simple guess the number and win the price:

num = int(input("Guess the number between 1 to 90:\n "))

match num:
    case 1:
        print("You guessed very basic, still will give you 10$ as a prize.")
    case 66:
        print("You have WON!! the jackpot prize of 1,00,000$.")
    case 90:
        print("You guessed the last number, you will get 100$ as a prize.")
    case _:
        print("Sorry, you have guessed the wrong number... pay us $10 for the next chance to win the prize.")

is_playing = int(input("Do you want to play again?:\n Enter '1' for Yes \n '0' for No:\n "))

if is_playing == 0:
    print("Thank you for playing the game. Have a nice day!")
elif is_playing == 1:
    num = int(input("Guess the number between 1 to 90:\n "))
    match num:
        case 1:
            print("You guessed very basic, still will give you 10$ as a prize.")
        case 66:
            print("You have WON!! the jackpot prize of 1,00,000$.")
        case 90:
            print("You guessed the last number, you will get 100$ as a prize.")
        case _:
            print("Sorry, you have guessed the wrong number... pay us $10 for the next chance to win the prize.")
else:
    print("You have entered an invalid input. Please enter '1' for Yes or '0' for No.")