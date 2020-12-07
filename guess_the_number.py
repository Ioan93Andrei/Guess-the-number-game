import random

def gameOn():
    random_number = random.randrange(0, 1000)
    chosen_number = int(input("Please pick a number: "))
    while True:
        if chosen_number == 1000 or chosen_number <= 0 :
            print("Number must be below 1000 and above 0.")
            print(random_number)
            chosen_number = int(input("Please pick a number: "))
            continue
        if chosen_number > random_number:
            print("Too high")
            chosen_number = int(input("Please pick a number: "))
        elif chosen_number < random_number: 
            print("Too low")
            chosen_number = int(input("Please pick a number: "))
        else:
            print("Congratulations, you guessed right. The number was " + str(chosen_number) + ".")
            answer = input("Do you want to play again? Y/N ")

            if answer in("Y", "y", 'yes'):
                print("Restarting game!")
                gameOn()
            else:
                print("Goodbye")
            break

gameOn()