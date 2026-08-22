attempts=0
import random
secret_number=random.randint(1,50)
while True:
  guess=int(input("Enter a random number:"))
  attempts+=1
  if guess==secret_number:
    print("Correct")
    print("You got it in",attempts,"tries")
    break
  elif guess<secret_number:
    print("Too low")
  else:
    print("Too high")
  if attempts==10:
    print("Game Over!the number was",secret_number)
    break
