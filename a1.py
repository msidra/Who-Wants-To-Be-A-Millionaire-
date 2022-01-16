'''                                    Welcome :)
 This program is designed to give you a feel of the hit show 'Who Wants To Be A Millionaire' but with a slight twist.
 It makes use of the following -
        1. if statements
        2. Boolean primitive data types
        3. while loops
        4. Character comparisons
        5. Functions
 Is your knowledge worth a million dollars? There's only one way to find out! '''

import random                      # imports package 'random' from library to make function 'random.choice()' work


def continue_game():               # function to determine whether to continue playing or not
    opt = int(input('\n Do you wish to: 1. Move on to the next round \n \t \t \t \t 2. Leave with your current cash prize '))
    if opt == 1:
        return True                 # returns to main program and continues it
    elif opt == 2:
        print('\n TOTAL AMOUNT WON: \U0001F4B0', cash, '\n See you next game. Farewell.')
        exit()


def exp_advice():                  # function to return a random letter to main function
    options = ['A', 'B', 'C', 'D']     # creates list 'options' with 4 elements
    answer = random.choice(options)    # chooses a random element from the list 'options'
    print('After much deliberation, Mr. Harper (expert) has come to the conclusion that the answer is option', answer)
    return answer                      # returns 'answer' to main program


def check(e, c):                   # function to check if random letter returned matches the right answer
    if e == 'B':
        print('Mr. Harper: The expert is called an expert for a reason. LEVEL UP!')
        c += 250000
        print(f"{'CASH WON: ' : >100}", '$%s' % c)
    else:
        c = 0
        print("Oh no! Seems like that wasn't the right answer.")
        print('Mr. Harper, the "expert", turned out to be a fraud and fled with your cash prize. Choose wisely next time.')
        print('\n')
        print(f"{'FINAL AMOUNT: ' : >100}", '$%s' % c)
        exit()


if __name__ == "__main__":          # to prevent code floating into the ether
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{' WHO WANTS TO BE A MILLIONAIRE ' : ^85}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    cash = 0                        # assigns value of 'cash' as 0

    print(f"{'  ROUND 1 ' : ^83}")
    print(' - Question 1 -')
    print(" Which of these brands is associated with the manufacture of household locks?")
    print(" \t \t A. Philips \t B. Chubbs \t C. Ronseal \t D. Flymo ")
    ans = str(input(" Choose an option: "))           # accepts user's input
    while True:                                       # loop works as long as True ('while True' is always True)
        if ans == 'B' or ans == 'b':                  # compares characters 'ans' and letter 'B'
            cash += 500                               # performs mathematical operation on 'cash'
            print(" \U0001F4B0 +500")
            break                                     # to leave loop and continue with rest of program
        elif ans in ['A', 'a', 'c', 'C', 'd', 'D']:   # to check if 'ans' matches any element in said list
            print("*cricket sounds* ")
            break
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'Cash won: ' : >100}", '$', cash)

    print('\n - Question 2 -')
    print("When and where did ice cream originate?")
    print("A. Rome, 4th century BCE  \t B. France, 17th century BCE  \t C. Italy, 7th century BCE  \t D. China, 618 CE ")
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'D' or ans == 'd':
            cash += 500
            print(" \U0001F4B0 +500")
            break
        elif ans in ['A', 'a', 'B', 'b', 'C', 'c']:
            cash = 0
            print("Take the nearest exit please.")
            print(f"{'Final Amount: ' : >100}", '$', cash)
            exit()                                                  # to terminate the program as the user has lost
        else:
            ans = str(input(' Invalid input. Please enter one of the given options: '))
    print(f"{'Cash won: ' : >100}", '$', cash)

    print('\n - Question 3 -')
    print("When did the Vikings invade Britain?")
    print("A. 810 CE  \t B. 618 CE  \t C. 793 CE  \t D. 618 BCE  ")
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'C' or ans == 'c':
            cash += 14000
            print(" \U0001F4B0 +5000")
            break
        elif ans in ['A', 'a', 'B', 'b', 'D', 'd']:
            cash = 0
            print("So close...not")
            print(f"{'Final Amount: ' : >100}", '$', cash)
            exit()
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)

    print('\n - Question 4 -')
    print(" In 1997, the race to Christmas number 1 was between the Spice Girls and who?")
    print("A. Teletubbies  \t B. TLC  \t C. Mariah Carey  \t D. The Mickey Mouse Club  ")
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'a' or ans == 'A':
            cash += 15000
            print(" \U0001F4B0 +15000")
            break
        elif ans in ['c', 'C', 'B', 'b', 'D', 'd']:
            cash = 0
            print("Halfway ther- never mind ")
            print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
            exit()
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)

    print(f"{'  ROUND 2 ' : ^83}")
    print('\n - Question 5 -')
    print("In Greek mythology, who is considered the goddess of good luck?")
    print("A. Nike  \t B. Tyche  \t C. Nemesis  \t D. Fortuna  ")
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'b' or ans == 'B':
            cash += 20000
            print(" \U0001F4B0 +20000")
            break
        elif ans in ['A', 'a', 'c', 'C', 'D', 'd']:
            cash -= 20000
            print("Guess someone angered Tyche. ")
            print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
            exit()
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)
    continue_game()                                                 # function call to ask if user wishes to proceed

    print('\n - Question 6 -')
    print("In Doctor Who, what was the look of the fourth doctor, as portrayed by Tom Baker?")
    print("A. Cape, velvet jacket, frilly shirt  \t B. Wide-brimmed hat, extra long scarf  \t C. Pinstripe suit, trainers   \t D. Bow-tie, braces, tweed jacket  ")
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'b' or ans == 'B':
            cash += 50000
            print(" \U0001F4B0 +50000")
            break
        elif ans in ['A', 'a', 'C', 'c', 'D', 'd']:
            cash = 50000
            print("Well you got a 50%")
            print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
            exit()
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)
    continue_game()

    print('\n - Question 7 -')
    print("During World War II, US soldiers used the first commercial aerosol cans to hold what??")
    print("A. Shaving cream  \t B. Insecticide  \t C. Cleaning fluid  \t D. Cleaning fluid   ")
    option = int(input('\n Do you wish to 1. Choose an option \n \t \t \t \t2. Get expert advice '))
    if option == 1:
        ans = str(input("Choose an option: "))
        while True:
            if ans == 'b' or ans == 'B':
                cash += 200000
                print(" \U0001F4B0 +200000")
                break
            elif ans in ['A', 'a', 'C', 'c', 'D', 'd']:
                cash = 100000
                print("See ya ")
                print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
                exit()
            else:
                ans = str(input(' Invalid input. Please enter one of the given options: '))
    elif option == 2:
        exp = exp_advice()                # calls function 'exp_advice()' and assigns value returned to 'exp'
        check(exp, cash)                  # calls function 'check()' while passing arguments 'exp' and 'cash'
    else:
        option = int(input(' Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)
    continue_game()

    print('\n - Question 8 -')
    print("According to the Population Reference Bureau, what is the approximate number of people who have ever lived on Earth?")
    print("A. 7.4 Billion  \t B. 116.7 Billion  \t C. 1.5 Trillion  \t D. 5.2 Trillion  ")
    option = int(input('\n Do you wish to 1. Choose an option \n \t \t \t \t2. Get expert advice '))
    if option == 1:
        ans = str(input("Choose an option: "))
        while True:
            if ans == 'b' or ans == 'B':
                cash += 200000
                print(" \U0001F4B0 +200000")
                break
            elif ans in ['A', 'a', 'B', 'b', 'D', 'd']:
                cash = 100000
                print("Oo that's gotta hurt ")
                print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
                exit()
            else:
                ans = str(input(' Invalid input. Please enter one of the given options: '))
    elif option == 2:
        exp = exp_advice()
        check(exp, cash)
    else:
        option = int(input(' Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)
    continue_game()

    print(' - Question 9 -')
    print("Neurologists believe that the brain's medial ventral prefrontal cortex is activated when you do what??")
    print("A. Have a panic attack  \t B. Get a joke  \t C. Remember a name  \t D. Listen to music  ")
    option = int(input('\n Do you wish to 1. Choose an option \n \t \t \t \t2. Get expert advice '))
    if option == 1:
        ans = str(input("Choose an option: "))
        while True:
            if ans == 'b' or ans == 'B':
                cash += 250000
                print(" \U0001F4B0 +250000")
                break
            elif ans in ['A', 'a', 'B', 'b', 'D', 'd']:
                cash = 250000
                print("Lol bye")
                print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
                exit()
            else:
                ans = str(input(' Invalid input. Please enter one of the given options: '))
    elif option == 2:
        exp = exp_advice()
        check(exp, cash)
    else:
        option = int(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)
    continue_game()

    print(' - The million dollar question -')
    print('The song "God Bless America" was originally written for what 1918 musical?')
    print('A. "Oh Lady! Lady!!"  \t B. "Yip, Yip, Yaphank"  \t C. "Blossom Time"  \t D. "Watch Your Step"  ')
    ans = str(input("Choose an option: "))
    while True:
        if ans == 'b' or ans == 'B':
            cash += 250000
            print(" \U0001F4B0 +250000")
            break
        elif ans in ['A', 'a', 'B', 'b', 'D', 'd']:
            cash = 0
            print("Guess someone angered Nike.")
            print(f"{'FINAL AMOUNT: ' : >100}", '$', cash)
            exit()
        else:
            ans = str(input('Invalid input. Please enter one of the given options: '))
    print(f"{'CASH WON: ' : >100}", '$', cash)

    print('Thank you for playing with us. Until next time!')
