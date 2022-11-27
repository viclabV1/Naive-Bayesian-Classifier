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
n = int(sys.argv[1])
trainingFileArg = sys.argv[2]
testFileArg = sys.argv[3]

#Then, we need to open the training file. The test file
# will not be opened until later after the training model has been
# learned. 
trainingFile = open(trainingFileArg)

#After this we start our training function
def training():
    #Vocab
    positiveDict = {}
    negativeDict = {}
    #Number of each doc type
    positiveReviews = 0
    negativeReviews = 0
    #number of words of each topic
    positiveWordCount = 0
    negativeWordCount = 0
    #For every review, get word frequencies, and if negative add to negative model, do the same for positive
    for review in trainingFile.readlines():
        reviewWords = words(review)
        if review.split()[1]=='1':
            for wordTuple in reviewWords:
                if wordTuple[0] in positiveDict:
                    positiveDict[wordTuple[0]] += wordTuple[1]
                else:
                    positiveDict[wordTuple[0]] = wordTuple[1]
            positiveReviews += 1
            positiveWordCount += wordTuple[1]
        else:
            for wordTuple in reviewWords:
                if wordTuple[0] in negativeDict:
                    negativeDict[wordTuple[0]] += wordTuple[1]
                else:
                    negativeDict[wordTuple[0]] = wordTuple[1]
            negativeReviews += 1
            negativeWordCount += wordTuple[1]
    print(positiveWordCount, negativeWordCount)
    #if occurences less than N, remove. do this for both positive and negative models
    removeKeys = []
    for word in positiveDict.keys():
        if positiveDict[word]<n:
            removeKeys.append(word)
    for key in removeKeys:
        positiveDict.pop(key)
    removeKeys = []
    for word in negativeDict.keys():
        if negativeDict[word]<n:
            removeKeys.append(word)
    for key in removeKeys:
        negativeDict.pop(key)
    return positiveDict, negativeDict, positiveWordCount, negativeWordCount, positiveReviews, negativeReviews



#Function for getting word frequency
def words(text) -> list:
    wordDict = {}
    #Look at each word
    splitText = text.split();
    #create list of all words
    for word in splitText:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

            
    #next, we sort the dictionary
    sortedWordList = sorted(wordDict, key = wordDict.get, reverse=True)
    sortedWordDict = {}
    for y in sortedWordList:
        sortedWordDict[y]=wordDict[y]
    sortedItems = list(sortedWordDict.items())
    
    return sortedItems[::-1]

#call training function
posModel, negModel, posWordCount, negWordCount, posReviewCount, negReviewCount = training()
#test file not opened until after training complete
testFile = open(testFileArg)

