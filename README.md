# Introduction

## Requirements

Mandelbrot requires `argparse`, `numpy`, `sysconfig`, `sys`, `matplotlib`, `pickle` and `multiprocessing`. To run Least-Squares method you need only `argparse`, `numpy`, and `matplotlib`

# Mandelbrot

Following figures were generated using `mandelbrot.py` program with grid size of `1000x1000` and maximum number of iterations with `1000`, then plotted as `200` bins histogram.

![Figure displaying Mandelbrot set in grayscale](https://github.com/nyu-compphys-2017/hw1-marekyggdrasil/blob/master/figure_mandelbrot_gray.png?raw=true "Mandelbrot Grayscale")
![Figure displaying Mandelbrot set in jet colormap](https://github.com/nyu-compphys-2017/hw1-marekyggdrasil/blob/master/figure_mandelbrot_jet.png?raw=true "Mandelbrot Jet")

## example commands

Getting some help.

```sh
python mandelbrot.py --help
```

Generating Mandelbrot set with grid size of 30x30 and saving it to file `dataset.p`.

```sh
python mandelbrot.py --generate 30 100 --save dataset.p
```

Loading Mandelbrot dataset from `dataset.p` and plotting it using as 2D histogram with 100 bins and `Inferno` color map.

```sh
python mandelbrot.py --load dataset.p --plot 100 --colormap inferno
```

Second and third commands without saving dataset to file, ignoring color map.

```sh
python mandelbrot.py --generate 30 100 --plot 100
```

Generating Mandelbrot dataset in multiprocessing mode with two threads.

```sh
python mandelbrot.py --generate 30 100 --threads 2 --save dataset.p
```

# Least-Squares

Millikan dataset demonstrating photoelectric effect with line fitted to is using `leastsquares.py`.

![Figure displaying Least-Squares fit to Millikan dataset](https://github.com/nyu-compphys-2017/hw1-marekyggdrasil/blob/master/figure_leastsquares_fit.png?raw=true "Millikan Dataset")

Zoom in for to show more clearly that fitted line does not overlap all the points.

![Figure displaying Least-Squares fit to Millikan dataset zoomed in](https://github.com/nyu-compphys-2017/hw1-marekyggdrasil/blob/master/figure_leastsquares_zoom.png?raw=true "Millikan Dataset (zoom)")

## example commands

Run Least-Squares fitting with file `millikan.txt`. Filename argument is required.

```sh
python leastsquares.py millikan.txt
```

# Report

Please consult the file [report.pdf](./report.pdf)

# Homework 1 statement

Problem statement in [HW1-Problems.md](./HW1-Problems.md)
