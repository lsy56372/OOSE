
# modules needed
import numpy as np
import argparse


################################

def readCommands():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("An illustration of a command line parser"))
  p.add_argument("--numb", dest ="numb", type=int, default=20, help=("Lenght of array to generate\nDefault = 20"))#change it to 20
  cmdargs = p.parse_args()
  return cmdargs


################################

def makeRand(n):
  '''Make an array of random numbers'''
  x=np.random.uniform(1,10,n) #Modify a random number between 1 and 10
  return(x)


################################
# main

if __name__=="__main__":
  com=readCommands()
  y=makeRand(com.numb)
  print(y)

