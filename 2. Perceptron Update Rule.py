#-----------------------------------

#
#   In this exercise we write a perceptron class
#   which can update its weights
#
#   Your job is to finish the train method so that it implements the perceptron update rule

import numpy as np

class Perceptron:

    weights = [1]
    threshold = 0
    
    def activate(self,values):
        '''Takes in @param values, @param weights lists of numbers
        and @param threshold a single number.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        #First calculate the strength with which the perceptron fires
        strength = np.dot(values,self.weights)
        
        if strength>self.threshold:
            result = 1
        else:
            result = 0
            
        return result

    def update(self,values,train,eta=.1):
        '''Takes in a 2D array @param values and a 1D array @param train,
        consisting of expected outputs for the inputs in values.
        Updates internal weights according to the perceptron training rule
        using these values and an optional learning rate, @param eta.
        '''
        #YOUR CODE HERE
        #update self.weights based on the training data
        for x, y in zip(values, train):
            y_pred = self.activate(x)
            for i, x_i in enumerate(x):
                self.weights[i] += (y - y_pred) * eta * x_i


        
        
    def __init__(self,weights=None,threshold=None):
        if weights.all():
            self.weights = weights
        if threshold:
            self.threshold = threshold

def sum_almost_equal(array1, array2, tol=1e-6):
    return sum(abs(array1 - array2)) < tol

p1 = Perceptron(np.array([1, 1, 1]), 0)
p1.update(np.array([[2, 0, -3]]), np.array([1]))
print sum_almost_equal(p1.weights, np.array([1.2, 1, 0.7]))

p2 = Perceptron(np.array([1,2,3]),0)
p2.update(np.array([[3,2,1],[4,0,-1]]),np.array([0,0]))
print sum_almost_equal(p2.weights, np.array([0.7, 1.8, 2.9]))

# p3 = Perceptron(np.array([3,0,2]),0)
# p3.update(np.array([[2,-2,4],[-1,-3,2],[0,2,1]]),np.array([0,1,0]))
# print sum_almost_equal(p3.weights, np.array([2.7, -0.3, 1.7]))