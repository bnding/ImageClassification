import util
import random

DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

def rawFeatureExtractorDigit(datum):
    """
    Returns a set of pixel features indicating whether
    each pixel in the provided datum is white (0) or gray/black (1)
    """
    features = []

    for x in range(DIGIT_DATUM_WIDTH):
        for y in range(DIGIT_DATUM_HEIGHT):
            if datum.getPixel(x, y) > 0:
                cell_value = 1
            else:
                cell_value = 0
            features.append(cell_value)

    return features

def rawFeatureExtractorFace(datum):
    """
    Returns a set of pixel features indicating whether
    each pixel in the provided datum is an edge (1) or no edge (0)
    """
    features = []

    for x in range(FACE_DATUM_WIDTH):
        for y in range(FACE_DATUM_HEIGHT):
            if datum.getPixel(x, y) > 0:
                cell_value = 1
            else:
                cell_value = 0
            features.append(cell_value)

    return features

def basicFeatureExtractorDigit(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is white (0) or gray/black (1)
  """
  # a = datum.getPixels()

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
  # a = datum.getPixels()

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
  # a = datum.getPixels()

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

