'''
Working with basics of visual plotting with matplotlib
'''
import matplotlib.pyplot as plt
import numpy as np

data = np.arange(10)

def plotData(data=data):
    #fig = plt.plot(data) # (1) both ways work
    plt.plot(data) # (2) both ways work
    plt.show()

def subplots1():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    plt.show()

    # issuing a plotting with matplotlib draws on the last figure and subplot used (creating one if none exists)
    # in this case, ax3
    plt.plot([1.5,3.5,-2,1.6])
    plt.show()

    # k-- is a style option to plot a black dashed line
    plt.plot(np.random.randn(50).cumsum(), 'k--')
    plt.show()

def subplots2():
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)

    # defaults to last plot added, ax3
    plt.plot(np.random.randn(50).cumsum(), 'k--')

    # specifies ax1
    _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
    
    #specifies ax2
    ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
    plt.show()

if __name__ == "__main__":
    #plotData()
    #subplots1()
    subplots2()