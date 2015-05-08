def main():
    f = open('modifiedInput.txt','w')
    with open('train.csv', 'rb') as fin:
        line = fin.readline()
        for line in fin:
            dataline = map(int,line.rstrip('\n').split(','))
            cards = []
            for i in xrange(5):
                cards.append(dataline[2*i:2*i+2])
            hand = dataline[-1]
            scount = [0,0,0,0]    
            for card in cards:
                scount[card[0]-1]+=1
            cards.sort(key=lambda tup:tup[1])
            scount.sort()
            for count in scount:
                f.write(str(count)+",")
            for x in xrange(4):
                f.write(str(cards[x+1][1]-cards[x][1])+",")
            f.write(str(cards[0][1]-cards[4][1])+",")
            f.write(str(hand)+"\n")
        f.close()
        # f2 = open('modifiedInput2.txt','w')
#         for line in fin:
#             dataline = map(int,line.rstrip('\n').split(','))
#             cards = []
#             for i in xrange(5):
#                 cards.append(dataline[2*i:2*i+2])
#             hand = dataline[-1]
#             scount = [0,0,0,0]
#             for card in cards:
#                 scount[card[0]-1]+=1
#             cards.sort(key=lambda tup:tup[1])
#             for count in scount:
#                 f2.write(str(count)+",")
#             for x in xrange(4):
#                 f2.write(str(cards[x+1][1]-cards[x][1])+",")
#             f2.write(str(cards[0][1]-cards[4][1])+",")
#             f2.write(str(hand)+"\n")
    fin.close()
#   f2.close()
    f = open('modifiedTest.txt','w')
    fin = open('test.csv')
    line = fin.readline()
    for line in fin:
        dataline = map(int,line.rstrip('\n').split(','))[1:]
        cards = []
        for i in xrange(5):
            cards.append(dataline[2*i:2*i+2])
        scount = [0,0,0,0]
        for card in cards:
            scount[card[0]-1]+=1
        cards.sort(key=lambda tup:tup[1])
        scount.sort()
        for count in scount:
            f.write(str(count)+",")
        for x in xrange(4):
            f.write(str(cards[x+1][1]-cards[x][1])+",")
        f.write(str(cards[0][1]-cards[4][1])+"\n")
    f.close()
    fin.close()
    return 0
    
    
    
if __name__ == '__main__':
    main()