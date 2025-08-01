print ("WELCOME TO THE GUESSING GAME!!!")
num = 60
guess = 0
trial = 0
while trial <= 5 :
     guessnum = int(input("Guess a number between 1 - 100 :"))
     guess == guessnum
     if guessnum == num :
         print(f"HURRAH YOU WON THE GAME YOUR GUESS {guessnum} IS CORRECT !!!")
         break
     elif guessnum < num :
         print("WRONG YOUR GUESS IS TOO LOW TRY AGAIN")
         trial = trial + 1
        
     elif guessnum > num :
        print ("WRONG YOUR GUESS IS TOO HIGH TRY AGAIN")
        trial = trial + 1
while trial >= 5 :
     print(f"YOU LOSE THE CORRECT NUMBER IS {num}")
     break
        