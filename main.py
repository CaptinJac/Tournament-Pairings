import player as player
from time import sleep
from alive_progress import alive_bar

for total in 5000, 7000, 4000, 0:
    with alive_bar(total) as bar:
        for x in range(5000):
            sleep(.001)
            bar()

while True:
    print("Welcome to a Swiss Tournament Parings program!")


player_name = input("Insert Player Name Here: ")

player = player.player(player_name)

print(player.name)