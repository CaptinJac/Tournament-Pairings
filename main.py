import player as player

player_list = []
rounds = 0 
current_round = 0

while True:
    print("Welcome to a Swiss Tournament Parings program!")
    print("Reading names.txt please wait...")
    f = open("names.txt")
    
    for x in f:
        player_name = player.player(x)
        player_list.append(player_name)
    f.close()

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
    print("Currently you have %s players! You will have %s amount of rounds for this tournament!" % (player_count, rounds))

    for x in player_list:

    break
