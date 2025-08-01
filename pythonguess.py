print ("WELCOME TO THE GUESSING GAME!!!")
num = 60
trial = 0
max_trial = 5
while trial < 5 :
     guessnum = int(input("Guess a number between 1 - 100 :"))
     if guessnum == num :
         print(f"HURRAH YOU WON THE GAME YOUR GUESS {guessnum} IS CORRECT !!!")
         break
     elif guessnum < num :
         print("WRONG YOUR GUESS IS TOO LOW TRY AGAIN")
         trial = trial + 1
     else :
        print ("WRONG YOUR GUESS IS TOO HIGH TRY AGAIN")
        trial = trial + 1
if trial == max_trial and guessnum != num :
     print(f"YOU LOSE THE CORRECT NUMBER IS {num}")
        