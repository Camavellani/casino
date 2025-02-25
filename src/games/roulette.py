
from src.core.casino import player, admin
from src.ui.ui import player as ui

from random import seed
from random import randint

class roulette:

    def __int__(self, uid):
        self.player = player()
        self.admin = admin()
        self.uid = uid

    roulette = { # possible positions on the roulette table
        'g' : ['0'],
        'r': ['1','3','5','7','9','12','14','16','18','19','21','23','25','27','30','32','34','36'],
        'b': ['2','4','6','8','10','11','13','15','17','20','22','24','26','28','29','31','33','35']
        }
    bets = {
        'green':'g', 'red':'r', 'black':'b',
        'odd': ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31','33','35'],
        'even': ['2','4','6','8','12','14','16','18','20','22','24','26','28','30','32','34','36'],
        'high': ['19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36'],
        'low': ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'],
        'column1': ['1','4','7','10','13','16','19','22','25','28','31','34'],
        'column2': ['2','5','8','11','14','17','20','23','26','29','32','35'],
        'column3': ['3','6','9','12','15','18','21','24','27','30','33','36'],
        'num': list(roulette.keys()) # puts the dictionary in terms of a list
        }


    payout = { # payout 1 means that u make the money u put in, and 2 means u profit twice the amount u paid
        'red': 1,
        'black': 1,
        'odd' : 1,
        'even': 1,
        'high': 1,
        'low' : 1,
        'column1': 2,
        'column2': 2,
        'column3': 2,
        'num': 36
        }
    def getValue():
        global color
        number = str(randint(0, 36)) # Chooses a random number for the roulette to
        print(number)
        for key,value in roulette.items():#  iteration over the dictionary 
            if number in value:
                color = key
        return  color, number
    def moneyWon(betAmount, bet):
        print("Congratulations you have won")
        bail = (payout.get(bet)) 
        money = (bail*betAmount)
        self.admin.addWinnings(self.uid, money)
        self.admin.addGame("Roulette", self.uid, money)
        print(f"You earned: {money}, your balance is now {self.player.getWinnings(self.uid)}")
        print(money)
        ui(self.uid)
        return(money)
        #return payout * betAmount
    def moneyLost(betAmount):
        self.admin.addWinnings(self.uid, betAmount)
        self.admin.addGame("Roulette", self.uid, betAmount)
        print(f"You have lost {betAmount}, your balance is now {self.player.getWinnings(self.uid)}")
        ui(self.uid)

    def didYouWin(winningColor, winningNumber, betOption, userPick,betAmount):#using option need compare the value of the option with the values in the key of the bet dictionary
     print(betOption)
     winningBets = []
     winningBets = [key
                    for key, list_of_values in bets.items ()
                    if winningNumber in list_of_values]
     print(winningBets)
     if(betOption == '1'):
        if(list(bets.keys())[list(bets.values()).index(winningColor)]) == userPick: #put the keys and values of the bets dictionary into lists, which helps show if the bet and actual value/color are the same
               print(list(bets.keys())[list(bets.values()).index(winningColor)]) #prints the winning color
               return moneyWon(betAmount,userPick) # returns the payout
        else:
             moneyLost(betAmount)
     elif(betOption == '2'):
         if winningNumber == userPick:
             return moneyWon(betAmount, userPick)
         else:
             moneyLost(betAmount)
     elif(betOption == '3'):
        print(userPick)
        i = 0
        for x in range(len(winningBets)):
            if(userPick == winningBets[x]):
                i+=1
        if(i<1):
                moneyLost(betAmount)
        else:
                return moneyWon(betAmount,userPick)

     elif(betOption == '4'):
        print(userPick)
        i = 0
        for x in range(len(winningBets)):
            if(userPick == winningBets[x]):
                i+=1
        if(i<1):
                moneyLost(betAmount)
        else:
                return moneyWon(betAmount,userPick)
     elif(betOption == '5'):
        print(userPick)
        i = 0
        for x in range(len(winningBets)):
            if(userPick == winningBets[x]):
                i+=1
        if(i<1):
                moneyLost(betAmount)
        else:
                return moneyWon(betAmount,userPick)
     else:
         print("This bet doesn't exist.Please try again")
         return 5

    Option = True
    goThrough = True
    nonValidMoney = True
    nonValidbet = True
    game_in_session = True 
    print("Welcome to the Roulette table")
    while game_in_session:
        while goThrough:
            print(""" What bet would you like to make. The options are below
            Option 1: Bet on color, red, black, green
            Option 2: Bet on exact number. Please enter a number from 0-36
            Option 3: Bet on high or low
            Option 4: Bet on even or odd
            Option 5: column1, column2, and column3 """)
            Option = input("Please enter your option : ")
            if Option not in ["1","2","3","4","5"]: # Checking to see if the user puts in an adeqaute option
                print("Please input a valid number")
            else:
                goThrough = False
        while nonValidMoney: # checks to see if the bettor is inputing an integer or an adequate number and not chars
            raw_bet = input("How much would you like to wager $: ")
            try: 
                bet = int(raw_bet)
                assert bet > 0
                nonValidMoney = False
            except:
                print("Wrong Input. Please Enter a number")
        while nonValidbet:
                userPick = input("What bet would you like to pick: ")
                if Option == "1":
                    if userPick not in ["red","black","green"]:
                        print("please input a valid color. No uppercase")
                    else:
                        nonValidbet = False
                elif Option == "2":
                    print("1-36")
                    num = int(userPick)
                    if num not in range(0,37):
                        print("Please put a number between 0-36 ")
                    else:
                        nonValidbet = False
                elif Option == "3":
                    if userPick not in ["high", "low"]:
                        print("Please put low or high")
                    else:
                        nonValidbet = False
                elif Option == "4":
                    if userPick not in ['even', 'odd']:
                        print("Please put even or odd")
                    else:
                        nonValidbet = False
                elif Option == "5":
                    if userPick not in ["column1", "column2", "column3"]:
                        print("Please input column1, column2 or column3")
                    else:
                        nonValidbet = False

        #highOption = "Low"
        print("The game is now in session/ No more bets")
        winningColor, winningValue  = getValue()
        print(winningValue)
        print(winningColor)
        didYouWin(winningColor, winningValue, Option, userPick, bet)
        keepPlaying=input("Woud you like to keep playing:")
        print(keepPlaying)
        if keepPlaying == "yes" or "Yes":
            print(keepPlaying)
            game_in_session = True
            Option = True
            goThrough = True
            nonValidMoney = True
            nonValidbet = True
        else:
            game_in_session = False

if __name__ == "__main__":
    roulette()

   
   
    #put the user interface into class
    
    #print (winningColor)
# now need functions to be able to play the game.
# need a random number Generator function
# function that finds if the bet is a winning bet
#functions that returns a payout