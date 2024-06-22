import random as rn
import math

upper=int(input("Enter the upper limit:"))
lower=int(input("Enter the lower limit:"))

number=rn.randint(lower,upper)
chances=round(math.log(upper-lower+1,2))
count=0
fnd=False

print(f"You have got {chances} chances to guess the number!!!")
while count<chances:
    guess=int(input("Guess a number:"))
    if guess==number:
        fnd=True
        print(f"Bravooo!!! You guessed the number in {count+1} chances")
    elif guess<number:
        print(f"Go higher\nYou are left with {chances-(count+1)}")
    else:
        print(f"Go lower\nYou are left with {chances-(count+1)}")
    count+=1

if count>=chances and fnd==False:
    print(f"The number was {number}\nYou didn't guess the number in the given {chances} chances :(\nBetter luck next time")