#Program Name: Naive Bayes Eval
#Author: Victor Paul LaBrie
#Date: November 13th, 2022
#Problem: Implement a program that will evaluate 
#the recall, accuracy, and precision of a 
#Naive-Bayes Model
import sys

testFileArg= sys.argv[1]
goldFileArg = sys.argv[2]
testFile = open(testFileArg)
goldFile = open(goldFileArg)

truePositives = 0
trueNegatives = 0
falsePositives = 0
falseNegatives = 0

systemReview = testFile.readlines()
goldReview = goldFile.readlines()
#calculate tp, np, tf, nf
for i in range(0, len(systemReview)):
    thisSysReview = systemReview[i].split()
    thisGoldReview = goldReview[i].split()
    #print(thisSysReview, thisGoldReview)
    if thisSysReview[1]== '1' and thisGoldReview[1] == '1':
        truePositives += 1
    elif thisSysReview[1]=='1' and thisGoldReview[1] == '0':
        falsePositives += 1
    elif thisSysReview[1]=='0' and thisGoldReview[1] == '0':
        trueNegatives +=1
    else:
        falseNegatives += 1
#accuracy
accuracy = (truePositives+trueNegatives)/(trueNegatives+truePositives+falseNegatives+falsePositives)
#precision
precision = (truePositives)/(truePositives+falsePositives)
#recall
recall = (truePositives)/(truePositives+falseNegatives)
print("Accuracy: "+str(accuracy), "Precision: " + str(precision), "Recall: " + str(recall))
