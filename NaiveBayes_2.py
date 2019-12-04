def trainFace(trainingFeatures,trainingLabels):
    givenTrue = []
    givenFalse = []
    countTrue = 0
    countFalse = 0

    # Assigning frequencies of numbers into respective locations in array of dictionaries
    for i in range(0,len(trainingFeatures)):
        # If image is true
        if(trainingLabels[i] == 1):
            countTrue += 1

            # new array
            if(len(givenTrue) == 0):
                for key in range(0, len(trainingFeatures[i])):
                    givenTrue.append({trainingFeatures[i][key]: 1})

            # array already exists
            else:
                for key in range(0, len(trainingFeatures[i])):
                    if(trainingFeatures[i][key] in givenTrue[key]):
                        givenTrue[key].update({trainingFeatures[i][key]: givenTrue[key].get(trainingFeatures[i][key]) + 1})
                    else:
                        givenTrue[key][trainingFeatures[i][key]] = 1
                
        # If image is false
        else:
            countFalse += 1
            if(len(givenFalse) == 0):
                for key in trainingFeatures[i]:
                    givenFalse.append({key: 1})
            else:
                for key in range(0, len(trainingFeatures[i])):
                    if(trainingFeatures[i][key] in givenFalse[key]):
                        givenFalse[key].update({trainingFeatures[i][key]: givenFalse[key].get(trainingFeatures[i][key]) + 1})
                    else:
                        givenFalse[key][trainingFeatures[i][key]] = 1

    # Dividing frequency by count to get probability
    for x in range(0, len(givenTrue)):
        for keys in givenTrue[x]:
            givenTrue[x].update({keys: givenTrue[x][keys] / countTrue})

    for x in range(0, len(givenFalse)):
        for keys in givenFalse[x]:
            givenFalse[x].update({keys: givenFalse[x][keys] / countFalse})


    # Now solving for p(y=true) and p(y=false)
    pyTrue = countTrue / len(trainingFeatures)
    pyFalse = countFalse / len(trainingFeatures)

    return givenTrue, pyTrue, givenFalse, pyFalse

def trainDigit(trainingFeatures,trainingLabels):
    numOfFeatures=len(trainingFeatures[0])
    given0True = [{} for i in range(0,numOfFeatures)]
    given0False = [{} for i in range(0,numOfFeatures)]
    count0True = 0
    count0False = 0
    given1True = [{} for i in range(0,numOfFeatures)]
    given1False = [{} for i in range(0,numOfFeatures)]
    count1True = 0
    count1False = 0
    given2True = [{} for i in range(0,numOfFeatures)]
    given2False = [{} for i in range(0,numOfFeatures)]
    count2True = 0
    count2False = 0
    given3True = [{} for i in range(0,numOfFeatures)]
    given3False = [{} for i in range(0,numOfFeatures)]
    count3True = 0
    count3False = 0
    given4True = [{} for i in range(0,numOfFeatures)]
    given4False = [{} for i in range(0,numOfFeatures)]
    count4True = 0
    count4False = 0
    given5True = [{} for i in range(0,numOfFeatures)]
    given5False = [{} for i in range(0,numOfFeatures)]
    count5True = 0
    count5False = 0
    given6True = [{} for i in range(0,numOfFeatures)]
    given6False = [{} for i in range(0,numOfFeatures)]
    count6True = 0
    count6False = 0
    given7True = [{} for i in range(0,numOfFeatures)]
    given7False = [{} for i in range(0,numOfFeatures)]
    count7True = 0
    count7False = 0
    given8True = [{} for i in range(0,numOfFeatures)]
    given8False = [{} for i in range(0,numOfFeatures)]
    count8True = 0
    count8False = 0
    given9True = [{} for i in range(0,numOfFeatures)]
    given9False = [{} for i in range(0,numOfFeatures)]
    count9True = 0
    count9False = 0

    # Assigning frequencies of numbers into respective locations in array of dictionaries
    for i in range(0,len(trainingFeatures)):
        # If image is 0
        if(trainingLabels[i] == 0):
            count0True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given0True[key]):
                    given0True[key].update({trainingFeatures[i][key]: given0True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given0True[key][trainingFeatures[i][key]] = 1
        # If image is 1
        if(trainingLabels[i] == 1):
            count1True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given1True[key]):
                    given1True[key].update({trainingFeatures[i][key]: given1True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given1True[key][trainingFeatures[i][key]] = 1
        # If image is 2
        if(trainingLabels[i] == 2):
            count2True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given2True[key]):
                    given2True[key].update({trainingFeatures[i][key]: given2True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given2True[key][trainingFeatures[i][key]] = 1
        # If image is 3
        if(trainingLabels[i] == 3):
            count3True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given3True[key]):
                    given3True[key].update({trainingFeatures[i][key]: given3True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given3True[key][trainingFeatures[i][key]] = 1
        # If image is 4
        if(trainingLabels[i] == 4):
            count4True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given4True[key]):
                    given4True[key].update({trainingFeatures[i][key]: given4True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given4True[key][trainingFeatures[i][key]] = 1
        # If image is 5
        if(trainingLabels[i] == 5):
            count5True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given5True[key]):
                    given5True[key].update({trainingFeatures[i][key]: given5True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given5True[key][trainingFeatures[i][key]] = 1
        # If image is 6
        if(trainingLabels[i] == 6):
            count6True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given6True[key]):
                    given6True[key].update({trainingFeatures[i][key]: given6True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given6True[key][trainingFeatures[i][key]] = 1
        # If image is 7
        if(trainingLabels[i] == 7):
            count7True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given7True[key]):
                    given7True[key].update({trainingFeatures[i][key]: given7True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given7True[key][trainingFeatures[i][key]] = 1
        # If image is 8
        if(trainingLabels[i] == 8):
            count8True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given8True[key]):
                    given8True[key].update({trainingFeatures[i][key]: given8True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given8True[key][trainingFeatures[i][key]] = 1
        # If image is 9
        if(trainingLabels[i] == 9):
            count9True += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given9True[key]):
                    given9True[key].update({trainingFeatures[i][key]: given9True[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given9True[key][trainingFeatures[i][key]] = 1
        # If image is not 0
        if(trainingLabels[i] != 0):
            count0False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given0False[key]):
                    given0False[key].update({trainingFeatures[i][key]: given0False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given0False[key][trainingFeatures[i][key]] = 1
         # If image is not 1
        if(trainingLabels[i] != 1):
            count1False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given1False[key]):
                    given1False[key].update({trainingFeatures[i][key]: given1False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given1False[key][trainingFeatures[i][key]] = 1
         # If image is not 2
        if(trainingLabels[i] != 2):
            count2False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given2False[key]):
                    given2False[key].update({trainingFeatures[i][key]: given2False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given2False[key][trainingFeatures[i][key]] = 1
         # If image is not 3
        if(trainingLabels[i] != 3):
            count3False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given3False[key]):
                    given3False[key].update({trainingFeatures[i][key]: given3False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given3False[key][trainingFeatures[i][key]] = 1
         # If image is not 4
        if(trainingLabels[i] != 4):
            count4False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given4False[key]):
                    given4False[key].update({trainingFeatures[i][key]: given4False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given4False[key][trainingFeatures[i][key]] = 1
         # If image is not 5
        if(trainingLabels[i] != 5):
            count5False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given5False[key]):
                    given5False[key].update({trainingFeatures[i][key]: given5False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given5False[key][trainingFeatures[i][key]] = 1
         # If image is not 6
        if(trainingLabels[i] != 6):
            count6False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given6False[key]):
                    given6False[key].update({trainingFeatures[i][key]: given6False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given6False[key][trainingFeatures[i][key]] = 1
         # If image is not 7
        if(trainingLabels[i] != 7):
            count7False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given7False[key]):
                    given7False[key].update({trainingFeatures[i][key]: given7False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given7False[key][trainingFeatures[i][key]] = 1
         # If image is not 8
        if(trainingLabels[i] != 8):
            count8False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given8False[key]):
                    given8False[key].update({trainingFeatures[i][key]: given8False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given8False[key][trainingFeatures[i][key]] = 1
         # If image is not 9
        if(trainingLabels[i] != 9):
            count9False += 1
            for key in range(0, len(trainingFeatures[i])):
                if(trainingFeatures[i][key] in given9False[key]):
                    given9False[key].update({trainingFeatures[i][key]: given9False[key].get(trainingFeatures[i][key]) + 1})
                else:
                    given9False[key][trainingFeatures[i][key]] = 1


    # Dividing frequency by count to get probability
    for x in range(0, numOfFeatures):
        for keys in given0True[x]:
            given0True[x].update({keys: given0True[x][keys] / count0True})
        for keys in given1True[x]:
            given1True[x].update({keys: given1True[x][keys] / count1True})
        for keys in given2True[x]:
            given2True[x].update({keys: given2True[x][keys] / count2True})
        for keys in given3True[x]:
            given3True[x].update({keys: given3True[x][keys] / count3True})
        for keys in given4True[x]:
            given4True[x].update({keys: given4True[x][keys] / count4True})
        for keys in given5True[x]:
            given5True[x].update({keys: given5True[x][keys] / count5True})
        for keys in given6True[x]:
            given6True[x].update({keys: given6True[x][keys] / count6True})
        for keys in given7True[x]:
            given7True[x].update({keys: given7True[x][keys] / count7True})
        for keys in given8True[x]:
            given8True[x].update({keys: given8True[x][keys] / count8True})
        for keys in given9True[x]:
            given9True[x].update({keys: given9True[x][keys] / count9True})
        for keys in given0False[x]:
            given0False[x].update({keys: given0False[x][keys] / count0False})
        for keys in given1False[x]:
            given1False[x].update({keys: given1False[x][keys] / count1False})
        for keys in given2False[x]:
            given2False[x].update({keys: given2False[x][keys] / count2False})
        for keys in given3False[x]:
            given3False[x].update({keys: given3False[x][keys] / count3False})
        for keys in given4False[x]:
            given4False[x].update({keys: given4False[x][keys] / count4False})
        for keys in given5False[x]:
            given5False[x].update({keys: given5False[x][keys] / count5False})
        for keys in given6False[x]:
            given6False[x].update({keys: given6False[x][keys] / count6False})
        for keys in given7False[x]:
            given7False[x].update({keys: given7False[x][keys] / count7False})
        for keys in given8False[x]:
            given8False[x].update({keys: given8False[x][keys] / count8False})
        for keys in given9False[x]:
            given9False[x].update({keys: given9False[x][keys] / count9False})


    # Now solving for p(y=true) and p(y=false)
    py0True = count0True / len(trainingFeatures)
    py0False = count0False / len(trainingFeatures)
    py1True = count1True / len(trainingFeatures)
    py1False = count1False / len(trainingFeatures)
    py2True = count2True / len(trainingFeatures)
    py2False = count2False / len(trainingFeatures)
    py3True = count3True / len(trainingFeatures)
    py3False = count3False / len(trainingFeatures)
    py4True = count4True / len(trainingFeatures)
    py4False = count4False / len(trainingFeatures)
    py5True = count5True / len(trainingFeatures)
    py5False = count5False / len(trainingFeatures)
    py6True = count6True / len(trainingFeatures)
    py6False = count6False / len(trainingFeatures)
    py7True = count7True / len(trainingFeatures)
    py7False = count7False / len(trainingFeatures)
    py8True = count8True / len(trainingFeatures)
    py8False = count8False / len(trainingFeatures)
    py9True = count9True / len(trainingFeatures)
    py9False = count9False / len(trainingFeatures)

    return given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,given0False,given1False,given2False,given3False,given4False,given5False,given6False,given7False,given8False,given9False,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True,py0False,py1False,py2False,py3False,py4False,py5False,py6False,py7False,py8False,py9False

# Solving for L(x)
def predictFace(testFeatures, testLabels, givenTrue, pyTrue, givenFalse, pyFalse):
    lx = []
    for i in range(0,len(testFeatures)):
        trueArr = []
        falseArr = []
        for key in range(0, len(testFeatures[i])):
            if(testFeatures[i][key] in givenTrue[key]):
                trueArr.append(givenTrue[key].get(testFeatures[i][key]))
            else:
                trueArr.append(0.000000001)

            if(testFeatures[i][key] in givenFalse[key]):
                falseArr.append(givenFalse[key].get(testFeatures[i][key]))
            else:
                falseArr.append(0.000000001)
        pGivenTrue = trueArr[0]
        for x in range (1, len(trueArr)):
            pGivenTrue *= trueArr[x]
        pGivenFalse = falseArr[0]
        for x in range (1, len(falseArr)):
            pGivenFalse *= falseArr[x]
        lxCalc = (pGivenTrue * pyTrue) / (pGivenFalse * pyFalse)
        if(lxCalc >= 1):
            lx.append(1)
        else:
            lx.append(0)
    return lx

# Solving for L(x)
def predictDigit(testFeatures,testLabels, given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,given0False,given1False,given2False,given3False,given4False,given5False,given6False,given7False,given8False,given9False,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True,py0False,py1False,py2False,py3False,py4False,py5False,py6False,py7False,py8False,py9False):
    predict = []
    lxCalc=[]
    for i in range(0,len(testFeatures)):
        p0GivenTrue=1
        p0GivenFalse=1
        p1GivenTrue=1
        p1GivenFalse=1
        p2GivenTrue=1
        p2GivenFalse=1
        p3GivenTrue=1
        p3GivenFalse=1
        p4GivenTrue=1
        p4GivenFalse=1
        p5GivenTrue=1
        p5GivenFalse=1
        p6GivenTrue=1
        p6GivenFalse=1
        p7GivenTrue=1
        p7GivenFalse=1
        p8GivenTrue=1
        p8GivenFalse=1
        p9GivenTrue=1
        p9GivenFalse=1
        for key in range(0, len(testFeatures[i])):
            if(testFeatures[i][key] in given0True[key]):
                p0GivenTrue = p0GivenTrue * given0True[key].get(testFeatures[i][key])
            else:
                p0GivenTrue = p0GivenTrue * 0.000000001
            if(testFeatures[i][key] in given0False[key]):
                p0GivenFalse = p0GivenFalse * given0False[key].get(testFeatures[i][key])
            else:
                p0GivenFalse = p0GivenFalse * 0.000000001
            if(testFeatures[i][key] in given1True[key]):
                p1GivenTrue = p1GivenTrue * given1True[key].get(testFeatures[i][key])
            else:
                p1GivenTrue = p1GivenTrue * 0.000000001
            if(testFeatures[i][key] in given1False[key]):
                p1GivenFalse = p1GivenFalse * given1False[key].get(testFeatures[i][key])
            else:
                p1GivenFalse = p1GivenFalse * 0.000000001
            if(testFeatures[i][key] in given2True[key]):
                p2GivenTrue = p2GivenTrue * given2True[key].get(testFeatures[i][key])
            else:
                p2GivenTrue = p2GivenTrue * 0.000000001
            if(testFeatures[i][key] in given2False[key]):
                p2GivenFalse = p2GivenFalse * given2False[key].get(testFeatures[i][key])
            else:
                p2GivenFalse = p2GivenFalse * 0.000000001
            if(testFeatures[i][key] in given3True[key]):
                p3GivenTrue = p3GivenTrue * given3True[key].get(testFeatures[i][key])
            else:
                p3GivenTrue = p3GivenTrue * 0.000000001
            if(testFeatures[i][key] in given3False[key]):
                p3GivenFalse = p3GivenFalse * given3False[key].get(testFeatures[i][key])
            else:
                p3GivenFalse = p3GivenFalse * 0.000000001
            if(testFeatures[i][key] in given4True[key]):
                p4GivenTrue = p4GivenTrue * given4True[key].get(testFeatures[i][key])
            else:
                p4GivenTrue = p4GivenTrue * 0.000000001
            if(testFeatures[i][key] in given4False[key]):
                p4GivenFalse = p4GivenFalse * given4False[key].get(testFeatures[i][key])
            else:
                p4GivenFalse = p4GivenFalse * 0.000000001
            if(testFeatures[i][key] in given5True[key]):
                p5GivenTrue = p5GivenTrue * given5True[key].get(testFeatures[i][key])
            else:
                p5GivenTrue = p5GivenTrue * 0.000000001
            if(testFeatures[i][key] in given5False[key]):
                p5GivenFalse = p5GivenFalse * given5False[key].get(testFeatures[i][key])
            else:
                p5GivenFalse = p5GivenFalse * 0.000000001
            if(testFeatures[i][key] in given6True[key]):
                p6GivenTrue = p6GivenTrue * given6True[key].get(testFeatures[i][key])
            else:
                p6GivenTrue = p6GivenTrue * 0.000000001
            if(testFeatures[i][key] in given6False[key]):
                p6GivenFalse = p6GivenFalse * given6False[key].get(testFeatures[i][key])
            else:
                p6GivenFalse = p6GivenFalse * 0.000000001
            if(testFeatures[i][key] in given7True[key]):
                p7GivenTrue = p7GivenTrue * given7True[key].get(testFeatures[i][key])
            else:
                p7GivenTrue = p7GivenTrue * 0.000000001
            if(testFeatures[i][key] in given7False[key]):
                p7GivenFalse = p7GivenFalse * given7False[key].get(testFeatures[i][key])
            else:
                p7GivenFalse = p7GivenFalse * 0.000000001
            if(testFeatures[i][key] in given8True[key]):
                p8GivenTrue = p8GivenTrue * given8True[key].get(testFeatures[i][key])
            else:
                p8GivenTrue = p8GivenTrue * 0.000000001
            if(testFeatures[i][key] in given8False[key]):
                p8GivenFalse = p8GivenFalse * given8False[key].get(testFeatures[i][key])
            else:
                p8GivenFalse = p8GivenFalse * 0.000000001
            if(testFeatures[i][key] in given9True[key]):
                p9GivenTrue = p9GivenTrue * given9True[key].get(testFeatures[i][key])
            else:
                p9GivenTrue = p9GivenTrue * 0.000000001
            if(testFeatures[i][key] in given9False[key]):
                p9GivenFalse = p9GivenFalse * given9False[key].get(testFeatures[i][key])
            else:
                p9GivenFalse = p9GivenFalse * 0.000000001   
        lxCalc.append((p0GivenTrue * py0True) / (p0GivenFalse * py0False))
        lxCalc.append((p1GivenTrue * py1True) / (p1GivenFalse * py1False))
        lxCalc.append((p2GivenTrue * py2True) / (p2GivenFalse * py2False))
        lxCalc.append((p3GivenTrue * py3True) / (p3GivenFalse * py3False))
        lxCalc.append((p4GivenTrue * py4True) / (p4GivenFalse * py4False))
        lxCalc.append((p5GivenTrue * py5True) / (p5GivenFalse * py5False))
        lxCalc.append((p6GivenTrue * py6True) / (p6GivenFalse * py6False))
        lxCalc.append((p7GivenTrue * py7True) / (p7GivenFalse * py7False))
        lxCalc.append((p8GivenTrue * py8True) / (p8GivenFalse * py8False))
        lxCalc.append((p9GivenTrue * py9True) / (p9GivenFalse * py9False))

        digit=lxCalc.index(max(lxCalc))

        predict.append(digit)
        lxCalc=[]
    return predict
            

            


#def main():
#    trainingData=[([3,8,8,9], 1), ([2,4,6,4], 0), ([4,3,9,9], 1), ([3, 4, 5, 1], 0), ([2,8,1,9], 1)]
#
#    
#    testingData = [([3,8,9,9], 1), ([2, 4, 6, 1], 0), ([4, 3, 9, 9], 1)]
#
#    givenTrue, pyTrue, givenFalse, pyFalse = trainFace(trainingData)
#    print(f"\nP(y=true): {pyTrue}")
#    print(f'givenTrue: {givenTrue}')
#    print(f"\nP(y=false): {pyFalse}")
#    print(f'givenFalse: {givenFalse}')
#
#
#    lx = predictFace(testingData, givenTrue, pyTrue, givenFalse, pyFalse,)
#
#    print(f"\n\n\nlx: {lx}")
#
#
#if __name__ == '__main__':
#    main()