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
def makeTrainFunctionFace(train):
    w0 = 0
    weights = [0.001 for i in len(extractFeatures(train[0]))]
    for (image, isFace) in train:
        features = extractFeatures(image)
        for i in weights:
            f = w0 + weights[i]*features[i]
            if(f >= 0 and isFace == 1):
                continue
            elif(f < 0 and isFace == 0):
                continue
            elif(f < 0 and isFace == 1):
                weights[i] = weights[i] + features[i]
                w0 = w0 + 1
            else:
                weights[i] = weights[i] - features[i]
                w0 = w0 - 1
    weights.append(w0)
    return weights

def makeTrainFunctionDigits(train, weights0, weights1, weights2, weights3, weights5, weights6, weights7, weights8, weights9):
    weights = [.001 for i in range(10)]
    w0 = 0
    w1 = 0
    w2 = 0
    w3 = 0
    w4 = 0
    w5 = 0
    w6 = 0
    w7 = 0
    w8 = 0
    w9 = 0
    image0 = 0
    image1 = 0
    image2 = 0
    image3 = 0
    image4 = 0
    image5 = 0
    image6 = 0
    image7 = 0
    image8 = 0
    image9 = 0
    weights0 = [0.001 for i in len(extractFeatures(train[0]))]
    weights1 = [0.001 for i in len(extractFeatures(train[0]))]
    weights2 = [0.001 for i in len(extractFeatures(train[0]))]
    weights3 = [0.001 for i in len(extractFeatures(train[0]))]
    weights4 = [0.001 for i in len(extractFeatures(train[0]))]
    weights5 = [0.001 for i in len(extractFeatures(train[0]))]
    weights6 = [0.001 for i in len(extractFeatures(train[0]))]
    weights7 = [0.001 for i in len(extractFeatures(train[0]))]
    weights8 = [0.001 for i in len(extractFeatures(train[0]))]
    weights9 = [0.001 for i in len(extractFeatures(train[0]))]
    for (image, isDigit) in train:
        features = extractFeatures(image)
        if(image0 == 0):
            for i in weights0:
                f = w0 + weights0[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights0[i] = weights0[i] + features[i]
                    w0 = w0 + 1
                else:
                    weights0[i] = weights0[i] - features[i]
                    w0 = w0 - 1
            image = 1
            weights0.append(w0)
        elif(image1 == 0):
            for i in weights1:
                f = w1 + weights1[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights1[i] = weights1[i] + features[i]
                    w1 = w1 + 1
                else:
                    weights1[i] = weights1[i] - features[i]
                    w1 = w1 - 1
            image1 = 1
            weights1.append(w1)
        elif(image2 == 0):
            for i in weights2:
                f = w2 + weights2[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights2[i] = weights2[i] + features[i]
                    w2 = w2 + 1
                else:
                    weights1[i] = weights2[i] - features[i]
                    w2 = w2 - 1
            image2 = 1
            weights2.append(w2)
        elif(image3 == 0):
            for i in weights3:
                f = w3 + weights3[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights3[i] = weights3[i] + features[i]
                    w3 = w3 + 1
                else:
                    weights3[i] = weights3[i] - features[i]
                    w3 = w3 - 1
            image3 = 1
            weights3.append(w3)
        elif(image4 == 0):
            for i in weights4:
                f = w4 + weights4[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights4[i] = weights4[i] + features[i]
                    w4 = w4 + 1
                else:
                    weights4[i] = weights4[i] - features[i]
                    w4 = w4 - 1
            image4 = 1
            weights4.append(w4)
        elif(image5 == 0):
            for i in weights5:
                f = w5 + weights5[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights5[i] = weights5[i] + features[i]
                    w5 = w5 + 1
                else:
                    weights5[i] = weights5[i] - features[i]
                    w5 = w5 - 1
            image5 = 1
            weights5.append(w5)
        elif(image6 == 0):
            for i in weights6:
                f = w6 + weights6[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights6[i] = weights6[i] + features[i]
                    w6 = w6 + 1
                else:
                    weights6[i] = weights6[i] - features[i]
                    w6 = w6 - 1
            image6 = 1
            weights6.append(w6)
        elif(image7 == 0):
            for i in weights7:
                f = w7 + weights7[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights7[i] = weights7[i] + features[i]
                    w7 = w7 + 1
                else:
                    weights7[i] = weights7[i] - features[i]
                    w7 = w7 - 1
            image7 = 1
            weights7.append(w7)
        elif(image8 == 0):
            for i in weights8:
                f = w8 + weights8[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights8[i] = weights8[i] + features[i]
                    w8 = w8 + 1
                else:
                    weights8[i] = weights8[i] - features[i]
                    w8 = w8 - 1
            image8 = 1
            weights8.append(w8)
        elif(image9 == 0):
            for i in weights9:
                f = w9 + weights9[i]*features[i]
                if(f >= 0 and isFace == 1):
                    continue
                elif(f < 0 and isFace == 0):
                    continue
                elif(f < 0 and isFace == 1):
                    weights9[i] = weights9[i] + features[i]
                    w9 = w9+ 1
                else:
                    weights9[i] = weights9[i] - features[i]
                    w9 = w9 - 1
            image9 = 1
            weights9.append(w9)

    return weights0, weights1, weights2, weights3, weights3, weights5, weights6, weights7, weights8, weights9


### method that given the test set, predicts whether the images are a face or not 
###PARAMETERs: 
#   1. test array of [(image,isFace),(image,isFace),(image,isFace)...]
#   2. array of weights
###RETURNS: 
#   1. the predicted values

def predictFace(test,weights):
    predict=[]
    fvalues = []
    w0 = weights[len(weights)-1]
    for (image, isFace) in test:
        features = extractFeatures(image)
        for i in weights:
            f = w0 + weights[i]*features[i]
            if(f >= 0):
                predict.append(1)
            elif(f < 0):
                predict.append(0)
            fvalues.append(f)
    return predict

def predictDigit(test, weights0, weights1, weights2, weights3, weights5, weights6, weights7, weights8, weights9):
    predict = []
    w0 = weights0[len(weights0)-1]
    w1 = weights1[len(weights1)-1]
    w2 = weights2[len(weights2)-1]
    w3 = weights3[len(weights3)-1]
    w4 = weights4[len(weights4)-1]
    w5 = weights5[len(weights5)-1]
    w6 = weights6[len(weights6)-1]
    w7 = weights7[len(weights7)-1]
    w8 = weights8[len(weights8)-1]
    w9 = weights9[len(weights9)-1]
    image0 = 0
    image1 = 0
    image2 = 0
    image3 = 0
    image4 = 0
    image5 = 0
    image6 = 0
    image7 = 0
    image8 = 0
    image9 = 0
    for (image, isDigit) in test:
        features = extractFeatures(image)
        if(image0 == 0):
            fvalues = []
            for i in weights0:
                f = w0 + weights0[i]*features[i]
                fvalues.append(f)
                if(f >= 0):
                    predict.append(0)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image = 1
            weights0.append(w0)
        elif(image1 == 0):
            fvalues = []
            for i in weights1:
                f = w1 + weights1[i]*features[i]
                if(f >= 0):
                    predict.append(1)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image1 = 1
            weights1.append(w1)
        elif(image2 == 0):
            fvalues = []
            for i in weights2:
                f = w2 + weights2[i]*features[i]
                if(f >= 0):
                    predict.append(2)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image2 = 1
        elif(image3 == 0):
            fvalues = []
            for i in weights3:
                f = w3 + weights3[i]*features[i]
                if(f >= 0):
                    predict.append(3)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image3 = 1
        elif(image4 == 0):
            for i in weights4:
                f = w4 + weights4[i]*features[i]
                if(f >= 0):
                    predict.append(4)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image4 = 1
            weights4.append(w4)
        elif(image5 == 0):
            fvalues = []
            for i in weights5:
                f = w5 + weights5[i]*features[i]
                if(f >= 0):
                    predict.append(5)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image5 = 1
        elif(image6 == 0):
            fvalues = []
            for i in weights6:
                f = w6 + weights6[i]*features[i]
                if(f >= 0):
                    predict.append(6)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image6 = 1
        elif(image7 == 0):
            fvalues = []
            for i in weights7:
                f = w7 + weights7[i]*features[i]
                if(f >= 0):
                    predict.append(7)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image7 = 1
        elif(image8 == 0):
            fvalues = []
            for i in weights8:
                f = w8 + weights8[i]*features[i]
                if(f >= 0):
                    predict.append(8)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image8 = 1
        elif(image9 == 0):
            fvalues = []
            for i in weights9:
                f = w9 + weights9[i]*features[i]
                if(f >= 0):
                    predict.append(9)
                elif(f < 0):
                    fmax = max(fvalues)
                    predict.append(fvalues.index(fmax))
            image9 = 1



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
