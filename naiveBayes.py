def train(trainingData):
    givenTrue = []
    givenFalse = []
    countTrue = 0
    countFalse = 0

    # Assigning frequencies of numbers into respective locations in array of dictionaries
    for data in trainingData:
        # If image is true
        if(data[1] == 1):
            countTrue += 1

            # new array
            if(len(givenTrue) == 0):
                for key in range(0, len(data[0])):
                    givenTrue.append({data[0][key]: 1})

            # array already exists
            else:
                for key in range(0, len(data[0])):
                    if(data[0][key] in givenTrue[key]):
                        givenTrue[key].update({data[0][key]: givenTrue[key].get(data[0][key]) + 1})
                    else:
                        givenTrue[key][data[0][key]] = 1
                
        # If image is false
        else:
            countFalse += 1
            if(len(givenFalse) == 0):
                for key in data[0]:
                    givenFalse.append({key: 1})
            else:
                for key in range(0, len(data[0])):
                    if(data[0][key] in givenFalse[key]):
                        givenFalse[key].update({data[0][key]: givenFalse[key].get(data[0][key]) + 1})
                    else:
                        givenFalse[key][data[0][key]] = 1

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

    return givenTrue, pyTrue, givenFalse, pyFalse

# Solving for L(x)
def predict(testingData, givenTrue, pyTrue, givenFalse, pyFalse):
    pGivenTrue = []
    pGivenFalse = []
    lx = []
    for data in testingData:
        if(data[1] == 1):
            for key in range(0, len(data[0])):
                if(data[0][key] in givenTrue[key]):
                    pGivenTrue.append(givenTrue[key].get(data[0][key]))
            probability = pGivenTrue[0]
            for x in range (1, len(pGivenTrue)):
                probability *= pGivenTrue[x]
            print(f"\n\ntrue probability: {probability}")
            if(probability >= 1):
                lx.append(1)
            else:
                lx.append(0)


        else:
            for key in range(0, len(data[0])):
                if(data[0][key] in givenFalse[key]):
                    pGivenFalse.append(givenFalse[key].get(data[0][key]))
            
            probability = pGivenFalse[0]
            for x in range (1, len(pGivenFalse)):
                probability *= pGivenFalse[x]
            print(f"\n\nfalse probability: {probability}")
            if(probability >= 1):
                lx.append(1)
            else:
                lx.append(0)

    print(pGivenTrue)
    return pGivenTrue, pGivenFalse, lx

def main():
    trainingData=[([3,8,8,9], 1), ([2,4,6,4], 0), ([4,3,9,9], 1), ([3, 4, 5, 1], 0), ([2,8,1,9], 1)]
    testingData = [([3,8,9,9], 1), ([2, 4, 6, 1], 0), ([4, 3, 9, 9], 1)]

    givenTrue, pyTrue, givenFalse, pyFalse = train(trainingData)
    print(f"\nP(y=true): {pyTrue}")
    print(f'givenTrue: {givenTrue}')
    print(f"\nP(y=false): {pyFalse}")
    print(f'givenFalse: {givenFalse}')


    pGivenTrue, pGivenFalse, lx = predict(testingData, givenTrue, pyTrue, givenFalse, pyFalse,)

    print(f"\n\n\npGivenTrue: {pGivenTrue}\npGivenFalse{pGivenFalse}\n\nlx: {lx}")


if __name__ == '__main__':
    main()