import Layer

class Network:
    def __init__(self, layers):
        self.layers = layers
    #implement forward propagation operation:
    #this operation effectively should just call the layer level forward propagation operation