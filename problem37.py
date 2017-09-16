import argparse
import numpy as np
import sysconfig
import sys
import matplotlib.pyplot as plt
import pickle

def actionGenerate(N, maxiter) :
    step = 4.0 / N
    rx = []
    ry = []
    for i in np.arange(-2.0, 2.0, step) :
        for j in np.arange(-2.0, 2.0, step) :
            c = complex(i, j)
            z = complex(0.0, 0.0) + c
            k = 0
            while k < maxiter and np.absolute(z) < 2.0 :
                z = z**2 + c
                k += 1
            if k == maxiter :
                rx.append(z.real)
                ry.append(z.imag)
    return rx, ry

def actionPlot(b, rx, ry) :
    heatmap, xedges, yedges = np.histogram2d(rx, ry, bins=b)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.show()

parser = argparse.ArgumentParser(description='Mandelbrot set generator and plotter.')
parser.add_argument('--generate', nargs=2, metavar=('N', 'maxiter'), type=int, help='generate Mandelbrot set from NxN grid and at most maxiter iterations per point')
parser.add_argument('--save', nargs=1, metavar=('filename'), help='save generated set to a file')
parser.add_argument('--load', nargs=1, metavar=('filename'), help='load generated set from a file')
parser.add_argument('--plot', nargs=1, metavar=('b'), type=int, help='generate plot of Mandelbrot set with b bins')
args = parser.parse_args()

rx = []
ry = []
if args.generate is not None :
    rx, ry = actionGenerate(args.generate[0], args.generate[1])

if args.save is not None :
    pickle.dump((rx, ry), open(args.save[0], 'wb'))

if args.load is not None :
    (rx, ry) = pickle.load(open(args.load[0], 'rb'))

if args.plot is not None :
    actionPlot(args.plot[0], rx, ry)
