import util
import random
import NaiveBayes
import kNN
import Perceptron

TEST_SET_SIZE = 100
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

def basicFeatureExtractorDigit(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is white (0) or gray/black (1)
  """
  a = datum.getPixels()

  features = []
  #feature1
  black=0
  for x in range(0,7):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  
  for x in range(0,7):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  
  for x in range(0,7):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  
  for x in range(0,7):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  
  for x in range(7,14):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  
  for x in range(7,14):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  
  for x in range(7,14):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature8
  black=0
  
  for x in range(7,14):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature9
  black=0
  
  for x in range(14,21):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature10
  black=0
  
  for x in range(14,21):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature11
  black=0
  
  for x in range(14,21):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature12
  black=0
  
  for x in range(14,21):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature13
  black=0
  
  for x in range(21,28):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  
  for x in range(21,28):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  
  for x in range(21,28):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  
  for x in range(21,28):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  return features

def basicFeatureExtractorDigit_2(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is white (0) or gray/black (1)
  """
  a = datum.getPixels()

  features = []
  #feature1
  black=0
  for x in range(0,4):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  
  for x in range(0,4):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  
  for x in range(0,4):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  
  for x in range(0,4):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  
  for x in range(4,8):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  
  for x in range(4,8):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  
  for x in range(4,8):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature8
  black=0
  
  for x in range(4,8):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature9
  black=0
  
  for x in range(8,12):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature10
  black=0
  
  for x in range(8,12):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature11
  black=0
  
  for x in range(8,12):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature12
  black=0
  
  for x in range(8,12):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature13
  black=0
  
  for x in range(12,16):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  
  for x in range(12,16):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  
  for x in range(12,16):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  
  for x in range(12,16):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  for x in range(16,20):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  
  for x in range(16,20):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  
  for x in range(16,20):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  
  for x in range(16,20):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  for x in range(20,24):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  
  for x in range(20,24):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  
  for x in range(20,24):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  
  for x in range(20,24):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  for x in range(24,28):
    for y in range(0,7):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  
  for x in range(24,28):
    for y in range(7,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  
  for x in range(24,28):
    for y in range(14,21):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  
  for x in range(24,28):
    for y in range(21,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  return features

def basicFeatureExtractorDigit_3(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is white (0) or gray/black (1)
  """
  a = datum.getPixels()

  features = []
  #feature1
  black=0
  for x in range(0,4):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(0,4):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(0,4):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(0,4):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(0,4):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(0,4):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0 
  for x in range(0,4):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(4,8):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0 
  for x in range(4,8):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0 
  for x in range(4,8):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(4,8):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(4,8):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(4,8):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(4,8):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(8,12):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(8,12):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(8,12):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(8,12):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(8,12):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(8,12):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0 
  for x in range(8,12):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(12,16):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0 
  for x in range(12,16):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0 
  for x in range(12,16):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(12,16):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(12,16):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(12,16):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(12,16):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  for x in range(16,20):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0 
  for x in range(16,20):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0 
  for x in range(16,20):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(16,20):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(16,20):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(16,20):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(16,20):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(20,24):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(20,24):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(20,24):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(20,24):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(20,24):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(20,24):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0 
  for x in range(20,24):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(24,28):
    for y in range(0,4):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0 
  for x in range(24,28):
    for y in range(4,8):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0 
  for x in range(24,28):
    for y in range(8,12):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(24,28):
    for y in range(12,16):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(24,28):
    for y in range(16,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(24,28):
    for y in range(20,24):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(24,28):
    for y in range(24,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  return features


def basicFeatureExtractorFace(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is an edge (1) or no edge (0)
  """
  features=[]
  #feature1
  black=0
  for x in range(0,15):
    for y in range(0,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(0,15):
    for y in range(14,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(0,15):
    for y in range(28,42):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(0,15):
    for y in range(42,56):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(0,15):
    for y in range(56,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(15,30):
    for y in range(0,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(15,30):
    for y in range(14,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature8
  black=0
  for x in range(15,30):
    for y in range(28,42):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature9
  black=0
  for x in range(15,30):
    for y in range(42,56):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature10
  black=0
  for x in range(15,30):
    for y in range(56,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature11
  black=0
  for x in range(30,45):
    for y in range(0,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature12
  black=0
  for x in range(30,45):
    for y in range(14,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature13
  black=0
  for x in range(30,45):
    for y in range(28,42):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature14
  black=0
  for x in range(30,45):
    for y in range(42,56):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature15
  black=0
  for x in range(30,45):
    for y in range(56,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature16
  black=0
  for x in range(45,60):
    for y in range(0,14):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature17
  black=0
  for x in range(45,60):
    for y in range(14,28):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature18
  black=0
  for x in range(45,60):
    for y in range(28,42):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature19
  black=0
  for x in range(45,60):
    for y in range(42,56):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature20
  black=0
  for x in range(45,60):
    for y in range(56,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)  
  return features

def basicFeatureExtractorFace_2(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is an edge (1) or no edge (0)
  """
  features=[]
  #feature1
  black=0
  for x in range(0,10):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(0,10):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(0,10):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(0,10):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(0,10):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(0,10):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(0,10):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(10,20):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(10,20):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(10,20):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(10,20):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(10,20):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(10,20):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(10,20):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(20,30):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(20,30):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(20,30):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(20,30):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(20,30):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(20,30):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(20,30):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(30,40):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(30,40):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(30,40):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(30,40):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(30,40):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(30,40):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(30,40):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(40,50):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(40,50):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(40,50):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(40,50):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(40,50):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(40,50):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(40,50):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature1
  black=0
  for x in range(50,60):
    for y in range(0,10):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature2
  black=0
  for x in range(50,60):
    for y in range(10,20):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature3
  black=0
  for x in range(50,60):
    for y in range(20,30):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature4
  black=0
  for x in range(50,60):
    for y in range(30,40):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature5
  black=0
  for x in range(50,60):
    for y in range(40,50):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature6
  black=0
  for x in range(50,60):
    for y in range(50,60):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black)
  #feature7
  black=0
  for x in range(50,60):
    for y in range(60,70):
      if datum.getPixel(x, y) > 0:
        black=black+1
  features.append(black) 
  return features

def extractImages(options_data,trainsize,testsize): #options_data is either "faces" or "digit"
    options_training = trainsize
    options_test = testsize
    numTraining = options_training
    numTest = options_test

    if(options_data=="faces"):
        rawTrainingData = util.loadDataFile("facedata/facedatatrain", numTraining,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        trainingLabels = util.loadLabelsFile("facedata/facedatatrainlabels", numTraining)
        rawValidationData = util.loadDataFile("facedata/facedatatrain", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        validationLabels = util.loadLabelsFile("facedata/facedatatrainlabels", numTest)
        rawTestData = util.loadDataFile("facedata/facedatatest", numTest,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
        testLabels = util.loadLabelsFile("facedata/facedatatestlabels", numTest)
    else:
        rawTrainingData = util.loadDataFile("digitdata/trainingimages", numTraining,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
        trainingLabels = util.loadLabelsFile("digitdata/traininglabels", numTraining)
        rawValidationData = util.loadDataFile("digitdata/validationimages", numTest,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
        validationLabels = util.loadLabelsFile("digitdata/validationlabels", numTest)
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
    featureFunction = basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    givenTrue, pyTrue, givenFalse, pyFalse=NaiveBayes.trainFace(trainFeatures,trainingLabels)
    predict=NaiveBayes.predictFace(testFeatures, testLabels, givenTrue, pyTrue, givenFalse, pyFalse)
    print(percentCorrect(testLabels,predict))

def runPerceptronFace(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    weights=Perceptron.makeTrainFunctionFace(trainFeatures,trainingLabels)
    predict=Perceptron.predictFace(testFeatures, testLabels,weights)
    print(percentCorrect(testLabels,predict))

def runPerceptronDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9=Perceptron.makeTrainFunctionDigits(trainFeatures,trainingLabels)
    predict=Perceptron.predictDigit(testFeatures, testLabels,weights0,weights1,weights2,weights3,weights4,weights5,weights6,weights7,weights8,weights9)
    print(percentCorrect(testLabels,predict))

def runNBDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True=NaiveBayes.trainDigit(trainFeatures,trainingLabels)
    predict=NaiveBayes.predictDigit(testFeatures,testLabels,given0True, given1True,given2True,given3True,given4True,given5True,given6True,given7True,given8True, given9True,py0True,py1True,py2True,py3True,py4True,py5True,py6True,py7True,py8True,py9True)
    print(percentCorrect(testLabels,predict))

def runkNNFace(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("faces",trainsize,testsize)
    featureFunction = basicFeatureExtractorFace_2
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,1)
    print(percentCorrect(testLabels,predict))

def runkNNDigit(trainsize,testsize):
    trainingData,trainingLabels,testData,testLabels=extractImages("digit",trainsize,testsize)
    featureFunction = basicFeatureExtractorDigit_3
    trainFeatures = list(map(featureFunction, trainingData))
    testFeatures = list(map(featureFunction,testData))
    predict=kNN.predict(trainFeatures,trainingLabels,testFeatures,testLabels,1)
    print(percentCorrect(testLabels,predict))


def main():
    runPerceptronFace(450,100)


if __name__ == '__main__':
    main()