from random import randint

def run_guess(guess,ran_num):
    if guess == ran_num:
        print("You guessed it !!!")
        return False
    else:
        print("Bad Guess. Let's try again")
        return True
if(__name__=='__main__'):
    ran_num = randint(1, 10)
    flag = True
    while flag:
        try:
            guess = int(input("Guess a number between 1 and 10 :"))
            if 0 < guess < 11:
                flag = run_guess(guess,ran_num)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a Number between 1 and 10")
