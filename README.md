## Introduction

# Requirements

Mandelbrot requires `argparse`, `numpy`, `sysconfig`, `sys`, `matplotlib`, `pickle` and `multiprocessing`. To run Least-Squares method you need only `argparse`, `numpy`, and `matplotlib`

## Mandelbrot

# example commands

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

## Least-Squares

# example commands

Run Least-Squares fitting with file `millikan.txt`. Filename argument is required.

```sh
python leastsquares.py millikan.txt
```

## Report

## Homework 1 statement

Problem statement in [HW1-Problems.md](./HW1-Problems.md)
