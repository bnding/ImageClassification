def train(trainingData):
    givenTrue = []
    givenFalse = []
    countTrue = 0
    countFalse = 0

    # Solving for p(x|y=true) and p(x|y=false)
    # Assigning frequencies of numbers into respective locations in array of dictionaries
    for x in range(0, len(trainingData)):
        # If image is true
        if(trainingData[x][1] == 1):
            countTrue += 1

            # new array
            if(len(givenTrue) == 0):
                for section in range(0, len(trainingData[x][0])):
                    givenTrue.append({trainingData[x][0][section]: 1})

            # array already exists
            else:
                for section in range(0, len(trainingData[x][0])):
                    if(trainingData[x][0][section] in givenTrue[section]):
                        givenTrue[section].update({trainingData[x][0][section]: givenTrue[section].get(trainingData[x][0][section]) + 1})
                    else:
                        givenTrue[section][trainingData[x][0][section]] = 1
                
        # If image is false
        else:
            countFalse += 1
            if(len(givenFalse) == 0):
                for x in trainingData[x][0]:
                    givenFalse.append({x: 1})
            else:
                for section in range(0, len(trainingData[x][0])):
                    if(trainingData[x][0][section] in givenFalse[section]):
                        givenFalse[section].update({trainingData[x][0][section]: givenFalse[section].get(trainingData[x][0][section]) + 1})
                    else:
                        givenFalse[section][trainingData[x][0][section]] = 1

    # Dividing frequency by count to get probability
    for x in range(0, len(givenTrue)):
        for keys in givenTrue[x]:
            givenTrue[x].update({keys: givenTrue[x][keys] / countTrue})

    for x in range(0, len(givenFalse)):
        for keys in givenFalse[x]:
            givenFalse[x].update({keys: givenFalse[x][keys] / countFalse})


    # Now solving for p(y=true) and p(y=false)
    pyTrue = countTrue / len(trainingData)
    pyFalse = countFalse / len(trainingData)


    print(f"\nP(y=true): {pyTrue}")
    print(f'givenTrue: {givenTrue}')

    print()
    print(f"\nP(y=false): {pyFalse}")
    print(f'givenFalse: {givenFalse}')

    return givenTrue, pyTrue, givenFalse, pyFalse


def predict(givenTrue, pyTrue, givenFalse, pyFalse):
    print("predict")

def main():
    trainingData=[([3,8,8,9], 1), ([2,4,6,4], 0), ([4,3,9,9], 1), ([3, 4, 5, 1], 0), ([2,8,1,9], 1)]
    train(trainingData)

if __name__ == '__main__':
    main()