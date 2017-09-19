#
#   Python Neural Networks code originally by Szabo Roland and used by permission
#
#   Modifications, comments, and exercise breakdowns by Mitchell Owen, (c) Udacity
#
#   Retrieved originally from http://rolisz.ro/2013/04/18/neural-networks-in-python/
#
#
#	Neural Network Sandbox
#
#	Define an activation function activate(), which takes in a number and returns a number.
#	Using test run you can see the performance of a neural network running with that activation function.
#
import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))


def activate(strength):
    return np.power(strength,2)
    
def activation_derivative(activate, strength):
    #numerically approximate
    return (activate(strength+1e-5)-activate(strength-1e-5))/(2e-5)