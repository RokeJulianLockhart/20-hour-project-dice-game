import random
import os

p1Score = 0
p2Score = 0
same = True
name1 = ""
name2 = ""

def diceRoll():  #the function generates 2 dice rolls and if they are equal adds a third then the total is checked and if it is even then it adds 10 more to the total otherwise it removes 5 point from the total
  dice1 = random.randint(1, 6)  #rolls dice no.1
  dice2 = random.randint(1, 6)  #rolls dice no.2
  dice3 = random.randint(1, 6)  #rolls dice no.3
  if dice1 == dice2:  #checks if dice 1 and 2 are equal
    total = dice1 + dice2 + dice3  #adds dice 3 if so
  else:
    total = dice1 + dice2  #if not adds dice 1 and 2
  if total == -5 or total == -3 or total == -1 or total == 1 or total == 3 or total == 5 or total == 7 or total == 9 or total == 11 or total == 13 or total == 15 or total == 17 or total == 19 or total == 21 or total == 23 or total == 25 or total == 27 or total == 29:  #checks if total is odd
    finalTotal = total - 5  #minuses 5 if odd
  else:
    finalTotal = total + 10  #adds 10 if even
  return (finalTotal)  #returns the total

givenUsername1 = str(input("Player 1 enter your user: "))
givenPassword1 = str(input("Player 1 enter your password: "))
f = open("logins.txt","r")
endOfFile = False
while not endOfFile:
  username = f.readline().strip()
  password = f.readline().strip()
  if givenUsername1 == username and givenPassword1 == password:
    login = True
  else:
    print("Incorrect details.")
    raise SystemExit(0)
  if username == "":
    endOfFile = True
givenUsername2 = str(input("Player 2 enter your user: "))
givenPassword2 = str(input("Player 2 enter your password: "))
f = open("logins.txt","r")
endOfFile = False
while not endOfFile:
  username = f.readline().strip()
  password = f.readline().strip()
  if givenUsername2 == username and givenPassword2 == password:
    login = True
  elif givenUsername1 != username or givenPassword1 != password:
    print("incorrect details")
    raise SystemExit(0)
  if username == "":
    endOfFile = True
os.system("clear")
name1 = input("player 1 enter your preffered name ")
name2 = input("player 2 enter your preffered name ")
for i in range(0, 5): #For loop that loops this 5 times
  input("Player 1 press enter to roll your dices! ")
  os.system("clear") #clears the console
  score1 = diceRoll()
  if score1 < 0:
    score1 = 0
  p1Score = p1Score + score1
  print(name1,"you rolled", score1, "points!") #displays the points player 1 rolls
  print(name1,"has a score of ", p1Score, "points!") #displays player 1's total score
  print(name2,"has a score of ", p2Score, "points!") #displays player 2's total score
  input("Player 2 press enter to roll your dices! ")
  os.system("clear") #clears the console
  score2 = diceRoll()
  if score2 < 0:
    score2 = 0
  p2Score = p2Score + score2
  print(name2,"you rolled", score2, "points!") #displays the points player 2 rolls
  print(name1,"has a score of", p1Score, "points!") #displays player 1's total score
  print(name2,"has a score of", p2Score, "points!") #displays player 2's total score
if p1Score > p2Score:
  print(name1,"WINS!")
  input("Press enter to close program")
  os.system("clear") #clears the console
  raise SystemExit(0) #ends program
elif p2Score > p1Score:
  print(name2,"WINS!")
  input("Press enter to close program")
  os.system("clear")
  raise SystemExit(0) #ends program
else:
  while p1Score == p2Score:
    winningDice1 = random.randint(1, 6)
    winningDice2 = random.randint(1, 6)
    input("You both drew so now you will roll 1 die and highest wins!")
    print(name1,"rolled",winningDice1,)
    print(name2,"rolled",winningDice2,)
    if winningDice1 > winningDice2: #compares the winning dice
      print(name1,"WINS!")
      input("Press enter to close program")
      os.system("clear") #clears the console
      raise SystemExit(0) #ends program
    elif winningDice2 > winningDice1: #compares the winning dice
      print(name2,"WINS!")
      input("Press enter to close program")
      os.system("clear") #clears the console
      raise SystemExit(0) #ends program