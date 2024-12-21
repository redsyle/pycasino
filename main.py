import random
money = 0
description = "A simple casino in Python. Author: psychoredz"
print(description)
wallet = "$"
while True:
    select = input("Enter command: ")
    if select == "setmoney":
        muchmoney = input("How much money you want to set? ")
        money = int(muchmoney)
        print(f"New balance: {money}{wallet}")
    elif select == "play":
        bet = int(input("Enter your bet: "))
        if money < bet: print("Not enough money!"); exit()
        else:
            money = money - bet
            gameselect = input("Enter game: ")
            if gameselect == "coinflip":
                coinselect = input("Select, orel or reshka? ").lower().replace(" ", "")
                x = random.choice(["orel", "reshka"])
                if coinselect == x:
                    print("You win!")
                    money += bet*2
                    print(f"New balance: {money}{wallet}")
                    bet = 0
                else:
                    print("You lose!")
                    print(f"New balance: {money}{wallet}")
                    bet = 0
            elif gameselect == "random":
                rand = random.choice([0, 0.2, 1, 2, 5])
                print(f"Multipier: {rand}")
                money += bet*rand
                print(f"New balance: {money}{wallet}")
            else: print("Unknown game!");
    elif select == "balance": print(f"Balance: {money}{wallet}")
    elif select == "exit": print("Bye!"); exit()
    elif select == "changewallet": wallet = input("Enter your new wallet: ")
    elif select == "description": print(description)
    else: print("Unknown command!")
