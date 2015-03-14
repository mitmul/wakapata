#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

n = 10

r = 3
p_xn_theta = np.array([theta ** r * (1 - theta) ** (n - r)
                       for theta in np.arange(0, 1.01, 0.01)])
plt.plot([t for t in np.arange(0, 1.01, 0.01)], p_xn_theta,
         label='r = 3')

r = 8
p_xn_theta = np.array([theta ** r * (1 - theta) ** (n - r)
                       for theta in np.arange(0, 1.01, 0.01)])
plt.plot([t for t in np.arange(0, 1.01, 0.01)], p_xn_theta,
         label='r = 8')
plt.xlabel('$\\theta$')
plt.ylabel('$P({\\bf x}^{(n)};\\theta)$')
plt.legend(loc='upper left')
plt.show()
