import numpy as np
import matplotlib.pyplot as plt
def main():
    classification = [[],[],[],[],[],[],[],[],[],[]]
    f = open('modifiedInput.txt')
    for line in f:
        line = line.rstrip('\n')
        data = line.split(',')
        data = map(int,data)
        classification[data[-1]].append(data)
    for i in xrange(8):
        feature = [[],[],[],[],[],[],[],[],[],[]]
        for classnum in xrange(10):
            for dataline in classification[classnum]:
                feature[classnum].append(dataline[i])
    
        for classnum in xrange(10):
            plt.figure(i)
            plt.subplot(4,3,classnum+1)
            plt.xlim(-1,13)
            plt.hist(feature[classnum])
    
    plt.show()
            
        
        
        
    
    f.close()
    
if __name__ == '__main__':
    main()