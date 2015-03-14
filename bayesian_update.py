#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

prior = [0.1, 0.4, 0.5]
head_prob = [0.8, 0.6, 0.3]

n_class = 3
n_iter = 100

target_j = 0

posterior_history = []
for i in range(n_iter):
    x = np.random.rand()

    # head
    if x <= head_prob[target_j]:
        for j in range(n_class):
            norm = np.sum([prior[k] * head_prob[k]
                           for k in range(n_class)])
            prior[j] = head_prob[j] * prior[j] / norm
    # tail
    else:
        for j in range(n_class):
            norm = np.sum([prior[k] * (1 - head_prob[k])
                           for k in range(n_class)])
            prior[j] = (1 - head_prob[j]) * prior[j] / norm

    posterior_history.append(np.copy(prior))

posterior_history = np.asarray(posterior_history)
plt.ylabel('posterior probability')
plt.xlabel('iteration')
plt.plot(np.arange(len(posterior_history)), posterior_history[:, 0],
         label='coin 1')
plt.plot(np.arange(len(posterior_history)), posterior_history[:, 1],
         label='coin 2')
plt.plot(np.arange(len(posterior_history)), posterior_history[:, 2],
         label='coin 3')
plt.legend()
plt.show()
