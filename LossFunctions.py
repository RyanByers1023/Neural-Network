#I will implement a loss function called: "MSE" "Mean Squared Error"
#L = 1/n * summation from 1 to n of((y-hat - y)^2)
#n represents the number of neurons in the current layer
#1/2 can be substituted for 1/n for simplicity in the calculation of the derivative.
#y-hat = x * weight
#x represents the raw data that was streamed in to this particular neuron
#y is representative of the target value

#this function calculates a value called loss, which represents how far off the output is from the expected output y
#with this in mind, MSE is the function that needs to be minimized

import numpy

#MSE loss function:
def CalculateLossFunction(trueLayer, predictedLayer):
    #convert layers to numpy arrays
    trueLayer = numpy.array(trueLayer)
    predictedLayer = numpy.array(predictedLayer)

    #element wise operations for (y-hat - y)^2
    squareDifference = (trueLayer - predictedLayer) ** 2

    mse = numpy.mean(squareDifference)

    return mse

def CalculateLossFunctionDerivative(trueLayer, predictedLayer):
    trueLayer = numpy.array(trueLayer)
    predictedLayer = numpy.array(predictedLayer)

    derivative = 2 * (predictedLayer - trueLayer) / trueLayer.numNeurons

    return derivative