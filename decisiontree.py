import numpy as np
import informationTheory as ith
import numpy as np
import informationTheory as ith

def splitDataSet(dataSet, axis):
    dataLen = len(dataSet)
    dim = len(dataSet[0])
    newDataSet = []
    output = {}
    for dataLine in dataSet:
        key = dataLine[axis]
        if not output.has_key(key):
            output[key] = []
        output[key].append(dataLine[:axis]+dataLine[axis+1:])  
      
    return output

def bestSplit(dataSet):
    dataLen = len(dataSet)
    dim = len(dataSet[0])
    entropy,flag = ith.calcShannonEnt(dataSet)
    if(flag == 1):
         return 0
    bestEntropyDiff = -1
    for axis in xrange(dim-1):
        splitTable = splitDataSet(dataSet,axis)
        newEntropy = 0.0
        for key in splitTable:
            prob = len(splitTable[key])/float(dataLen)
            newEntropy += prob * ith.calcShannonEnt(splitTable[key])[0]
        diff = entropy - newEntropy
        if (diff > bestEntropyDiff):
            bestEntropyDiff = diff
            bestAxis = axis
            split = splitTable
    return splitTable, bestAxis

def maxCount(dataSet):
    classCount = {}
    for line in dataSet:
        if not classCount.has_key(line[-1]):
            classCount[line[-1]] = 0
        classCount[line[-1]] += 1
    maxCount = 0
    for key in classCount:
        if classCount[key] > maxCount:
            maxCount = classCount[key]
            maxKey = key
    return maxKey

def createTree(dataSet):
    dataLen = len(dataSet)
    dim = len(dataSet[0])
    if len(dataSet[0]) == 1:
        return maxCount(dataSet)
    split = bestSplit(dataSet)
    if split == 0:
        return dataSet[0][-1]
    axis = split[1]
    tree = {axis:{}}
    for key in split[0]:
        tree[axis][key] = createTree(split[0][key])
    return tree
      
def labelCreateTree(dataSet,labels):
    dataLen = len(dataSet)
    dim = len(dataSet[0])
    if len(dataSet[0]) == 1:
        return maxCount(dataSet)
    split = bestSplit(dataSet)
    if split == 0:
        return dataSet[0][-1]
    axis = split[1]
    label = labels[axis]
    tree = {label:{}}
    for key in split[0]:
        tree[label][key] = labelCreateTree(split[0][key],labels[:axis]+labels[axis+1:])
    return tree
    
def classify(tree,dataLine):
    if not isinstance(tree, dict):
        return tree
    #print tree
    axis = tree.keys()[0]
    nextLevel = tree[axis]
    key = dataLine[axis]
    del dataLine[axis]
    print nextLevel
    return classify(nextLevel[key],dataLine)         
    
        
def main():
    data = np.array([1,2,3,4,5])
    print data[0]

if __name__ == '__main__':
    main()
    