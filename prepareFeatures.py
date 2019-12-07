import util
import random
import featureFuncLib
import NaiveBayes
import kNN
import Perceptron

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

def runNBFace(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    givenTrue, pyTrue, givenFalse, pyFalse=NaiveBayes.trainFace(trainFeatures,trainingLabels)
    predict=NaiveBayes.predictFace(testFeatures, testLabels, givenTrue, pyTrue, givenFalse, pyFalse)
    print(percentCorrect(testLabels,predict))

def runNBDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True=NaiveBayes.trainDigit(trainFeatures,trainingLabels)
    predict=NaiveBayes.predictDigit(testFeatures,testLabels,given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True)
    print(percentCorrect(testLabels,predict))

def runPerceptronFace(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    weights=Perceptron.makeTrainFunctionFace(trainFeatures,trainingLabels)
    predict=Perceptron.predictFace(testFeatures, testLabels,weights)
    print(percentCorrect(testLabels,predict))

def runPerceptronDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9=Perceptron.makeTrainFunctionDigits(trainFeatures,trainingLabels)
    predict=Perceptron.predictDigit(testFeatures, testLabels,weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9)
    print(percentCorrect(testLabels,predict))

def runkNNFace(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    kvalue=1
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    print(percentCorrect(testLabels,predict))

def runkNNDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    kvalue = 1
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    print(percentCorrect(testLabels,predict))

def main():
    # runNBFace(450,100)
    # 0.88
    # 
    runNBDigit(450,100)
    # 0.58 (train set=450), 0.81 (training set=5000)
    # 
    # runPerceptronFace(450,100)
    # 0.71 (timeout=500) > 0.73 (timeout=50) --> 0.82
    # 
    # runPerceptronDigit(450,100)
    # 0.76 --> 0.8
    # 
    # runkNNFace(450,100)
    # 0.72
    # 
    # runkNNDigit(450,100)
    # 0.79
    # 

if __name__ == '__main__':
    main()