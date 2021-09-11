# How to measure statistical causality: A Transfer Entropy Approach with Financial Applications
# source: https://towardsdatascience.com/causality-931372313a1c
# Open Quant Book: https://www.ebook.openquants.com/index.html
# GOAL: Use statistics and information theory to uncover complex causal relationships from observational data
# OBJECTIVES:
# *
import numpy as np
import matplotlib.pyplot as plt

# Random-like non-linear 2-dimensional system
def x1(n):
    if n > 0:
        return 0.441 * x1(n - 1) + np.random.normal(0,1)
    else:
        return 0

def x2(n):
    if n > 0:
        return 0.51 * (x1(n-1)**2) + np.random.normal(0,1)
    else:
        return 0

def nonlinear_sys(n_max = 1000):
    x1_vec = [x1(a) for a in range(0,n_max)]
    x2_vec = [x2(a) for a in range(0,n_max)]

    plt.scatter(x1_vec, x2_vec, alpha = .5)
    plt.title('2D Non-linear System')
    plt.xlabel('x1')
    plt.ylabel('x2')

    return x1_vec, x2_vec

x1_vec, x2_vec = nonlinear_sys()

#### =============== Statistical Causality =============== ####
# Granger causality:
# X Granger-cause Y if the future realizations o Y is better explained using the past information from X and Y rather Y alone.
