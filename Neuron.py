import numpy
import ActivationFunctions as ActivFunc

class Neuron:
    def __init__(self, num_inputs):
        #The collection of weights and the neuron's bias will be intialized to random values, and I will train the network using backpropagation (NOT IMPLEMENTED)
        self.weights = numpy.random.rand(num_inputs)
        self.bias = numpy.random.rand()

    #available activation functions:

    def ReLuActivation(self, preActivationValue):
        return ActivFunc.ReLuActivation(preActivationValue)

    def SigmoidActivation(self, preActivationValue):
        return ActivFunc.SigmoidActivation(preActivationValue)
    
    def TanhActivation(self, preActivationValue):
        return ActivFunc.TanhActivation(preActivationValue)

    def PropagateForward(self, inputs):
        #calculate dot product between the inputs obtained from the previous layer and the weights this neuron has assigned to them respectively
        totalInput = numpy.dot(inputs, self.weights) + self.bias
        #pass this value through an activation function, in this case, I am using ReLu
        return self.ReLuActivation(totalInput)
