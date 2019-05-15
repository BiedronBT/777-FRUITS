from os import system, name
import time
from random import randint
from sty import fg


def clear():
    """This function will be used to clear the screen"""
    if name == 'nt':
        # If run on Windows
        system('cls')
    else:
        # If run on Linux
        system('clear')


# Below are defined 6 lists of 6 strings which are displayed in game symbols
# Number in parenthesis for 'fg' method sets 8-bit color for string
strawberry = [fg(111) + '         ' + fg.rs,
               fg(34) + '    ##   ' + fg.rs,
              fg(196) + '   ####  ' + fg.rs,
              fg(196) + '   ####  ' + fg.rs,
              fg(196) + '    ##   ' + fg.rs,
              fg(111) + '         ' + fg.rs]

banana = [fg(226) + '         ' + fg.rs,
          fg(226) + '      #  ' + fg.rs,
          fg(226) + '     ##  ' + fg.rs,
          fg(220) + '    ##   ' + fg.rs,
          fg(220) + '  ##     ' + fg.rs,
          fg(226) + '         ' + fg.rs]

plum = [fg(22) + '         ' + fg.rs,
        fg(22) + '    ##   ' + fg.rs,
        fg(19) + '  ####   ' + fg.rs,
        fg(19) + ' #####   ' + fg.rs,
        fg(19) + '  ##     ' + fg.rs,
        fg(22) + '         ' + fg.rs]

raspberry = [fg(161) + '         ' + fg.rs,
              fg(34) + '    #    ' + fg.rs,
             fg(161) + '   ###   ' + fg.rs,
             fg(161) + '  #####  ' + fg.rs,
             fg(161) + '   ###   ' + fg.rs,
             fg(161) + '         ' + fg.rs]

orange = [fg(111) + '         ' + fg.rs,
           fg(40) + '     #   ' + fg.rs,
          fg(208) + '   ###   ' + fg.rs,
          fg(208) + '  #####  ' + fg.rs,
          fg(208) + '   ###   ' + fg.rs,
          fg(111) + '         ' + fg.rs]

seven = [fg(111) + '         ' + fg.rs,
          fg(88) + '   ####  ' + fg.rs,
         fg(124) + '      #  ' + fg.rs,
         fg(160) + '     #   ' + fg.rs,
         fg(196) + '    #    ' + fg.rs,
         fg(111) + '         ' + fg.rs]


class Cash:

    def __init__(self, credit=100, bet=2):
        """
        Sets amount of player's credits at the beginning of game,
        initial bet, and variants of bets that player will be able to toggle between
        """
        self.credit = credit
        self.bet = bet
        self.bets = [2, 5, 10, 20]

    def change_bet(self):
        """Moves first number of bets list at the end"""
        self.bets.append(self.bets.pop(0))
        self.bet = self.bets[0]

    def charge(self):
        """
        Checks if player has enough credit to place a bet
        if not gives prompt and returns True so player will be able to lower bet
        else it subtracts bet from player's credits
        """
        if self.bet <= self.credit:
            self.credit -= self.bet
            return False
        else:
            machine.still()
            print('\n\t     Not enough credit to place a bet')
            time.sleep(2)
            return True


class Slots:

    def __init__(self):
        """
        Defining 3 slots of machine as lists from already defined variables
        First slot is unique because except printable symbol it has also multiplier of bet
        """
        self.slot_one = [(strawberry, 2), (banana, 10), (plum, 3), (strawberry, 2), (raspberry, 5), (plum, 3), (orange, 8), (seven, 15)]
        self.slot_two = [banana, strawberry, plum, orange, strawberry, plum, raspberry, seven]
        self.slot_three = [plum, strawberry, raspberry, orange, plum, strawberry, seven, banana]

    def roll(self):
        """
        This method is responsible for showing machine's slots in motion
        """
        # First of all 3 random numbers are set
        # Since every symbol of slots has 6 lines, all 3 numbers must be divisible by 6 to make full rotates
        a, b, c = 1, 1, 1
        while a % 6 != 0:
            a = randint(70, 110)
        while b % 6 != 0:
            b = randint(60, 90)
        while c % 6 != 0:
            c = randint(70, 100)

        # This for loop composes 3 lists to pass them to function that will print current state of slots
        # Does this for random number of times using first random number set before
        # Variable 'i' will be used to access only some parts of displayed symbols
        i = 1
        for _ in range(a):
            clear()
            if i == 6:
                i = 0
                # After each 6 jumps of slots by single line first symbol of each slot list will be moved at the end
                self.slot_one.append(self.slot_one.pop(0))
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            # Here are composed lists to be printed
            # First symbol may be partial and then will be taken part of forth symbol
            s1 = self.slot_one[0][0][i:] + self.slot_one[1][0] + self.slot_one[2][0] + self.slot_one[3][0][0:i]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        # Similar as before, but now first slot will not changed - no move
        i = 1
        for _ in range(b):
            clear()
            if i == 6:
                i = 0
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        # Last sequence, with only last slot changing
        i = 1
        for t in range(c):
            clear()
            if i == 6:
                i = 0
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            # Equation below gives last slot slowing-down effect, can be tweaked easily
            time.sleep(0.02 + t**2 / 90000)

    def still(self):
        """This method is used to compose states of slots while not moving and pass to print"""
        clear()
        fin1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
        fin2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
        fin3 = self.slot_three[0] + self.slot_three[1] + self.slot_three[2]
        layout(fin1, fin2, fin3)
        print('\n\t  [ENTER] Play   [B] Change bet   [Q] Quit ')

    def adding_credits(self, prize):
        """
        Adds credits to player's account, 1 credit for prize times
        Also print the whole layout
        :param prize: result of win_amount function, may be 0 if there is no match in slots
        """
        for n in range(prize):
            clear()
            money.credit += 1
            fin1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            fin2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
            fin3 = self.slot_three[0] + self.slot_three[1] + self.slot_three[2]
            layout(fin1, fin2, fin3)
            time.sleep(0.03)


def win_amount():
    """
    This function checks if there is a match in slots, 3 horizontal lines and 2 diagonal
    :return: If match - placed bet times symbol's multiplier, if no match - 0
    """
    if machine.slot_one[0][0] == machine.slot_two[0] == machine.slot_three[0]:
        return money.bet * machine.slot_one[0][1]
    elif machine.slot_one[1][0] == machine.slot_two[1] == machine.slot_three[1]:
        return money.bet * machine.slot_one[1][1]
    elif machine.slot_one[2][0] == machine.slot_two[2] == machine.slot_three[2]:
        return money.bet * machine.slot_one[2][1]
    elif machine.slot_one[0][0] == machine.slot_two[1] == machine.slot_three[2]:
        return money.bet * machine.slot_one[0][1]
    elif machine.slot_one[2][0] == machine.slot_two[1] == machine.slot_three[0]:
        return money.bet * machine.slot_one[2][1]
    else:
        return 0


def layout(s1, s2, s3):
    """
    Responsible for graphical representation of game
    :param s1, s2, s3: Three slots prepared by one of methods from Slots class
    """
    print('\n\t   __________________________________________')
    print('\t  /                                         /|')
    print('\t /_________________________________________/ |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|   STRAWBERRY  x2       PLUM       x3    |  |')
    print('\t|                                         |  |')
    print('\t|   RASPBERRY   x5       ORANGE     x8    |  |')
    print('\t|                                         |  |')
    print('\t|   BANANA     x10       SEVENS    x15    |  |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|   -----------------------------------   |  |')
    for l, m, r in zip(s1, s2, s3):
        print('\t|  |', l, '|', m, '|',  r, '|  |  |')
    print('\t|   -----------------------------------   |  |')
    print('\t|                                         |  |')
    print('\t|    BET  {}              CREDIT {}    |  |'.format(' ' * (2 - len(str(money.bet))) + str(money.bet),
                                                                 ' ' * (5 - len(str(money.credit))) + str(money.credit)))
    print('\t|                                         | /')
    print('\t|_________________________________________|/')

def welcome():
    welcome = ['\n\n\t #######    #######    #######',
               '\t########   ########   ########',
               '\t     ##         ##         ##',
               '\t    ##         ##         ##',
               '\t   ##         ##         ##',
               '\t  ##         ##         ##',
               '\t  ##         ##         ##',
               '\n\n'
               '\t#### ###  #  #  # ##### ####',
               '\t#    #  # #  #  #   #   #  ',
               '\t###  ###  #  #  #   #   ####',
               '\t#    #  # #  #  #   #      #',
               '\t#    #  # ####  #   #   ####']
    for c in welcome:
        print(c)
        time.sleep(0.1)
    time.sleep(1)

if __name__ == '__main__':
    clear()
    welcome()
    money = Cash()
    machine = Slots()

    while True:
        machine.still()
        again = input('\n')
        if again == 'q':
            break
        elif again == 'b':
            money.change_bet()
            continue
        elif again == '':
            if money.charge():
                continue
            machine.roll()
            machine.adding_credits(win_amount())

    time.sleep(1)
    clear()
