#
# Super-Six for Computerselbstbeschäftigung
#

from random import randint

# VAR
number_players = 64
sticks = 8192
players = []
board = []

VERBOSE = False
SUMMARIZE = True

# FUNC

def roll_dice():
    return randint(1, 6)

def init_players(n_p, n_s):
    t = []
    for item in range(n_p):
        t.append(n_s)
    return t

def is_over(p):
    t = 0
    for points in p:
        if points > 0:
            t += 1
    if t == 1:
        return True
    else:
        return False

def init_board():
    return [False, False, False, False, False]

def print_board(b):
    z = 1
    print("+===+===+")
    for feld in b:
        if feld == True:
            print("| " + str(z) + " | x |")
        else:
            print("| " + str(z) + " | O |")
        z += 1
    print("+===+===+")
    return None

def print_players(p):
    z = 1
    for n in p:
        print(str(z) + ". Player: " + str(n))
        z += 1
    
def move():
    return None

# INIT
board = init_board()
players = init_players(number_players, sticks)

# LET'S PLAY
z = 1
r = 1
while(True):
    if(VERBOSE):
        print("")
        print("Round: " + str(r))
        print_board(board)
        print_players(players)
    for p in players:
        if z > number_players:
            z = 1
        if p > 0:
            d = roll_dice()
            if d == 6:
                players[z-1] = p-1
                if(VERBOSE):
                    print("Player " + str(z) + " rolls " + str(d) + " and drops one stick")
            else:
                if board[d-1] == False:
                    board[d-1] = True
                    players[z-1] = p-1
                    if(VERBOSE):
                        print("Player " + str(z) + " rolls " + str(d) + " and puts one stick onto number " + str(d))
                else:
                    board[d-1] = False
                    players[z-1] = p+1
                    if(VERBOSE):
                        print("Player " + str(z) + " rolls " + str(d) + " and takes one stick from number " + str(d))

        z += 1
    if is_over(players):
        break
    r += 1
if(SUMMARIZE):
    print("The game took " + str(r) + " rounds.")
