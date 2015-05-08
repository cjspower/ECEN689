import numpy as np
import matplotlib.pyplot as plt

def main():
    cards = []
    hands = [[],[],[],[],[],[],[],[],[],[]]
    with open('train.csv', 'rb') as f:
        f.readline()
        for line in f:
            line = line.rstrip('\n')
            data = line.split(',')
            datalen = len(data)
            l = map(int,data)
            card = []
            card.append([l[0],l[1]])
            card.append([l[2],l[3]])
            card.append([l[4],l[5]])
            card.append([l[6],l[7]])
            card.append([l[8],l[9]])
            card.sort(key=lambda tup:tup[1])
            card.append(l[10])
            cards.append(card)     
            hands[l[10]].append(card)
    f.close
    average = [[],[],[],[],[],[],[],[],[],[]]
    maxSuit = [[],[],[],[],[],[],[],[],[],[]]
    i = 0
    for handss in hands:
        for hand in handss:
            suits = [0,0,0,0]
            average[i].append(float(hand[4][1]-hand[0][1])/4)
            for q in xrange(5):
                suits[hand[q][0]-1] += 1
            suits.sort()
            maxSuit[i].append(suits[3])
        i += 1
    plt.title('Histogram of average difference')
    for x in xrange(10):
        plt.subplot(3,4,x+1)
        plt.hist(maxSuit[x],bins = 10)
    plt.show()
        
    
if __name__ == '__main__':
    main()