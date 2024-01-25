# modules needed
import numpy as np


################################
# define 4 function:mean,max,min and difference 

def getMean(x):
  mean=np.mean(x)
  return(mean)

def getMax(y):
  max=np.max(y)
  return(max)

def getMin(z):
  min=np.min(z)
  return(min)
def difference(x,y):
  dif=x-y
  return(dif)
# the main block

if __name__ == '__main__':
  # create some data
  data=np.random.rand(100)
  # call our function
  meanX=getMean(data)
  maxY=getMax(data)
  minZ=getMin(data)
  diff = difference(maxY, minZ) 

  print("Mean is",meanX)
  print("Max is",maxY)
  print("Min is",minZ)
  print("The difference between the maximum value and the minimum value is" ,diff)


# the end
################################

