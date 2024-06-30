import Neuron
import numpy

#if a network is looked at as a matrix:
#this object represents a single column of the matrix that makes up the neural network
    #inputNumNeurons references the number of neurons from the previous layer
    def __init__(self, inputNumNeurons, numNeurons):
        #seed random number generator
        numpy.random.seed(71)
        #below scalar is used to ensure values that the neurons are intialized with are small
        scalar = 0.01

        #parameters used to store both the weight and the bias for the corresponding neuron
        #W0 = first 
        self.parameters = {}
        #initialize parameters
        for neuronIndex in range(1, numNeurons):
            #initialize weights
            parameters['W' + str(neuronIndex)] = numpy.random.randn(numNeurons, 1) * scalar
            #initialize biases
            parameters['b' + str(neuronIndex)]

    #implement forward propagation operation:

