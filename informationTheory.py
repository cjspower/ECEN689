import numpy as np

def calcShannonEnt(data):
    #calculate the information entropy of a dataset
    #dataSet in np.array format
    #label is the last element in a dataSet
    dataLen = len(data)
    labelCounts = {}
    for line in data:
        if not labelCounts.has_key(line[-1]):
            labelCounts[line[-1]] = 0
        labelCounts[line[-1]] += 1
    shannonEnt = 0.0
    if len(labelCounts) == 1:
        flag = 1
    else:
        flag = 0
    for key in labelCounts:
        prob = float(labelCounts[key])/dataLen
        shannonEnt -= prob * np.log2(prob)
    return shannonEnt,flag
    
def main():
    data = [[1,1,1],[1,1,1],[1,0,0],[0,1,0],[0,1,0]]
    print calcShannonEnt(data)
    
if __name__ == '__main__':
    main()