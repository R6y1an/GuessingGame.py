from random import randint

guessNumber=int(input("Enter your guess between 1 to 10:"))
randomNumber=randint(1,10)

if guessNumber==randomNumber:
    print("You have won")
else:
    print("You have loss") 
    print("Random number was:,randomNumber")   

