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
accuracy = (truePositives+trueNegatives)/(trueNegatives+truePositives+falseNegatives+falsePositives)
precision = truePositives/(truePositives+falsePositives)
recall = truePositives/(truePositives+falseNegatives)
print("Accuracy: "+str(accuracy), "Precision: " + str(precision), "Recall: " + str(recall))