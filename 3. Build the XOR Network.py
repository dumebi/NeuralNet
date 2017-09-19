#
#   In this exercise, you will create a network of perceptrons which
#   represent the xor function use the same network structure you used
#   in the previous quizzes.
#
#   You will need to do two things:
#   First, create a network of perceptrons with the correct weights
#   Second, define a procedure EvalNet() which takes in a list of 
#   inputs and ouputs the value of this network.

import numpy as np

class Perceptron:

    weights = [1]
    threshold = 0
    
    def evaluate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = np.dot(values[i],self.weights[i])
        
        #Then evaluate the return value of the perceptron
        if strength >= self.threshold:
            result = 1
        else:
            result = 0

        return result

    def __init__(self,weights=None,threshold=None):
        if weights.all():
            self.weights = weights
        if threshold:
            self.threshold = threshold
            

Network = [
    # input layer, declare input layer perceptrons here
    [Perceptron(np.array([1, 1]), 0.5), Perceptron(np.array([-1, -1]), -1.5)],
    # output node, declare output layer perceptron here
    [Perceptron(np.array([1, 1]), 1.5)]
]


def EvalNetwork(inputValues, Network):
    results = [node.activate(inputValues) for node in Network[0]]
    outputValue = Network[1][0].activate(np.array(results))
    return outputValue


def test():
    """
    A few tests to make sure that the perceptron class performs as expected.
    """
    print "0 XOR 0 = 0?:", EvalNetwork(np.array([0,0]), Network)
    print "0 XOR 1 = 1?:", EvalNetwork(np.array([0,1]), Network)
    print "1 XOR 0 = 1?:", EvalNetwork(np.array([1,0]), Network)
    print "1 XOR 1 = 0?:", EvalNetwork(np.array([1,1]), Network)

test()