import Layer
#network should effectively just be a list of layers
class Network:
    def __init__(self, layers):
        self.layers = layers
    #implement forward propagation operation:
    #this operation effectively should just call the layer level forward propagation operation