import random
import operator
import math

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

### method that given the test set, predicts whether the images are a face or not 
###PARAMETERs: 
#   1. train array of [(image,isFace),(image,isFace),(image,isFace)...]
#   2. test array of [(image,isFace),(image,isFace),(image,isFace)...]
###RETURNS: 
#   1. the predicted values

def predict(trainFeatures,trainLabels,testFeatures,testLabels,kvalue):
    predict=[]
    #FOR EACH IMAGE THAT YOU WANT TO PREDICT
    for i in range(0,len(testFeatures)):
        featureArrayCurrent=testFeatures[i]
        q=[]
        #LOOK AT EACH IMAGE IN THE TRAINING SET
        for j in range(0,len(trainFeatures)):
            featureArrayCompare=trainFeatures[j]
            distance=0
            #CALCULATE THE SIMILARITY BETWEEN THE IMAGE IN THE TEST SET AND IN THE TRAINING SET
            for k in range(0,len(featureArrayCurrent)):
                distance=distance+math.pow(abs(featureArrayCurrent[k]-featureArrayCompare[k]),2)
            #IF THIS IS ONE OF THE K MOST SIMILAR IMAGES, ADD IT TO THE ARRAY OF K MOST SIMILAR IMAGES
            if (len(q)<kvalue or q[0][0]>distance):  
                if (len(q)<kvalue):
                    q.append((distance,j))
                elif (q[0][0]>distance):
                    q[0]=(distance,j)
                q.sort(key = operator.itemgetter(0),reverse=True)
        kDict={}
        for item in q:
            if (kDict.get(str(trainLabels[item[1]]))==None): #IF THE DIGIT IS NOT IN THE DICTIONARY YET
                kDict[str(trainLabels[item[1]])]=1
            else: #THE DIGIT IS IN THE DICTIONARY
                kDict[str(trainLabels[item[1]])]=kDict[str(trainLabels[item[1]])]+1
        #FIND THE DIGIT THAT APPEARS MOST OFTEN IN THE K MOST SIMILAR IMAGES
        predict.append(int(max(kDict, key=kDict.get)))
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
        
