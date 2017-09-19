#-----------------------------------

#
#   In this exercise you will put the finishing touches on a perceptron class
#
#   Finish writing the activate() method by using numpy.dot and adding in the thresholded
#   activation function

import numpy

class Perceptron:

    weights = [1]
    threshold = 0
    
    def activate(self,values):
        '''Takes in @param values, a list of numbers.
        @return the output of a threshold perceptron with
        given weights and threshold, given values as inputs.
        ''' 
               
        
        #YOUR CODE HERE

        #TODO: calculate the strength with which the perceptron fires
        strength = numpy.dot(values, self.weights)
        #TODO: return 0 or 1 based on the threshold
        result = int(strength > self.threshold)
            
        return result

        
        
    def __init__(self,weights=None,threshold=None):
        if weights.all():
            self.weights = weights
        if threshold:
            self.threshold = threshold

p1 = Perceptron(numpy.array([1, 2]), 0.)
print p1.activate(numpy.array([ 1,-1]))
print p1.activate(numpy.array([-1, 1]))
print p1.activate(numpy.array([ 2,-1]))