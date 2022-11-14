#Program Name: Naive Bayes Classifier
#Author: Victor Paul LaBrie
#Date: November 13th, 2022
#Problem: Implement a program that will learn 
# a Naive Bayes classifier from training data and 
# then use that to assign sentiment to the 
# reviews in a set of test data

import sys
import re

#First, we need to take in command line arguments.
n = sys.argv[1]
trainingFileArg = sys.argv[2]
testFileArg = sys.argv[3]

#Then, we need to open the training file. The test file
# will not be opened until later after the training model has been
# learned. 
trainingFile = open(trainingFileArg)

#After this we start our main function
def main(n):
    return 0
