import player as player
from time import sleep

while True:
    print("Welcome to a Swiss Tournament Parings program!")


player_name = input("Insert Player Name Here: ")

player = player.player(player_name)

print(player.name)