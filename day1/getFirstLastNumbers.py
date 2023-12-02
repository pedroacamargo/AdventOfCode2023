f = open("input.txt", "r")
array = f.read().split("\n")

stringNumber = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five":"5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

finalNumbers = []

for word in array:
    print("word before:" + word)

    numberString = []
    auxWord = ""
    for letter in word:
        auxWord += letter

        if letter.isnumeric():
            numberString.append(letter)
            auxWord = ""
            continue
        
        for x in stringNumber:
            if x in auxWord:
                numberString.append(stringNumber[x])                
                auxWord = x[-1]
                
    # print(numberString)
    
    if len(numberString) > 2:
        # get the first number and last number
        firstNumber = numberString[0]
        lastNumber = numberString[-1]
        numberString = [firstNumber, lastNumber]
    elif len(numberString) == 1:
        numberString.append(numberString[0])
    
    print("Word After:", end="")
    print("".join(numberString))
    finalNumbers.append(int("".join(numberString)))


print(sum(finalNumbers))