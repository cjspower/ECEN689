import matplotlib.pyplot as plt
def main():
    X = ['kNN','NB','DecisionTree','RF']
    X = [1,2,3,4]
    Y = [0.565,0.485,0.485,0.555]
    plt.title('compare of different algorithms')
    plt.xlabel('algorithm')
    plt.ylabel('score')
    plt.ylim(0,1)
    plt.plot(X,Y)
    plt.show()
    
    
    
    return 0
if __name__ == '__main__':
    main()