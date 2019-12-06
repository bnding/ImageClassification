import util
import random
import featureFuncLib
import NaiveBayes
import kNN
import Perceptron
import math
import numpy
import time

DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

def extractImages(options_data,trainsize,testsize): #options_data is either "faces" or "digit"
    options_training = trainsize
    options_test = testsize
    numTraining = options_training
    numTest = options_test

    if (options_data=="faces"):
        rawTrainingData = util.loadDataFile("facedata/facedatatrain", numTraining,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        trainingLabels = util.loadLabelsFile("facedata/facedatatrainlabels", numTraining)
        # rawValidationData = util.loadDataFile("facedata/facedatatrain", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        # validationLabels = util.loadLabelsFile("facedata/facedatatrainlabels", numTest)
        rawTestData = util.loadDataFile("facedata/facedatatest", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        testLabels = util.loadLabelsFile("facedata/facedatatestlabels", numTest)
    else:
        rawTrainingData = util.loadDataFile("digitdata/trainingimages", numTraining,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
        trainingLabels = util.loadLabelsFile("digitdata/traininglabels", numTraining)
        # rawValidationData = util.loadDataFile("digitdata/validationimages", numTest,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
        # validationLabels = util.loadLabelsFile("digitdata/validationlabels", numTest)
        rawTestData = util.loadDataFile("digitdata/testimages", numTest,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
        testLabels = util.loadLabelsFile("digitdata/testlabels", numTest)
    return rawTrainingData,trainingLabels,rawTestData,testLabels

def findError(test,predict):
    testCorrect=0
    predictCorrect=0
    for i in range(0,len(test)):
        if (test[i]!=0):
            testCorrect=testCorrect+1
        if (predict[i]!=0):
            predictCorrect=predictCorrect+1
    return abs(testCorrect-predictCorrect)/testCorrect #NOT SURE IF THIS IS CALCULATING ERROR CORRECTLY

def percentCorrect(test,predict):
    guessCorrect=0
    for i in range(0,len(test)):
        if (test[i]==predict[i]):
            guessCorrect=guessCorrect+1
    return guessCorrect/len(test)

def xPercent(percent,trainFeatures,trainLabels):
    newTrainSize=math.floor(percent*len(trainFeatures))
    newTrainFeatures=[]
    newTrainLabels=[]
    x=random.sample(range(len(trainFeatures)), newTrainSize)
    for item in x:
        newTrainFeatures.append(trainFeatures[item])
        newTrainLabels.append(trainLabels[item])
    return newTrainFeatures,newTrainLabels

def runNBFace(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    start = time.time()
    givenTrue, pyTrue, givenFalse, pyFalse=NaiveBayes.trainFace(trainFeatures,trainingLabels)
    end = time.time()
    predict=NaiveBayes.predictFace(testFeatures, testLabels, givenTrue, pyTrue, givenFalse, pyFalse)
    return percentCorrect(testLabels,predict),abs(start-end)

def runNBDigit(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    start = time.time()
    given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True=NaiveBayes.trainDigit(trainFeatures,trainingLabels)
    end = time.time()
    predict=NaiveBayes.predictDigit(testFeatures,testLabels,given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True)
    return percentCorrect(testLabels,predict),abs(start-end)

def runPerceptronFace(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    start = time.time()
    weights=Perceptron.makeTrainFunctionFace(trainFeatures,trainingLabels)
    end = time.time()
    predict=Perceptron.predictFace(testFeatures, testLabels,weights)
    return percentCorrect(testLabels,predict),abs(start-end)

def runPerceptronDigit(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    start = time.time()
    weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9=Perceptron.makeTrainFunctionDigits(trainFeatures,trainingLabels)
    end = time.time()
    predict=Perceptron.predictDigit(testFeatures, testLabels,weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9)
    return percentCorrect(testLabels,predict),abs(start-end)

def runkNNFace(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    kvalue=1
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    return percentCorrect(testLabels,predict)

def runkNNDigit(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    kvalue = 1
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    return percentCorrect(testLabels,predict)

def main():
    for i in range(1,11):
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runNBFace(i/10,450,100)
            acc.append(accuracy)
            t.append(time)
            print("NB face, trial "+str(j)+", training size "+str(i)+"0%, train time, "+str(time)+", accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        avgtime=sum(t)/len(t)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev)+", AVERAGE TRAINING TIME "+str(avgtime))
    for i in range(1,11):
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runNBDigit(i/10,5000,100)
            acc.append(accuracy)
            t.append(time)
            print("NB digit, trial "+str(j)+", training size "+str(i)+"0%, train time, "+str(time)+", accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        avgtime=sum(t)/len(t)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev)+", AVERAGE TRAINING TIME "+str(avgtime))
    for i in range(1,11):
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runPerceptronFace(i/10,450,100)
            acc.append(accuracy)
            t.append(time)
            print("Perceptron face, trial "+str(j)+", training size "+str(i)+"0%, train time, "+str(time)+", accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        avgtime=sum(t)/len(t)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev)+", AVERAGE TRAINING TIME "+str(avgtime))
    for i in range(1,11):
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runPerceptronDigit(i/10,5000,100)
            acc.append(accuracy)
            t.append(time)
            print("Perceptron digit, trial "+str(j)+", training size "+str(i)+"0%, train time, "+str(time)+", accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        avgtime=sum(t)/len(t)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev)+", AVERAGE TRAINING TIME "+str(avgtime))
    for i in range(1,11):
        acc=[]
        for j in range(5):
            accuracy=runkNNFace(i/10,450,100)
            acc.append(accuracy)
            print("kNN face, trial "+str(j)+", training size "+str(i)+"0%, accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev))
    for i in range(1,11):
        acc=[]
        for j in range(5):
            accuracy=runkNNDigit(i/10,5000,100)
            acc.append(accuracy)
            print("kNN digit, trial "+str(j)+", training size "+str(i)+"0%, accuracy "+str(accuracy))
        mean=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        print("TRAINING SIZE "+str(i)+"0%, MEAN ACCURACY "+str(mean)+", STANDARD DEVIATION ACCURACY "+str(stdev))

            
    #runNBFace(450,100)
    # 0.88
    # 
    #runNBDigit(5000,100)
    # 0.58 (train set=450), 0.81 (training set=5000)
    # 
    #runPerceptronFace(450,100)
    # 0.71 (timeout=500) > 0.73 (timeout=50) --> 0.82
    # 
    #runPerceptronDigit(5000,100)
    # 0.76 --> 0.8
    # 
    #runkNNFace(450,100)
    # 0.72
    # 
    #runkNNDigit(5000,100)
    # 0.79
    #

if __name__ == '__main__':
    main()
