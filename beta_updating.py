#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.special import gamma


def beta_pdf(alpha, beta):
    coeff = gamma(alpha + beta) / (gamma(alpha) * gamma(beta))

    return [coeff * (t ** (alpha - 1)) * ((1 - t) ** (beta - 1))
            for t in np.arange(0, 1.01, 0.01)]


def animate(nframe):
    x = np.array([1, 1, 1, 1, 0, 1, 1, 0, 1, 0])
    n = nframe
    r = np.sum(x[:n])
    print r, n
    alpha = 1 + r
    beta = 1 + n - r
    plt.clf()
    plt.plot([t for t in np.arange(0, 1.01, 0.01)],
             beta_pdf(alpha, beta))
    plt.ylim([0, 5])
    plt.xlabel('$\\theta$')
    plt.ylabel('$p(\\theta | {\\bf x}^{(%d)}) = {\\rm Be}(%d, %d)$'
               % (nframe, alpha, beta))
    plt.title('Step: %d' % (nframe))

fig = plt.figure()

anim = animation.FuncAnimation(fig, animate, frames=11)
anim.save('figure_4-3.gif', writer='imagemagick', fps=1)
