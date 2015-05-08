from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
import numpy as np
import csv
def main():
    XX = []
    Y = []
    X = []
    with open('modifiedInput.txt', 'rb') as f:
        for line in f:
            line = line.rstrip('\n')
            data = line.split(',')
            datalen = len(data)
            XX.append(map(int,data))
    f.close
    print 'readfile done'
    np.random.shuffle(X)
    for i in xrange(17500):
        X.append(XX[i][:datalen-1])
        Y.append(XX[i][-1])
    #clf = neighbors.KNeighborsClassifier(n_neighbors = 2,weights = 'distance')
    #clf.fit(X,Y)
    clf = RandomForestClassifier()
    #gnb = GaussianNB()
    #gnb.fit(X,Y)
    clf = clf.fit(X, Y)
        # clf2 = tree.DecisionTreeClassifier()
        # clf2 = clf2.fit(X, Y)
    print 'model created'
    
    fin = open('modifiedTest.txt', 'rb')
    fout = open('submit.csv', 'wb')
    
    
    # right = 0
#     wrong = 0
#     count = 0
#     for i in xrange(17500,len(XX)):
#         if XX[i][-1] == clf.predict(XX[i][:datalen-1])[0]:
#             right += 1
#         else:
#             wrong += 1
#     print right,wrong


if __name__ == '__main__':
    main()