#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.misc import comb
import matplotlib.pyplot as plt

prior = np.array([0.1, 0.4, 0.5])
head_prob = np.array([0.8, 0.6, 0.3])

e_b_history = []

for n_iter in range(1, 101):
    e_b = 0
    for r in range(n_iter + 1):
        p_xn_given_wi = head_prob ** r * (1 - head_prob) ** (n_iter - r)
        p_r_given_wi = comb(n_iter, r) * p_xn_given_wi
        p_wi_given_r = p_r_given_wi / np.sum(p_r_given_wi * prior) * prior
        e_b_r = np.min(1 - p_wi_given_r)
        p_n_r = np.sum(p_r_given_wi * prior)
        e_b += np.sum(e_b_r * p_n_r)
    print n_iter, e_b
    e_b_history.append(e_b)

plt.ylabel('Bayes error $e_b$')
plt.xlabel('number of observation $n$')
plt.plot(e_b_history)
plt.show()
