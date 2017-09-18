import argparse
import numpy as np
import matplotlib.pyplot as plt

def actionReadData(filename) :
    x = np.array([])
    y = np.array([])
    with open(filename, 'r') as data:
        for line in data :
            xy = line.split()
            x = np.append(x, float(xy[0]))
            y = np.append(y, float(xy[1]))
    return x, y

def actionLeastSquares(x, y) :
    N = np.size(x)
    Ex = ( 1.0 / N ) * np.sum(x)
    Ey = ( 1.0 / N ) * np.sum(y)
    Exx = ( 1.0 / N ) * np.sum(x ** 2)
    Exy = ( 1.0 / N ) * np.dot(x, y)
    m = (Exy - Ex * Ey) / (Exx - Ex ** 2)
    c = (Exx * Ey - Ex * Exy) / (Exx - Ex ** 2)
    fity = np.array([m*fitx + c for fitx in x])
    return fity

def actionPlot(x, y, fity) :
    plt.plot(x, y, 'yo')
    plt.plot(x, fity, '-o')
    plt.show()

parser = argparse.ArgumentParser(description='Least-Squares fitting.')
parser.add_argument('filename', nargs=1, metavar=('filename'), help='load data from file, see millikan.txt as an example')
parser.add_argument('--save', nargs=1, metavar=('filename'), help='save numerical results to a output file in same format as input file')
args = parser.parse_args()

x, y = actionReadData(args.filename[0])
fity = actionLeastSquares(x, y)
actionPlot(x, y, fity)

if args.save is not None :
    f = open(args.save[0], 'wb')
    for cx, cy in zip(x, fity) :
        f.write('%s %s\n' % (str(cx), str(cy)))
    f.close()
