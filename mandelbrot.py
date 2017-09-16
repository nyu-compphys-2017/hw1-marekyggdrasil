import argparse
import numpy as np
import sysconfig
import sys
import matplotlib.pyplot as plt
import pickle
import multiprocessing
from multiprocessing import Pool

def actionProcessChunk(step, maxiter, xmin, xmax) :
    rx = []
    ry = []
    for i in np.arange(xmin, xmax, step) :
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

def actionGenerate(N, maxiter, chunks) :
    step = 4.0 / N
    rx = []
    ry = []
    if chunks == 1 :
        rx, ry = actionProcessChunk(step, maxiter, -2.0, 2.0)
    else :
        p = Pool(chunks)
        results = []
        chunk_size = 4.0 / chunks
        for i in range(0, chunks) :
            xmin = -2.0 + chunk_size * i
            xmax = xmin + chunk_size
            # submit the job
            results.append(p.apply_async(actionProcessChunk, (step, maxiter, xmin, xmax)))
        # wait for results
        for res in results :
            rrx, rry = res.get()
            rx += rrx
            ry += rry
    return rx, ry

def actionPlot(b, c, rx, ry) :
    cmap = None
    if c is not None :
        cmap = c[0]
    heatmap, xedges, yedges = np.histogram2d(rx, ry, bins=b)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower', cmap=cmap)
    plt.show()

parser = argparse.ArgumentParser(description='Mandelbrot set generator and plotter.')
parser.add_argument('--generate', nargs=2, metavar=('N', 'maxiter'), type=int, help='generate Mandelbrot set from NxN grid and at most maxiter iterations per point')
parser.add_argument('--threads', nargs=1, metavar=('n'), type=int, default=[1], help='number of threads to be use during dataset generation')
parser.add_argument('--save', nargs=1, metavar=('filename'), help='save generated set to a file')
parser.add_argument('--load', nargs=1, metavar=('filename'), help='load generated set from a file')
parser.add_argument('--plot', nargs=1, metavar=('b'), type=int, help='generate plot of Mandelbrot set as 2D histogram with b bins')
parser.add_argument('--colormap', nargs=1, metavar=('c'), help='colormap of the plot (ex. gray, jet, plasma, inferno, viridis, magma)')
args = parser.parse_args()

rx = []
ry = []
if args.generate is not None :
    rx, ry = actionGenerate(args.generate[0], args.generate[1], args.threads[0])

if args.save is not None :
    pickle.dump((rx, ry), open(args.save[0], 'wb'))

if args.load is not None :
    (rx, ry) = pickle.load(open(args.load[0], 'rb'))

if args.plot is not None :
    if len(rx) != len(ry) :
        raise ValueError('Mandelbrot dataset is corrupted, generate a new dataset')
    if len(rx) == 0 :
        raise ValueError('No Mandelbrot dataset, use --generate or --load options before plotting')
    actionPlot(args.plot[0], args.colormap, rx, ry)
