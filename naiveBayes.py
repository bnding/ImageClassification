def train(trainingData):
    givenTrue = []
    givenFalse = []
    for x in range(0, len(trainingData)):
        if(trainingData[x][1] == 1):
            if(len(givenTrue) == 0):
                for section in range(0, len(trainingData[x][0])):
                    givenTrue.append({trainingData[x][0][section]: 0})
            else:
                flag = 0
                for section in range(0, len(trainingData[x][0])):
                    if(trainingData[x][0][section] in givenTrue[section]):
                        givenTrue[section].update({trainingData[x][0][section]: givenTrue[section].get(trainingData[x][0][section]) + 1})
                    else:
                        givenTrue[section][trainingData[x][0][section]] = 0
                

        else:
            if(len(givenFalse) == 0):
                for x in trainingData[x][0]:
                    givenFalse.append({x: 0})

    print(f'givenTrue: {givenTrue}')
    print(f'givenFalse: {givenFalse}')


def main():
    trainingData=[([3,8,8,9], 1), ([2,4,6,4], 0), ([4,3,9,9], 1)]
    train(trainingData)

if __name__ == '__main__':
    main()