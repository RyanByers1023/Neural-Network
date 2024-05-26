import Neuron
import numpy

#if a network is looked at as a matrix:
#The entire layer is a column, numNeurons indicates # of rows, numInputs indicates num of rows from previous column (layer).
class Layer:
    #inputNumNeurons references the number of neurons from the previous layer
    #numNeurons references the number of neurons from the current layer
    def __init__(self, inputNumNeurons, numNeurons):
        #seed random number generator
        numpy.random.seed(71)
        #below scalar is used to ensure values that the neurons are intialized with are small
        scalar = 0.01
        #parameters dictionary will be used to store both the weight and the bias for the corresponding neuron
        #how to determine which parameter entry goes with which neuron?
        #the indices tell you: parameter[W0] goes with layer[0] and so on...

        parameters = {}
        #initialize parameters
        for neuronIndex in range(1, numNeurons):
            parameters['W' + str(neuronIndex)] = numpy.random.randn(numNeurons, 1) * scalar
            parameters['b' + str(neuronIndex)]
    #implement forward propagation operation:

