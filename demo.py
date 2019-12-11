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
    return percentCorrect(testLabels,predict),abs(end-start)

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
    return percentCorrect(testLabels,predict),abs(end-start)

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
    return percentCorrect(testLabels,predict),abs(end-start)

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
    return percentCorrect(testLabels,predict),abs(end-start)

def runkNNFace(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    kvalue=1
    start = time.time()
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    end = time.time()
    kNNpredictTimePerImage = abs(end-start) / len(predict)
    return percentCorrect(testLabels,predict),kNNpredictTimePerImage

def runkNNDigit(percent,trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = featureFuncLib.basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    trainFeatures,trainingLabels=xPercent(percent,trainFeatures,trainingLabels)
    kvalue = 1
    start = time.time()
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,kvalue)
    end = time.time()
    kNNpredictTimePerImage = abs(end-start) / len(predict)
    return percentCorrect(testLabels,predict),kNNpredictTimePerImage

def main():
    # file output
    outfile = open('FaceDigitClassification.log','w+')

    print("===================================================================")
    print("NB face:")
    print("-- classifier: Naive Bayes Algorithm")
    print("-- image type: face")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("NB face:", file=outfile)
    print("-- classifier: Naive Bayes Algorithm", file=outfile)
    print("-- image type: face", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runNBFace(i/10,450,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    print("===================================================================")
    print("NB digit:")
    print("-- classifier: Naive Bayes Algorithm")
    print("-- image type: digit")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("NB digit:", file=outfile)
    print("-- classifier: Naive Bayes Algorithm", file=outfile)
    print("-- image type: digit", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runNBDigit(i/10,5000,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    print("===================================================================")
    print("Perceptron face:")
    print("-- classifier: Perceptron Algorithm")
    print("-- image type: face")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("Perceptron face:", file=outfile)
    print("-- classifier: Perceptron Algorithm", file=outfile)
    print("-- image type: face", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runPerceptronFace(i/10,450,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    print("===================================================================")
    print("Perceptron digit:")
    print("-- classifier: Perceptron Algorithm")
    print("-- image type: digit")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("Perceptron digit:", file=outfile)
    print("-- classifier: Perceptron Algorithm", file=outfile)
    print("-- image type: digit", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runPerceptronDigit(i/10,5000,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", training time (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE TRAINING TIME (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    print("===================================================================")
    print("kNN face")
    print("-- classifier: kNN")
    print("-- image type: face")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("kNN face", file=outfile)
    print("-- classifier: kNN", file=outfile)
    print("-- image type: face", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runkNNFace(i/10,450,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", predict time per image (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", predict time per image (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE PREDICTION TIME PER IMAGE (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE PREDICTION TIME PER IMAGE (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    print("===================================================================")
    print("kNN digit")
    print("-- classifier: kNN")
    print("-- image type: digit")
    print("-------------------------------------------------------------------")
    print("===================================================================", file=outfile)
    print("kNN digit", file=outfile)
    print("-- classifier: kNN", file=outfile)
    print("-- image type: digit", file=outfile)
    print("-------------------------------------------------------------------", file=outfile)
    # for i in range(1,11):
    for i in range(10,11):
        print("TRAINING SIZE: "+str(i)+"0%")
        print("TRAINING SIZE: "+str(i)+"0%", file=outfile)
        acc=[]
        t=[]
        for j in range(5):
            accuracy,time=runkNNDigit(i/10,5000,100)
            acc.append(accuracy)
            t.append(time)
            error=1-accuracy
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", predict time per image (seconds)="+str(round(time,3)))
            print("  Trial "+str(j)+": accuracy="+str(round(accuracy,2))+", error="+str(round(error,2))+", predict time per image (seconds)="+str(round(time,3)), file=outfile)
        mean_acc=sum(acc) / len(acc)
        stdev=numpy.std(acc)
        mean_error=1-mean_acc
        avgtime=sum(t)/len(t)
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE PREDICTION TIME PER IMAGE (SECONDS)="+str(round(avgtime,3)))
        print("  ** SUMMARY: MEAN ACCURACY="+str(round(mean_acc,2))+", STANDARD DEVIATION="+str(round(stdev,2))+", MEAN ERROR="+str(round(mean_error,2))+", AVERAGE PREDICTION TIME PER IMAGE (SECONDS)="+str(round(avgtime,3)), file=outfile)
    print("===================================================================")
    print("===================================================================", file=outfile)
    print()
    print(' ', file=outfile)

    outfile.close()
            

if __name__ == '__main__':
    main()
