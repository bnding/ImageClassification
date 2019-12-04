# util.py
# -------
#
import sys
import random
import os
import zipfile

## Constants

DATUM_WIDTH = 0 # in pixels
DATUM_HEIGHT = 0 # in pixels

## Module Classes

class Datum:
  """
  A datum is a pixel-level encoding of digits or face/non-face edge maps.

  Digits are from the MNIST dataset and face images are from the 
  easy-faces and background categories of the Caltech 101 dataset.
    
  Each digit is 28x28 pixels, and each face/non-face image is 60x74 
  pixels, each pixel can take the following values:
    0: no edge (blank)
    1: gray pixel (+) [used for digits only]
    2: edge [for face] or black pixel [for digit] (#)
    
  Pixel data is stored in the 2-dimensional array pixels, which
  maps to pixels on a plane according to standard euclidean axes
  with the first dimension denoting the horizontal and the second
  the vertical coordinate:
    
    28 # # # #      #  #
    27 # # # #      #  #
     .
     .
     .
     3 # # + #      #  #
     2 # # # #      #  #
     1 # # # #      #  #
     0 # # # #      #  #
       0 1 2 3 ... 27 28
   
  For example, the + in the above diagram is stored in pixels[2][3], or
  more generally pixels[column][row].
       
  The contents of the representation can be accessed directly
  via the getPixel and getPixels methods.
  """
  def __init__(self, data, width, height):
    """
    Create a new datum from file input (standard MNIST encoding).
    """
    DATUM_HEIGHT = height
    DATUM_WIDTH = width
    self.height = DATUM_HEIGHT
    self.width = DATUM_WIDTH
    if data == None:
      data = [[' ' for i in range(DATUM_WIDTH)] for j in range(DATUM_HEIGHT)] 
    # tbox = Print_image_toolbox() 
    # print()
    # tbox.print_list_image(data) 
    # tmp = convertToInteger(data)
    # print()
    # tbox.print_list_image(tmp)
    # tmp2 = arrayInvert(tmp)
    # print()
    # tbox.print_list_image(tmp2)
    # tmp3 = arrayInvert(convertToInteger(data))
    # print()
    # tbox.print_list_image(tmp3)
    self.pixels = arrayInvert(convertToInteger(data)) 
    # print()
    # tbox.print_list_image(self.pixels)
    # print()
    
  def getPixel(self, column, row):
    """
    Returns the value of the pixel at column, row as 0, or 1.
    """
    return self.pixels[column][row]
      
  def getPixels(self):
    """
    Returns all pixels as a list of lists.
    """
    return self.pixels    
      
  def getAsciiString(self):
    """
    Renders the data item as an ascii image.
    """
    rows = []
    data = arrayInvert(self.pixels)
    for row in data:
      ascii = map(asciiGrayscaleConversionFunction, row)
      rows.append( "".join(ascii) )
    return "\n".join(rows)
    
  def __str__(self):
    return self.getAsciiString()

class Print_image_toolbox():
  def print_list_image(self,list_image):
    for i in range(len(list_image)):
      for j in range(len(list_image[i])):
        print(list_image[i][j], end=' ')
      print()


# Data processing, cleanup and display functions

def loadDataFile(filename, n, width, height):
  """
  Reads n data images from a file and returns a list of 'list of lists' objects.
  (Return less then n items if the end of file is encountered).
  """
  DATUM_WIDTH=width
  DATUM_HEIGHT=height
  fin = readlines(filename)
  fin.reverse()
  items = []
  for i in range(n):
    data = []
    for j in range(height):
      data.append(list(fin.pop()))
    if len(data[0]) < DATUM_WIDTH-1:
      # we encountered end of file...
      print ("Truncating at %d examples (maximum)" % i)
      break
    # tbox = Print_image_toolbox() 
    # tbox.print_list_image(data)
    items.append(Datum(data,DATUM_WIDTH,DATUM_HEIGHT))
  return items

def readlines(filename):
  "Opens a file or reads it from the zip archive data.zip"
  if(os.path.exists(filename)): 
    return [l[:-1] for l in open(filename).readlines()]
  else: 
    z = zipfile.ZipFile('data.zip')
    return z.read(filename).split('\n')

def loadLabelsFile(filename, n):
  """
  Reads n labels from a file and returns a list of integers.
  """
  fin = readlines(filename)
  labels = []
  for line in fin[:min(n, len(fin))]:
    if line == '':
        break
    labels.append(int(line))
  return labels

def asciiGrayscaleConversionFunction(value):
  """
  Helper function for display purposes.
  """
  if(value == 0):
    return ' '
  elif(value == 1):
    return '+'
  elif(value == 2):
    return '#'    
    
def IntegerConversionFunction(character):
  """
  Helper function for file reading.
  """
  if(character == ' '):
    return 0
  elif(character == '+'):
    return 1
  elif(character == '#'):
    return 2    

def convertToInteger(data):
  """
  Helper function for file reading.
  """
  if type(data) != type([]):
    return IntegerConversionFunction(data)
  else:
#    return map(convertToInteger, data)
    return list(map(convertToInteger, data))

def sign( x ):
  """
  Returns 1 or -1 depending on the sign of x
  """
  if( x >= 0 ):
    return 1
  else:
    return -1

def arrayInvert(array):
  """
  Inverts a matrix stored as a list of lists.
  input:  array[row (y)][column (x)]  
  output: result[column (x)][row (y)]
          result = inverted_array[column (x)][row (y)]
  purpose: To maintain an image pixels in a 2D coordinate
           1) that is easy to picture in mind when programming 
           2) with origin at bottom left
           3) with y (row) from 0 growing upward
           4) with x (column) from 0 growing right
           5) with each pixel referenced by result[x (column)][y (row)]
  """
  result = [[] for i in array[0]]
  for outer in array:
    for inner in range(len(outer)):
      result[inner].append(outer[inner])
  return result


# Testing

def _test():
  import doctest
  doctest.testmod() # Test the interactive sessions in function comments
  n = 1
#  items = loadDataFile("facedata/facedatatrain", n,60,70)
#  labels = loadLabelsFile("facedata/facedatatrainlabels", n)
  items = loadDataFile("digitdata/trainingimages", n, 28, 28)

  tbox = Print_image_toolbox() 
  print ()
  print('*** print items[0].pixels')
  tbox.print_list_image(items[0].pixels)
  print()

  labels = loadLabelsFile("digitdata/traininglabels", n)
  for i in range(1):
    print (items[i])
    print (items[i].height)
    print (items[i].width)
    print (dir(items[i]))
    print (items[i].getPixels())
    print (items[i].getPixel(16,5))
    print (labels[i])

if __name__ == "__main__":
  _test()  