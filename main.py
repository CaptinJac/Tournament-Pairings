from random import shuffle
import player as player
from time import sleep
import os

player_list = []
rounds = 0 
current_round = 0

def issue_parings(player_list, current_round):
    top_list = []
    bot_list = []
    pairings = []
    
    for x in player_list:
        score = x.score
        if score == 3 * current_round:
            top_list.append(x)
        else:
            bot_list.append(x)
    
    if (len(top_list) % 2 == 0) or (len(bot_list) % 2 == 0):
        pass
    else:
        for x in top_list:
            bot_list.append(x)
        top_list = []
    top_list = player_list
    if len(top_list) == 0:
        pass
    else: 
        shuffle(top_list)
        for x in range(len(top_list) - 1):
            if len(top_list) == 0 :
                break
            table = []
            player_1 = top_list[0]
            player_2 = top_list[1]
            table.append(player_1)
            table.append(player_2)
            top_list.pop(0)
            top_list.pop(0)
            pairings.append(table)
        return pairings
    
    

    
def start():
    while True:
        print("Welcome to a Swiss Tournament Parings program!")
        print("Reading names.txt please wait...")
        f = open("names.txt")
        
        for x in f:
            player_name = player.player(x, 0)
            player_list.append(player_name)
        f.close()

        sleep(1)
        print("Done!")
        print("Calculating Rounds. Please wait...")

        player_count = len(player_list)
        
        if player_count < 4: 
            print("I'm sorry, there is not enought players to compete right now! Add more names to names.txt! Please try again!")
            input("Press Enter to quit...")  
            break
        elif player_count >= 4 and player_count <= 8:
            rounds = 3
        elif player_count >= 9 and player_count <= 16:
            rounds = 4
        elif player_count >= 17 and player_count <= 32:
            rounds = 5
        elif player_count >= 33 and player_count <= 64:
            rounds = 6
        elif player_count >= 65 and player_count <= 128:
            rounds = 7
        elif player_count >= 129 and player_count <= 256:
            rounds = 8
        elif player_count >= 257 and player_count <= 512:
            rounds = 9
        elif player_count >= 513 and player_count <= 1024:
            rounds = 10
        elif player_count >= 1025 and player_count <= 2048:
            rounds = 11
        elif player_count >= 2049:
            rounds = 12
        
        sleep(1)
        print("Currently you have %s players! You will have %s rounds for this tournament!" % (player_count, rounds))
        input("Press Enter to begin the first round...")
        
        os.system('cls' if os.name == 'nt' else 'clear')

        round_pairing = issue_parings(player_list,current_round)
        
        for x in round_pairing:
            for y in x:
                print(y.name)

        break

start()