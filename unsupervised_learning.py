#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1701)

c = 3  # wi = 0, 1, 2
m = 2  # vk = 0, 1
n = 10000

# true pi
pi_tilde = np.array([0.1, 0.4, 0.5])
print 'pi_tilde:', pi_tilde

# initialize pi
pi = np.array([0.3, 0.5, 0.2])
print 'initial_pi:', pi

# initialize theta
theta = np.array([[0.8, 0.2],
                  [0.6, 0.4],
                  [0.3, 0.7]])
print 'theta:'
print theta


def retrieve_w():
    cum = np.cumsum(pi_tilde)
    tmp = np.random.rand()

    # if wi=0
    if tmp < cum[0]:
        return 0

    # if wi=1
    elif tmp < cum[1]:
        return 1

    # if wi=2
    else:
        return 2


def retrieve_v(wi):
    cum = np.cumsum(theta[wi, :])
    tmp = np.random.rand()

    if tmp < cum[0]:
        return 0
    else:
        return 1

# throwing dice
r = np.array([0, 0])
for _ in range(n):
    # throwing dice
    xt = retrieve_v(retrieve_w())
    if xt == 0:
        r[0] += 1
    else:
        r[1] += 1


def p_w_v(pi, theta):
    nume = theta.T * pi
    deno = np.sum(nume, axis=1)

    return nume.T / deno


pi_history = []
negative_log = []
for t in range(1, n + 1):
    # update pi
    pi = np.sum(p_w_v(pi, theta) * r, axis=1) / n

    p_vk = np.sum(theta.T * pi, axis=1)
    p_x = np.sum(r * np.log(p_vk))

    pi_history.append(pi)
    negative_log.append(p_x)

plt.xlabel('iteration $t$')
plt.ylabel('$\log P({\\bf x})$')
plt.xlim([0, 50])
plt.plot(negative_log)
plt.savefig('figure_5-2.png')

pi_history = np.asarray(pi_history)
plt.clf()
plt.ylim([0, 0.55])
plt.xlim([0, 50])
plt.plot(np.arange(50), np.ones(50) * 0.5, 'k--')
plt.plot(np.arange(50), np.ones(50) * 0.4, 'k--')
plt.plot(np.arange(50), np.ones(50) * 0.1, 'k--')
plt.plot(pi_history[:, 0], label='$\\pi_1$')
plt.plot(pi_history[:, 1], label='$\\pi_2$')
plt.plot(pi_history[:, 2], label='$\\pi_3$')
plt.xlabel('iteration $t$')
plt.ylabel('$\\pi_i (i=1,2,3)$')
plt.legend(bbox_to_anchor=(1, 1.02), loc='upper left')
plt.subplots_adjust(right=0.8)
plt.savefig('figure_5-3.png')
