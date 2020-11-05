import random

random_number = random.randrange(0, 500)
chosen_number = int(float(input("Please pick a number: ")))

while chosen_number != random_number:
    print(chosen_number)

    if chosen_number > 500:
        print ("Number must be below 500.")
        break
    else:
      if chosen_number > random_number:
          print("Too high")
          chosen_number = int(float(input("Please pick a number: ")))
      elif chosen_number < random_number: 
          print("Too low")
          chosen_number = int(float(input("Please pick a number: ")))
          print ("Congratulations, you guessed right. The number was " + str(chosen_number))
          break

print("Goodbye")
  