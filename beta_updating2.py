#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed(1701)

n = -1
r = -1
true_theta = 0.8

break_10 = None
break_100 = None


def beta_pdf(thetas, alpha, beta):
    return stats.beta.pdf(thetas, alpha, beta)


def animate(nframe):
    global n, r, true_theta, draw_title, break_10, break_100
    alpha = 1 + r
    beta = 1 + n - r

    thetas = [t for t in np.arange(0, 1.001, 0.001)]
    post_s = beta_pdf(thetas, alpha, beta)

    plt.clf()
    plt.plot(thetas, post_s, label='n = %d' % n)
    plt.xlim([0, 1])
    plt.ylim([0, 35])
    plt.xlabel('$\\theta$')
    plt.ylabel('$p(\\theta | {\\bf x}^{(%d)}) = {\\rm Be}(%d, %d)$'
               % (n, alpha, beta))

    x = np.random.rand()

    # head
    if x <= true_theta:
        r += 1

    if n == 10:
        break_10 = (thetas, post_s)
    if n >= 10:
        plt.plot(break_10[0], break_10[1], label='n = 10')
    if n == 100:
        break_100 = (thetas, post_s)
    if n >= 100:
        plt.plot(break_100[0], break_100[1], label='n = 100')

    n += 1

    plt.legend(loc='upper left')
    plt.savefig('imgs/%05d.png' % nframe)

    print nframe, ':', n, r, alpha, beta


def save_imgs():
    if not os.path.exists('imgs'):
        os.mkdir('imgs')
    for i in range(1002):
        animate(i)

if __name__ == '__main__':
    save_imgs()
    print subprocess.check_output([
        'mogrify', '-format', 'gif', 'imgs/*.png'])
    print subprocess.check_output([
        'rm', '-rf', 'imgs/*.png'])
    print subprocess.check_output([
        'rm', '-rf', 'imgs/00000.gif'])
    print subprocess.check_output([
        'gifsicle', '--optimize=3', '--delay=3',
        '--colors=256', '-O3', 'imgs/*.gif', '>', 'figure_4-6.gif'])
