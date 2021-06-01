
import random
import time
cards = []
list = [2,3,4,5,6,7,8,9,10]
list2 = ["king","queen","jack","ace"]
list3 = ["king","queen","jack"]
bet = 0
bet1 = 0
mtot = 0

def Cprint(y):
    for i in list:
        cards.append(str(i) + " of " + y)
    for i in list2:
        cards.append(str(i) + " of " + y)
    return

spades = Cprint("spades")
hearts = Cprint("hearts")
diamonds = Cprint("diamonds")
clubs = Cprint("clubs")
repeat = 1
run = 0
while repeat == 1:
    while run == 0:
        run = -2
        phd = []
        dhd = []
        phd1 = []
        p1in = 0
        p2in = 0
        player1 = 1
        player2 = 1
        ptot = 0
        ptot1 = 0
        dtot = 0
        mtot = 0
        mtot1 = 0
        print ("___________________________")
        mtot = int(input("Welcome to BlackJack Player 1! Place your bet! The bet pot currently has " + str(bet) + " dollars!"))
        print (str(mtot) + " dollars have been put in the bet-pot!")
        bet = bet-mtot
        time.sleep(1)
        mtot1 = int(input("Welcome to BlackJack Player 2! Place your bet! The bet pot currently has " + str(bet1) + " dollars!"))
        print (str(mtot1) + " dollars have been put in the bet-pot!")
        bet1 = bet1- mtot1
        time.sleep(1)
        for i in range(2):
            phd.append(cards[random.randint(0,51)])
        for i in range(2):
            phd1.append(cards[random.randint(0,51)])
        for i in range(2):
            dhd.append(cards[random.randint(0,51)])
        ace=1
        def Pcount():
            global ptot
            for i in list:
                for x in range(2):
                    if str(i) in phd[x]:
                        ptot += i
            for i in list3:
                for x in range(2):
                    if str(i) in phd[x]:
                        ptot += 10
            for x in range(2):
                if "ace" in phd[x]:
                    ptot += ace
        def Pcount1():
            global ptot1
            for i in list:
                for x in range(2):
                    if str(i) in phd1[x]:
                        ptot1 += i
            for i in list3:
                for x in range(2):
                    if str(i) in phd1[x]:
                        ptot1 += 10
            for x in range(2):
                if "ace" in phd1[x]:
                    ptot1 += ace
        def Dcount():
            global dtot
            for i in list:
                for x in range(2):
                    if str(i) in dhd[x]:
                        dtot += i
            for i in list3:
                for x in range(2):
                    if str(i) in dhd[x]:
                        dtot += 10
            for x in range(2):  
                if "ace" in phd[x]:
                    dtot += ace
        Dcount()
        Pcount()
        Pcount1()
        print ("__________GAME BEGINS__________")
        time.sleep(0.5)
        p = input(">>>>>Player 1<<<<< you have been dealt the " + phd[0] + " and the " + phd[1] + ". Your number total is " + str(ptot) + ". Would you like the value of ace's to be 11 or 1?")
        if str(11) in p:
            ace = 11
            print ("The value of Ace's is now 11 for the rest of the game.")
            for i in range(2):
                if "ace" in phd[i]:
                    ptot += ace
                    ptot = ptot-1
            for i in range(2):
                if "ace" in dhd[i]:
                    dtot += ace
        else:
            print ("The value of Ace's is now 1 for the rest of the game.")
        time.sleep(1)
        loop = 0
        Cnew = 2
        while loop == 0:
            cont = input (">>>>>Player 1<<<<< your total is " + str(ptot) + ". Would you like to hit or stay?")
            if "hit" in cont:
                phd.append(cards[random.randint(0,51)])
                for i in list:
                    if str(i) in phd[Cnew]:
                        ptot += i
                for i in list3:
                    if str(i) in phd[Cnew]:
                        ptot += 10
                if "ace" in phd[Cnew]:
                    ptot += ace
                if ptot < 21:
                    print ("Your new card is " + phd[Cnew])
                    Cnew += 1
                if ptot > 21:
                    mtot = 0
                    print ("Sorry you lost your bet and busted! You drew the " + phd[Cnew] + ". It looks like you total was " + str(ptot) + ", which is greater than 21! You are now out of the round!")
                    time.sleep(5)
                    loop += 1
                    p1in = 1
                    run += 1
            elif "stay" in cont:
                loop += 1
        time.sleep(0.5)
        print (">>>>>Player 2<<<<< you have been dealt the " + phd1[0] + " and the " + phd1[1] + ". ")
        loop = 0
        Cnew = 2
        while loop == 0:
            cont = input (">>>>>Player 2<<<< your total is " + str(ptot1) + ". Would you like to hit or stay?")
            if "hit" in cont:
                phd1.append(cards[random.randint(0,51)])
                for i in list:
                    if str(i) in phd1[Cnew]:
                        ptot1 += i
                for i in list3:
                    if str(i) in phd1[Cnew]:
                        ptot1 += 10
                if "ace" in phd1[Cnew]:
                    ptot1 += ace
                if ptot1 < 21:
                    print ("Your new card is " + phd1[Cnew])
                    Cnew += 1
                if ptot1 > 21:
                    mtot1 = 0
                    print ("Sorry you lost your bet and busted! You drew the " + phd1[Cnew] + ". It looks like you total was " + str(ptot1) + ", which is greater than 21! You are now out of the round!")
                    time.sleep(5)
                    loop += 1
                    p2in = 1
                    run += 1
            elif "stay" in cont:
                loop += 1
        if run == 0:
            ("Since both players busted, we must now restart the round!")
            time.sleep(5)
    time.sleep(0.5)
    print ("Now it is the dealer's turn. To hit or stay. ")
    print ("The dealer's face down card was the " + dhd[1] + ". His total was " + str(dtot))
    time.sleep(2)
    loop = 0
    Cnew = 2
    while loop == 0:
        if dtot < 17:
            dhd.append(cards[random.randint(0,51)])
            for i in list:
                if str(i) in dhd[Cnew]:
                    dtot += i
            for i in list3:
                if str(i) in dhd[Cnew]:
                    dtot += 10
            if "ace" in dhd[Cnew]:
                dtot += ace
            print ("The dealer hits and receives the " + dhd[Cnew] + ". His new total is " + str(dtot))
            time.sleep(3)
            Cnew += 1
        if dtot > 16 and dtot < 22:
            print ("The dealer stays.")
            time.sleep(1)
            if dtot == ptot and p1in == 0:
                bet = bet+mtot
                print ("Player 1, the dealer tied with you! Nobody loses or wins any money!")
                loop += 1
            if ptot > dtot and p1in == 0:
                bet = bet+(mtot*2)
                print ("Player 1, your hand was greater than the dealer's you get 2x your bet! You now have " + str(bet) + " dollars!")
                loop += 1
            if dtot > ptot and p1in == 0:
                mtot = 0
                print ("Player 1, your hand was less than the dealers. You lost all your money :(")
                loop += 1
            if dtot == ptot1 and p2in == 0:
                bet1 = bet1+mtot1
                print ("Player 2, the dealer tied with you! Nobody loses or wins any money!")
                loop += 1
            if ptot1 > dtot and p2in == 0:
                bet1 = bet1+(mtot1*2)
                print ("Player 2, your hand was greater than the dealer's you get 2x your bet! You now have " + str(bet1) + " dollars!")
                loop += 1
            if dtot > ptot1 and p2in == 0:
                mtot1 = 0
                print ("Player 2, your hand was less than the dealers. You lost all your money :(")
                loop += 1
        if dtot > 21:
            bet = bet+(mtot*2)
            bet1 = bet1+(mtot1*2)
            if p1in == 0 and p2in == 0:
                print ("The dealer busted! Everyone gets 2x their bet! Player 1, you now have " + str(bet) + " dollars! Player 2, you now have " + str(bet1) + " dollars!")
            if p1in == 0 and p2in == 1:
                print ("The dealer busted! Everyone gets 2x their bet! Player 1, you now have " + str(bet) + " dollars! Player 2, you busted so you get nothing. :(")
            if p1in == 1 and p2in ==0:
                print ("The dealer busted! Everyone gets 2x their bet! Player 2, you now have " + str(bet1) + " dollars! Player 1, you busted so you get nothing. :(")
            loop += 1
            time.sleep(1)
    repeat = input("Would you guys  like to continue?")
    if "y" in repeat or "c" in repeat:
        repeat = 1
        run = 0
        loop = 0
    else:
        repeat = 0
        print("Thank you for playing BlackJack at GKV Python Resort. Have a nice day! Player 1 has earned " + str(bet) + " dollars. Player 2 has earned " + str(bet1) + " dollars! Come back again with more money, because with risks come rewards.")
       
