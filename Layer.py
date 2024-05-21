import Neuron

#if a network is looked at as a matrix:
#The entire layer is a column, numNeurons indicates # of rows, numInputs indicates num of rows from previous column.
class Layer:
    def __init__(self, numNeurons, numInputs):
        #create a column of neurons
        self.neurons = [Neuron(numInputs) for _ in range(numNeurons)]
    #implement forward propagation operation:
