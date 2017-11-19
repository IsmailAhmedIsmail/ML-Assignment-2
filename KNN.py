import numpy as np
import math

def euclideanDist(testCase, x):
    sum = 0
    for i in range(len(x)):
        d = testCase[i] - x[i]
        sum += d * d
    return math.sqrt(sum)

def errors(testCase):
    errorsList = []
    for i, x in enumerate(trainX):
        e = euclideanDist(testCase, x)
        errorsList.append((i,e))
    return errorsList

def vote(KNN):
    classeshash = {}
    for i in classes:
        classeshash[i] = 0
    for n in KNN:
        classeshash[trainY[n[0]]] += 1
    count = 0
    decision = ""
    for c in classeshash:
        if classeshash[c] > count:
            decision = c
            count = classeshash[c]
    # tie = [c for c in classeshash if classeshash[c] == count]
    # if(len(tie)>1):
    #     print("Tie happened")
    #     print(classeshash)
    #     print(decision)
    return decision

def output(k):
    print("K value: ", k)
    count = 0.0
    for i in range(len(predicted)):
        print("Predicted class: ", predicted[i], "\tActual class: ", testY[i])
        if(predicted[i] == testY[i]):
            count += 1
    print("Number of correctly classified instances: ", count, "Total number of instances: ", len(predicted))
    print("Accuracy: ", count/len(predicted))

train = np.genfromtxt('TrainData.txt',
                     delimiter=',',
                     dtype=['<f8','<f8','<f8','<f8','<f8','<f8','<f8','<f8','U15'])

trainX = [[float(i[n]) for n in range(7)] for i in train]
trainY = [i[8] for i in train]

test = np.genfromtxt('TestData.txt',
                     delimiter=',',
                     dtype=['<f8','<f8','<f8','<f8','<f8','<f8','<f8','<f8','U15'])

testX = [[float(i[n]) for n in range(7)] for i in test]
testY = [i[8] for i in test]

classes = []
for i in train:
    if i[8] not in classes:
        classes.append(i[8])

for k in range(1,9):
    predicted = []
    for testCase in testX:
        errorsList = errors(testCase)
        sortedErrors = sorted(errorsList, key=lambda x: float(x[1]))
        KNN = sortedErrors[0:k]
        predicted.append(vote(KNN))
    output(k)