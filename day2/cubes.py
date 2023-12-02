f = open("input.txt", "r")
array = f.read().split("\n")

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
maxPlays = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possibleGames = []
powerOfMinimumSets = 0

for game in array:
    isPossible = True
    gameNumber = game.split(":")[0].strip().split(" ")[1].strip()
    
    reds = []
    blues = []
    greens = []

    game = game.split(":")[1].strip().split(";")
    game = [x.split(",") for x in game]

    # print("\nGame " + gameNumber + ":")
    for set in game:
        # print("\nSet:")
        for play in set:
            play = play.strip().split(" ")
            # print(play)
            
            tuple = (int(play[0]), play[1])
            
            
            if tuple[1] == "red":
                reds.append(tuple[0])
            elif tuple[1] == "green":
                greens.append(tuple[0])
            elif tuple[1] == "blue":
                blues.append(tuple[0])
            
            if tuple[0] > maxPlays[tuple[1]]:
                isPossible = False
            
            
            
            # print(tuple)
         
    # print("Reds: " + str(reds))
    # print("Greens: " + str(greens))
    # print("Blues: " + str(blues))
    
    maxDic = {
        "red": max(reds),
        "green": max(greens),
        "blue": max(blues)
    }
    
    powerOfMinimumSets += maxDic["red"] * maxDic["green"] * maxDic["blue"]
    
    if isPossible:
        possibleGames.append(gameNumber)    


print("Power of Minimum Sets: " + str(powerOfMinimumSets))
print("Possible games: " + str(possibleGames))
print("Sum of possible games: " + str(sum([int(x) for x in possibleGames])))