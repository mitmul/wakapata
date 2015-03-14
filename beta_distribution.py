#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma


def beta_pdf(alpha, beta):
    coeff = gamma(alpha + beta) / (gamma(alpha) * gamma(beta))

    return [coeff * (t ** (alpha - 1)) * ((1 - t) ** (beta - 1))
            for t in np.arange(0, 1.01, 0.01)]


def draw_beta_pdf(alpha, beta):
    plt.plot([t for t in np.arange(0, 1.01, 0.01)],
             beta_pdf(alpha, beta),
             label='${\\rm Be}(%d, %d)$' % (alpha, beta))

draw_beta_pdf(1, 5)
draw_beta_pdf(3, 9)
draw_beta_pdf(16, 16)
draw_beta_pdf(6, 6)
draw_beta_pdf(1, 1)
draw_beta_pdf(5, 1)
draw_beta_pdf(9, 3)

plt.xlabel('$\\theta$')
plt.ylabel('$P(\\theta;\\alpha, \\beta)$')
plt.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
plt.subplots_adjust(right=0.8)
plt.show()
