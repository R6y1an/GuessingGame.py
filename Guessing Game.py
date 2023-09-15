from random import randint

guessNumber=int(input("Enter your guess between 1 to 100:"))
randomNumber=randint(1,100)

if guessNumber==randomNumber:
    print("You have won")
else:
    print("You have loss") 
    print("Random number was:,randomNumber")   

