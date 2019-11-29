import random

### method to split into training and test set
###PARAMETERS: 
#   1. array of [(image,isFace),(image,isFace),(image,isFace)...]
#   2. percentage; x% goes into the train set, the rest go into the test set
###RETURNS: 
#   1. train array of [(image,isFace),(image,isFace),(image,isFace)...] 
#   2. test array of [(image,isFace),(image,isFace),(image,isFace)...]
def selectTrainTest(array,percentage):
    random.shuffle(array)
    split=percentage*len(array)
    i=0
    train=[]
    test=[]
    for item in array:
        if (i<split):
            train.append(item)
        else:
            test.append(item)
    return train,test



### method to extract features from images
###PARAMETER:
#   1. image
###RETURNS:
#   2. array of features for that image
def extractFeatures(image):
    array=[]
    ################################################
    return array

### method that given the train set, returns the function that we can use to predict whether an item in the test set is a face or not
###PARAMETER: 
#   1. train array of [(image,isFace),(image,isFace),(image,isFace)...]
###RETURNS: 
#   1. an array of weights for the function that predicts whether an image is a face or not
def makeTrainFunctionFace(trainFeatures,trainLabels):
    length=len(trainFeatures)
    #assume that there is at least one image... NO ERROR CHECKING YET
    numOfFeatures=len(trainFeatures[0])
    weights=[]
    #initialize all weights to be 0
    weights = [0.0001 for i in range(0,numOfFeatures+1)]
    timeLimit=50
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]!=0) or (f<0 and trainLabels[i]==0)):
                continue
            if (f<0 and trainLabels[i]!=0):
                update=1
                for k in range(0,numOfFeatures):
                    weights[k+1]=weights[k+1]+trainFeatures[i][k]
                weights[0]=weights[0]+1
            if (f>=0 and trainLabels[i]==0):
                update=1
                for k in range(0,numOfFeatures):
                    weights[k+1]=weights[k+1]-trainFeatures[i][k]
                weights[0]=weights[0]-1
        if (update==0):
            break
        else:
            update=0
    return weights
    
def makeTrainFunctionDigits(trainFeatures,trainLabels):
    length=len(trainFeatures)
    #assume that there is at least one image... NO ERROR CHECKING YET
    numOfFeatures=len(trainFeatures[0])
    #initialize all weights to be 0
    weights0 = [0.001 for i in range(0,numOfFeatures+1)]
    weights1 = [0.001 for i in range(0,numOfFeatures+1)]
    weights2 = [0.001 for i in range(0,numOfFeatures+1)]
    weights3 = [0.001 for i in range(0,numOfFeatures+1)]
    weights4 = [0.001 for i in range(0,numOfFeatures+1)]
    weights5 = [0.001 for i in range(0,numOfFeatures+1)]
    weights6 = [0.001 for i in range(0,numOfFeatures+1)]
    weights7 = [0.001 for i in range(0,numOfFeatures+1)]
    weights8 = [0.001 for i in range(0,numOfFeatures+1)]
    weights9 = [0.001 for i in range(0,numOfFeatures+1)]
    timeLimit=50
    #GET WEIGHTS FOR DIGIT 0
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights0[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights0[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==0) or (f<0 and trainLabels[i]!=0)):
                continue
            if (f<0 and trainLabels[i]==0):
                update=1
                for k in range(0,numOfFeatures):
                    weights0[k+1]=weights0[k+1]+trainFeatures[i][k]
                weights0[0]=weights0[0]+1
            if (f>=0 and trainLabels[i]!=0):
                update=1
                for k in range(0,numOfFeatures):
                    weights0[k+1]=weights0[k+1]-trainFeatures[i][k]
                weights0[0]=weights0[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 1
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights1[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights1[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==1) or (f<0 and trainLabels[i]!=1)):
                continue
            if (f<0 and trainLabels[i]==1):
                update=1
                for k in range(0,numOfFeatures):
                    weights1[k+1]=weights1[k+1]+trainFeatures[i][k]
                weights1[0]=weights1[0]+1
            if (f>=0 and trainLabels[i]!=1):
                update=1
                for k in range(0,numOfFeatures):
                    weights1[k+1]=weights1[k+1]-trainFeatures[i][k]
                weights1[0]=weights1[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 2
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights2[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights2[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==2) or (f<0 and trainLabels[i]!=2)):
                continue
            if (f<0 and trainLabels[i]==2):
                update=1
                for k in range(0,numOfFeatures):
                    weights2[k+1]=weights2[k+1]+trainFeatures[i][k]
                weights2[0]=weights2[0]+1
            if (f>=0 and trainLabels[i]!=2):
                update=1
                for k in range(0,numOfFeatures):
                    weights2[k+1]=weights2[k+1]-trainFeatures[i][k]
                weights2[0]=weights2[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 3
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights3[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights3[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==3) or (f<0 and trainLabels[i]!=3)):
                continue
            if (f<0 and trainLabels[i]==3):
                update=1
                for k in range(0,numOfFeatures):
                    weights3[k+1]=weights3[k+1]+trainFeatures[i][k]
                weights3[0]=weights3[0]+1
            if (f>=0 and trainLabels[i]!=3):
                update=1
                for k in range(0,numOfFeatures):
                    weights3[k+1]=weights3[k+1]-trainFeatures[i][k]
                weights3[0]=weights3[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 4
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights4[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights4[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==4) or (f<0 and trainLabels[i]!=4)):
                continue
            if (f<0 and trainLabels[i]==4):
                update=1
                for k in range(0,numOfFeatures):
                    weights4[k+1]=weights4[k+1]+trainFeatures[i][k]
                weights4[0]=weights4[0]+1
            if (f>=0 and trainLabels[i]!=4):
                update=1
                for k in range(0,numOfFeatures):
                    weights4[k+1]=weights4[k+1]-trainFeatures[i][k]
                weights4[0]=weights4[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 5
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights5[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights5[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==5) or (f<0 and trainLabels[i]!=5)):
                continue
            if (f<0 and trainLabels[i]==5):
                update=1
                for k in range(0,numOfFeatures):
                    weights5[k+1]=weights5[k+1]+trainFeatures[i][k]
                weights5[0]=weights5[0]+1
            if (f>=0 and trainLabels[i]!=5):
                update=1
                for k in range(0,numOfFeatures):
                    weights5[k+1]=weights5[k+1]-trainFeatures[i][k]
                weights5[0]=weights5[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 6
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights6[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights6[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==6) or (f<0 and trainLabels[i]!=6)):
                continue
            if (f<0 and trainLabels[i]==6):
                update=1
                for k in range(0,numOfFeatures):
                    weights6[k+1]=weights6[k+1]+trainFeatures[i][k]
                weights6[0]=weights6[0]+1
            if (f>=0 and trainLabels[i]!=6):
                update=1
                for k in range(0,numOfFeatures):
                    weights6[k+1]=weights6[k+1]-trainFeatures[i][k]
                weights6[0]=weights6[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 7
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights7[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights7[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==7) or (f<0 and trainLabels[i]!=7)):
                continue
            if (f<0 and trainLabels[i]==7):
                update=1
                for k in range(0,numOfFeatures):
                    weights7[k+1]=weights7[k+1]+trainFeatures[i][k]
                weights7[0]=weights7[0]+1
            if (f>=0 and trainLabels[i]!=7):
                update=1
                for k in range(0,numOfFeatures):
                    weights7[k+1]=weights7[k+1]-trainFeatures[i][k]
                weights7[0]=weights7[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 8
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights8[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights8[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==8) or (f<0 and trainLabels[i]!=8)):
                continue
            if (f<0 and trainLabels[i]==8):
                update=1
                for k in range(0,numOfFeatures):
                    weights8[k+1]=weights8[k+1]+trainFeatures[i][k]
                weights8[0]=weights8[0]+1
            if (f>=0 and trainLabels[i]!=8):
                update=1
                for k in range(0,numOfFeatures):
                    weights8[k+1]=weights8[k+1]-trainFeatures[i][k]
                weights8[0]=weights8[0]-1
        if (update==0):
            break
        else:
            update=0
    #GET WEIGHTS FOR DIGIT 9
    update=0
    for iteration in range(0,timeLimit):
        for i in range(0,length):
            f=weights9[0]
            #compute f
            for j in range(0,numOfFeatures):
                f=f+weights9[j+1]*trainFeatures[i][j]
            if ((f>=0 and trainLabels[i]==9) or (f<0 and trainLabels[i]!=9)):
                continue
            if (f<0 and trainLabels[i]==9):
                update=1
                for k in range(0,numOfFeatures):
                    weights9[k+1]=weights9[k+1]+trainFeatures[i][k]
                weights9[0]=weights9[0]+1
            if (f>=0 and trainLabels[i]!=9):
                update=1
                for k in range(0,numOfFeatures):
                    weights9[k+1]=weights9[k+1]-trainFeatures[i][k]
                weights9[0]=weights9[0]-1
        if (update==0):
            break
        else:
            update=0
    return weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9


### method that given the test set, predicts whether the images are a face or not 
###PARAMETERs: 
#   1. test array of [(image,isFace),(image,isFace),(image,isFace)...]
#   2. array of weights
###RETURNS: 
#   1. the predicted values

def predictFace(testFeatures,testLabels,weights):
    predict=[]
    for i in range(0,len(testFeatures)):
        f=weights[0]
        for j in range(0,len(testFeatures[i])):
             f=f+weights[j+1]*testFeatures[i][j]
        if (f>=0):
            predict.append(1)
        else:
            predict.append(0)
    return predict

def predictDigit(testFeatures,testLabels,weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9):
    predict=[]
    for i in range(0,len(testFeatures)):
        f0=weights0[0]
        f1=weights1[0]
        f2=weights2[0]
        f3=weights3[0]
        f4=weights4[0]
        f5=weights5[0]
        f6=weights6[0]
        f7=weights7[0]
        f8=weights8[0]
        f9=weights9[0]
        for j in range(0,len(testFeatures[i])):
             f0=f0+weights0[j+1]*testFeatures[i][j]
             f1=f1+weights1[j+1]*testFeatures[i][j]
             f2=f2+weights2[j+1]*testFeatures[i][j]
             f3=f3+weights3[j+1]*testFeatures[i][j]
             f4=f4+weights4[j+1]*testFeatures[i][j]
             f5=f5+weights5[j+1]*testFeatures[i][j]
             f6=f6+weights6[j+1]*testFeatures[i][j]
             f7=f7+weights7[j+1]*testFeatures[i][j]
             f8=f8+weights8[j+1]*testFeatures[i][j]
             f9=f9+weights9[j+1]*testFeatures[i][j]
        m=max(f0,f1,f2,f3,f4,f5,f6,f7,f8,f9)
        if (m==f0): 
            predict.append(0)
        elif (m==f1): 
            predict.append(1)
        elif (m==f2): 
            predict.append(2)
        elif (m==f3): 
            predict.append(3)
        elif (m==f4): 
            predict.append(4)
        elif (m==f5): 
            predict.append(5)
        elif (m==f6): 
            predict.append(6)
        elif (m==f7): 
            predict.append(7)
        elif (m==f8): 
            predict.append(8)
        else:
            predict.append(9)
    return predict

###method that given the test set and predicted values, returns the error
###PARAMETERS:
#   1. the test set
#   2. the predicted values
###RETURNS:
#   1. the error

def findError(test,predict):
    testCorrect=0
    predictCorrect=0
    for i in range(0,len(test)):
        if (test[i][1]!=0):
            testCorrect=testCorrect+1
        if (predict[i]!=0):
            predictCorrect=predictCorrect+1
    return abs(testCorrect-predictCorrect)/testCorrect #NOT SURE IF THIS IS CALCULATING ERROR CORRECTLY
        

    
    
