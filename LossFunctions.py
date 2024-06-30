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
def CalculateMSELossFunction(observedLayer, predictedLayer):
    #convert layers to numpy arrays
    observedLayer = numpy.array(observedLayer)
    predictedLayer = numpy.array(predictedLayer)

    #matrix operations for summation((y-hat - y)^2)
    squareDifference = (observedLayer - predictedLayer) ** 2

    #get number of columns (n)
    n = np.shape(observedLayer)[1]
    #divide squareDifference by n
    mse = squareDifference / n;

    #potential improvement: use numpy.mean. chatgpt was doing this, does this actually work?

    return mse

#use this to calculate the loss function relative to the next layer
#useful for backpropagation
def CalculateMSELossFunctionDerivative(observedLayer, predictedLayer):
    #create an array that is composed of the info contained within observedLayer
    observedLayer = numpy.array(observedLayer)
    #compute the summation of the 
    predictedLayer = numpy.array(predictedLayer)

    #pre calculated derivative for MSE loss function = 2(p - y). plug in and solve
    derivative = 2 * (predictedLayer - observedLayer)

    return derivative