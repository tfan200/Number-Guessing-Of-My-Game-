import random
print("Welcome To My Number Guessing Game!")
YourMum = random.randint(1,10) 
 
chances = 0 
print("Guess a number from 1-10!")

#Make A Freaking Loop Noob!!

while chances < 5: 
    guess = int(input("Enter Your Guess"))
    if guess == YourMum:
        print ("Congrats!, i will spend that many Days with your mum!")
        break
    elif guess < YourMum:
        print("The Guess Is small like your pe...", guess)
    else: 
        print("Your guess very big like my pe...")
        break
    chances += 1
if not chances < 5: 
    print("You are a loser, i hope you die, i hope you were never born. PLS JUSR DIE ALREADY. You were a mistake! Your parents made a freaking mistake") 