''' this is the main wumpus code file '''
WUMPUS_INSTRUCTIONS = "WELCOME TO 'HUNT THE WUMPUS'\n"\
                      "THE WUMPUS LIVES IN A CAVE OF 20 ROOMS. EACH ROOM\n"\
                      "HAS 3 TUNNELS LEADING TO OTHER ROOMS. (LOOK AT A\n"\
                      "DODECAHEDRON TO SEE HOW THIS WORKS-IF YOU DON'T KNOW\n"\
                      "WHAT A DODECAHEDRON IS, ASK SOMEONE)\n"\
                      "\n"\
                      " HAZARDS:\n"\
                      " BOTTOMLESS PITS: TWO ROOMS HAVE BOTTOMLESS PITS"\
                      " IN THEM\n"\
                      " IF YOU GO THERE, YOU FALL INTO THE PIT (& LOSE!)\n"\
                      " SUPER BATS     : TWO OTHER ROOMS HAVE SUPER BATS."\
                      " IF YOU\n"\
                      " GO THERE, A BAT GRABS YOU AND TAKES YOU TO"\
                      " SOME OTHER\n"\
                      " ROOM AT RANDOM. (WHICH MAY BE TROUBLESOME)\n"\
                      " WUMPUS:\n"\
                      " THE WUMPUS IS NOT BOTHERED BY HAZARDS"\
                      "(HE HAS SUCKER\n"\
                      " FEET AND IS TOO BIG FOR A BAT TO LIFT).  USUALLY\n"\
                      " HE IS ASLEEP.  TWO THINGS WAKE HIM UP: YOU "\
                      "SHOOTING AN\n"\
                      " ARROW OR YOU ENTERING HIS ROOM.\n"\
                      " IF THE WUMPUS WAKES HE MOVES (P=.75) ONE ROOM\n"\
                      " OR STAYS STILL (P=.25).  AFTER THAT, IF HE IS"\
                      " WHERE YOU\n"\
                      " ARE, HE EATS YOU UP AND YOU LOSE!\n"\
                      "\n"\
                      " YOU:\n"\
                      " EACH TURN YOU MAY MOVE OR SHOOT A CROOKED ARROW\n"\
                      " MOVING:  YOU CAN MOVE ONE ROOM (THRU ONE TUNNEL)\n"\
                      " ARROWS:  YOU HAVE 5 ARROWS.  YOU LOSE WHEN YOU RUN"\
                      " OUT\n"\
                      " EACH ARROW CAN GO FROM 1 TO 5 ROOMS. YOU AIM BY"\
                      " TELLING\n"\
                      "   THE COMPUTER THE ROOM#S YOU WANT THE ARROW TO"\
                      " GO TO.\n"\
                      "   IF THE ARROW CAN'T GO THAT WAY (IF NO TUNNEL)"\
                      " IT MOVES\n"\
                      "   AT RANDOM TO THE NEXT ROOM.\n"\
                      "     IF THE ARROW HITS THE WUMPUS, YOU WIN.\n"\
                      "     IF THE ARROW HITS YOU, YOU LOSE.\n"\
                      " WARNINGS:\n"\
                      " WHEN YOU ARE ONE ROOM AWAY FROM A WUMPUS OR HAZARD,\n"\
                      " THE COMPUTER SAYS:\n"\
                      " WUMPUS:  'I SMELL A WUMPUS'\n"\
                      " BAT   :  'BATS NEARBY'\n"\
                      " PIT   :  'I FEEL A DRAFT'\n"\
                      "\n"
CAVES = [[1,4,7],
         [0,2,9],
         [1,3,11],
         [2,4,13],
         [0,3,5],
         [4,6,14],
         [5,7,16],
         [0,6,8],
         [7,9,17],
         [1,8,10],
         [9,11,18],
         [2,10,12],
         [11,13,19],
         [3,12,14],
         [5,13,15],
         [14,16,19],
         [6,15,17],
         [8,16,18],
         [10,17,19],
         [12,15,18],]
GAME_WON = "HEE HEE HEE - THE WUMPUS'LL GET YOU NEXT TIME!!\n"
GAME_LOST = "HA HA HA - YOU LOSE!\n"
GAME_DEBUG = True
ARROWS = 5

YOU = 0
WUMPUS = 1
PITS = 2
PIT2 = 3
BATS1 = 4
BATS2 = 5
LOCS = 6

PLAYER = [YOU, ARROWS]


def game_setup():
    ''' game setup '''
    if GAME_DEBUG:
        print('[+] Game setup starting...')
    print(WUMPUS_INSTRUCTIONS)
    print(f'[*] you are in Cave {YOU} : {CAVES[YOU]}')
    print(f'[*] wumpus is in Cave {WUMPUS} : {CAVES[WUMPUS]}')
    print(f'[*] pit 1 is in Cave {PITS} : {CAVES[PITS]}')
    print(f'[*] pit 2 is in Cave {PIT2} : {CAVES[PIT2]}')
    print(f'[*] bats 1 is in Cave {BATS1} : {CAVES[BATS1]}')
    print(f'[*] bats 2 is in Cave {BATS2} : {CAVES[BATS2]}')
    print(f'[*] locations are {LOCS} : {CAVES[LOCS]}')
    if GAME_DEBUG:
        print('[+] Game setup complete!') 


def game_play():
    ''' game play '''
    if GAME_DEBUG:
        print('[+] Game play starting...')

    if GAME_DEBUG:
        print('[+] Game play complete!')


def main():
    ''' main function '''
    print('[-] Wumpus Game starting...')
    game_setup()
    game_play()
    print(f'[=] number of caves = {len(CAVES)}' )
    print('[-] Wumpus Game complete!')


if __name__ == '__main__':
    main()
