def read_input():
    f = open("input.txt", "r")
    array = f.read().split("\n")
    array = [i.split(":")[1].strip() for i in array]
    tuples = [(i.split("|")[0].strip(), i.split("|")[1].strip()) for i in array]
    
    return tuples

def getCopies(gameNumber, scratchcards, numberOfMatches):
    if numberOfMatches > 0:
        for i in range(numberOfMatches):
            scratchcards.append(gameNumber)            

    return 0


# ----------------------- #
scratchcards = read_input()
res = 0

for game in scratchcards:
    
    roundDict = {
        "winningNumbers": game[0].split(" "),
        "myNumbers": game[1].split(" ")
    }
    
    numberOfMatches = 0
        
    filtered_list = list(filter(lambda x: x != '', roundDict["myNumbers"]))    
    intfiltered_list = [int(i) for i in filtered_list]
    
    winningNumbers = list(filter(lambda x: x != '', roundDict["winningNumbers"]))
    intwinningNumbers = [int(i) for i in winningNumbers]
    print(intwinningNumbers)
        
    for number in intfiltered_list:
        if number in intwinningNumbers:
            numberOfMatches = 1
    
    
    
    res += numberOfMatches

print(res)