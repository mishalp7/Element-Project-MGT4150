# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# allows us to access the random function
import random
from time import sleep

# declare variables
playAgain = True
correctInput = True
tie = False
win = False
randVal = 0
compSelect = ""
userSelect = ""
countWater = 0
countFire = 0
countEarth = 0
countAir = 0
countLight = 0
countLosses = 0
countWins = 0

print("Welcome to the battle of the elements! Choose your element and see if you are the avatar!")
print("Rules of the game:\n Waterbender beats Firebender and Airbender.\n Firebender beats Airbender and "
      "Lightningbender.\n Airbender beats Earthbender and Lightningbender.\n Earthbender beats Waterbender and "
      "Firebender.\n Lightningbender beats Earthbender and Waterbender.")

# while loop to allow user to play as many times as they like
while playAgain:

    # determine the random value for computer

    randVal = random.randint(0, 0)

    # ask for the users choice
    print("Please enter what type of bender you are and see if you win!")
    # make sure the user input a valid selection
    userSelect = input()

    # count
    if userSelect == "Waterbender":
        countWater = countWater + 1
        countFire = 0
        countEarth = 0
        countAir = 0
        countLight = 0
    elif userSelect == "Firebender":
        countWater = 0
        countFire = countFire + 1
        countEarth = 0
        countAir = 0
        countLight = 0
    elif userSelect == "Earthbender":
        countWater = 0
        countFire = 0
        countEarth = countEarth + 1
        countAir = 0
        countLight = 0
    elif userSelect == "Airbender":
        countWater = 0
        countFire = 0
        countEarth = 0
        countAir = countAir + 1
        countLight = 0
    elif userSelect == "Lightningbender":
        countWater = 0
        countFire = 0
        countEarth = 0
        countAir = 0
        countLight = countLight + 1

    # print(countWater, countFire, countAir, countEarth, countLight)

    if userSelect == "Waterbender" or userSelect == "Firebender" or userSelect == "Earthbender" or userSelect == "Lightningbender" or userSelect == "Airbender":
        correctInput = True
    else:
        print("Please enter a correct choice.")
        playAgain = True
        correctInput = False

    # don't let them choose the same bender three times in a row
    if countWater == 3:
        print("You ran out of water bending. Please choose another option.")
        correctInput = False
    elif countFire == 3:
        print("You ran out of fire bending. Please choose another option.")
        correctInput = False
    elif countAir == 3:
        print("You ran out of air bending. Please choose another option.")
        correctInput = False
    elif countEarth == 3:
        print("You ran out of earth bending. Please choose another option.")
        correctInput = False
    elif countLight == 3:
        print("You ran out of lightning bending. Please choose another option.")
        correctInput = False

    if countWater == 4 or countFire == 4 or countAir == 4 or countEarth == 4 or countLight == 4:
        print("CAN YOU NOT READ!?!?")
        correctInput = False

    if countWater == 5 or countFire == 5 or countAir == 5 or countEarth == 5 or countLight == 5:
        print("PLEASE!!! SELECT ANOTHER OPTION!")
        correctInput = False

    if countWater == 6 or countFire == 6 or countAir == 6 or countEarth == 6 or countLight == 6:
        print("You have not followed directions. Goodbye!")
        correctInput = False
        playAgain = False

    # give the computer their choice
    if randVal == 0:
        compSelect = "Waterbender"
    elif randVal == 1:
        compSelect = "Firebender"
    elif randVal == 2:
        compSelect = "Earthbender"
    elif randVal == 3:
        compSelect = "Lightningbender"
    elif randVal == 4:
        compSelect = "Airbender"

    # mess with the results

    # decide the winner
    if correctInput is True:
        print("User chose", userSelect)
        sleep(1)
        print("Computer chose", compSelect)

        # determine who won
        if userSelect == compSelect:
            sleep(.5)
            print('You tied')
            tie = True
            win = False
        elif (userSelect == "Waterbender" and compSelect == "Lightningbender") or (
                userSelect == "Waterbender" and compSelect == "Earthbender") or (
                userSelect == "Earthbender" and compSelect == "Airbender") or (
                userSelect == "Earthbender" and compSelect == "Lightningbender") or (
                userSelect == "Firebender" and compSelect == "Waterbender") or (
                userSelect == "Firebender" and compSelect == "Earthbender") or (
                userSelect == "Airbender" and compSelect == "Firebender") or (
                userSelect == "Airbender" and compSelect == "Waterbender") or (
                userSelect == "Lightningbender" and compSelect == "Airbender") or (
                userSelect == "Lightningbender" and compSelect == "Firebender"):
            # print("You lost! :(")
            countLosses = countLosses + 1
            countWins = 0
            tie = False
            win = False
        elif (userSelect == "Waterbender" and compSelect == "Firebender") or (
                userSelect == "Waterbender" and compSelect == "Airbender") or (
                userSelect == "Earthbender" and compSelect == "Waterbender") or (
                userSelect == "Earthbender" and compSelect == "Firebender") or (
                userSelect == "Firebender" and compSelect == "Lightningbender") or (
                userSelect == "Firebender" and compSelect == "Airbender") or (
                userSelect == "Airbender" and compSelect == "Earthbender") or (
                userSelect == "Airbender" and compSelect == "Lightningbender") or (
                userSelect == "Lightningbender" and compSelect == "Earthbender") or (
                userSelect == "Lightningbender" and compSelect == "Waterbender"):
            # print("You won! :)")
            countLosses = 0
            countWins = countWins + 1
            tie = False
            win = True

        # give the user output depending on if they won and what they choose
        if win is True:
            if userSelect == "Waterbender" and compSelect == "Firebender":
                print("Your defensive waterbending snuffs any attacks from the Firebender, giving you an opening to attack against a defenseless opponent.")
            elif userSelect == "Waterbender" and compSelect == "Airbender":
                print("Due to air containing water, the Airbenders offensive and defensive attempts only act to provide an avenue to attack.")
            elif userSelect == "Firebender" and compSelect == "Lightningbender":
                print("Due to your diligent studies in Firebending and the movements of Waterbenders, you are able to redirect any lightning sent your way and add even more inertia to it.")
            elif userSelect == "Firebender" and compSelect == "Airbender":
                print("The Airbender has only managed to supply your flames with more oxygen, increasing your offensive abilities.")
            elif userSelect == "Earthbender" and compSelect == "Firebender":
                print("You understand that Firebenders only have offensive abilities, so by using your strong defense to nullify their attacks, their only option is to surrender.")
            elif userSelect == "Earthbender" and compSelect == "Waterbender":
                print("Your strong defense has managed to block all attacks, forcing the waterbender to be on the defensive and eventually overwhelming them.")
            elif userSelect == "Airbender" and compSelect == "Earthbender":
                print("No matter their efforts the Earthbender is unable to overwhelm your ability to divert their attacks.")
            elif userSelect == "Airbender" and compSelect == "Lightningbender":
                print("Using your knowledge of lightning, you understand that your opponent will be unable to produce enough static friction from with air by pulling the air away from them.")
            elif userSelect == "Lightningbender" and compSelect == "Earthbender":
                print("Your knowledge of the fact that Earthbenders must have a strong connection to the ground continuously in order to bend, making them act as a ground to your lightning.")
            elif userSelect == "Lightningbender" and compSelect == "Waterbender":
                print("While a Waterbender is a formidable opponent all around, your lightning will pass through any of their water-based attacks or defensive moves.")
        elif win is False:
            if compSelect == "Waterbender" and userSelect == "Firebender":
                print("The fire you have bended has been smothered, leading to water surrounding you and your fire.")
            elif compSelect == "Waterbender" and userSelect == "Airbender":
                print("While airbending is very versatile, the Waterbender is capable of attacking you with the water content in the air you bend.")
            elif compSelect == "Firebender" and userSelect == "Lightningbender":
                print("The lightning you have bended towards the Firebender has been redirected towards you.")
            elif compSelect == "Firebender" and userSelect == "Airbender":
                print("The air you bended has only managed to add more energy to the fire, engulfing you in flames.")
            elif compSelect == "Earthbender" and userSelect == "Firebender":
                print("The fire you have bended was blocked by the strong defense of the Earthbender, resulting in your offensive abilities being insufficient.")
            elif compSelect == "Earthbender" and userSelect == "Waterbender":
                print("The water you have bended was blocked by the Earthbender, resulting in your bending being nulled.")
            elif compSelect == "Airbender" and userSelect == "Earthbender":
                print("The earth that you have bended was redirected through airflow by the Airbender.")
            elif compSelect == "Airbender" and userSelect == "Lightningbender":
                print("The Airbender has used airflow to affect the polarity and static friction in the air, resulting in you being unable to bend lightning.")
            elif compSelect == "Lightningbender" and userSelect == "Earthbender":
                print("Due to the earth you use acting as a ground for the lightning, your earthbending has only acted to provide a pathway for the electricity to reach you.")
            elif compSelect == "Lightningbender" and userSelect == "Waterbender":
                print("Due to the conductivity of water, the Lightning will pass through your water and strike you.")

    # give rude output if user wins or loses
    if tie is False and correctInput is True:
        sleep(.5)
        if countWins == 1:
            print("You won! :)")
        if countWins == 2:
            print("You won ... again...")
        if countWins == 3:
            print("Seriously? You won again?")
        if countWins == 4:
            print("Fine. I'm done playing with you.")
            correctInput = False
            playAgain = False

        if countLosses == 1:
            print("You lost. :(")
        if countLosses == 2:
            print("You lost again.")
        if countLosses == 3:
            print("You are not a very good bender.")
        if countLosses == 4:
            print("I'm getting bored. Game over.")
            correctInput = False
            playAgain = False

        # allow the user to decide if they want to play again
        playAgain = input("Would you like to play again (Y or N)?").upper() == "Y"
