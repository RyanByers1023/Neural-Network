import numpy
import ActivationFunctions as ActivFunc

class Neuron:
    def __init__(self, num_inputs):
        #The collection of weights and the neuron's bias will be intialized to random values, and I will train the network using backpropagation (NOT IMPLEMENTED)
        self.weights = numpy.random.rand(num_inputs)
        self.bias = numpy.random.rand()

    #available activation functions:
    
    def ReLuActivation(self, neuronValue):
        return ActivFunc.ReLuActivation(neuronValue)

    def SigmoidActivation(self, neuronValue):
        return ActivFunc.SigmoidActivation(neuronValue)
    
    def TanhActivation(self, neuronValue):
        return ActivFunc.TanhActivation(neuronValue)
