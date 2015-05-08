from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

def main():
    f = open('modifiedInput.txt')
    X = []
    Y = []
    f.readline()
    for line in f:
        line = line.rstrip('\n')
        data = line.split(',')
        datalen = len(data)
        X.append(map(int,data[0:datalen-1]))
        Y.append(int(data[-1]))
        score = []
    for i in xrange(10):
        X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,Y,test_size=0.2,random_state=i)
        clf = RandomForestClassifier()
        #clf = GaussianNB()
        clf.fit(X_train, y_train)
        score.append(clf.score(X_test, y_test))

    print np.average(score)
    
if __name__ == '__main__':
    main()