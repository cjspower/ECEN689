from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
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
    for XXX in XX:
        X.append(XXX[:datalen-1])
        Y.append(XXX[-1])
    #clf = neighbors.KNeighborsClassifier(n_neighbors = 2,weights = 'distance')
    #clf.fit(X,Y)
    clf = tree.DecisionTreeClassifier()
    #gnb = GaussianNB()
    #gnb.fit(X,Y)
    clf = clf.fit(X, Y)
        # clf2 = tree.DecisionTreeClassifier()
        # clf2 = clf2.fit(X, Y)
    print 'model created'
    
    fin = open('modifiedTest.txt', 'rb')
    fout = open('submit.csv', 'wb')
    writer = csv.writer(fout)
    writer.writerow(['id','hand'])
    counter = 0
    for line in fin:
        counter += 1
        if counter%10000 == 0:
            print counter
        line = line.rstrip('\n')
        data = line.split(',')
        data = map(int,data)
        y = clf.predict(data)
        writer.writerow([counter, y[0]])

if __name__ == '__main__':
    main()     
        
    