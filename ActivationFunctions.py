#activation functions are required for achieving a normalized value. Values between 0 and 1 are useful in probability type problems.  Neural networks therefore can output probabilities relative to recognition/prediction problems. Eg. there is a x% chance this is one thing compared to another/or the best next thing I should say relative to this input (text/image) is probably this and there is a x% certainty that i am correct in this analysis.
#what problem do i want to solve: TBD

#Non-linear activation functions are required for backpropagation
#EX: f(x) = x (this is a linear function b/c the value of the highest exponent relative to an unknown value x is 1) f'(x) = 1. f''(x) = 0. f'''(x) = 0... there is no way to extract information from this via taking the derivative of f(x)...
#this is why I must use a non-linear activation function like ReLu

#utlizing the activation function:
#calculate summation of all neurons within a particular hidden layer (column), and pass this value thorugh an activation function like ReLu. Outputs a value between 0 and 1.
#note: each neuron in a layer will be multiplied by a value called a "weight". Weights have the effect of negating or increasing the impact of any particular neuron towards the next layer. 
#so when i am "training" the network, I am trying to find the ideal weights to enchance the network's ability to produce a "good" output. This is done via "backpropogation"

#backpropagation entails the automatic (relatively speaking) adjustment of biases and weights relative to a particular neuron in order to achieve the goal of minimization of error
#error is determined by calculating the difference between the output of the neural network provided vs. what the output SHOULD be. (use a known data set that is normalized in the same way this neural network is)
#this difference can be represented as a function (the error function)
#therefore, minimization of this function is the primary goal of the backpropagation process
#minimization of any function is determined by the negative gradient, the gradient is the direction of the function's greatest ascent, the inverse (negative) of this is then the direction of greatest descent, represented by a vector
#"To find the gradient [of any function], take the derivative of the function with respect to x, then substitute the x-coordinate of the point of interest in for the x values in the derivative." -socratic.org
# What I don't understand: taking the derivative of any single variable function nets you f prime (f'(x)). This is representative of the slope of f(x). This does not net you the STEEPEST slope, but rather the exact slope at a certain position. So, why is the process to find the gradient the same as the process for finding the derivative the same when these two things gave different meanings in the context of a function?
#"Substitute the x-coordinate of the point of interest" -- this is probably what I am missing.
#How to find "the point of interest" then is the question i need an answer for. (NOT SOLVED YET)
#ANSWER: the point of interest is relative to the weight of the particular neuron we are evaluating in the context of the loss function

#use this as a pointer to determine which weights to reduce/increase and which biases to reduce/increase for each individual layer.

#it is clear that this process must include data with known outputs so the error function can be determined, and the network can be trained.
#i need to find somewhere to source this data...
#this is worth looking into: https://paperswithcode.com/datasets

#ReLu is very simple... returns the maximum value between an input neuronValue, and 0. ReLu, therefore always outputs a positive number
#BUT ReLu can output values greater than 1, so a softmax function must be applied to the final layer's outputs to clamp the neurons' outputs between 0 and 1 (if needed)
#even with this "limitation", it seems that this is still the most used activation function, and it is computationally simple, so I will use it
import math

def ReLuActivation(neuronValue):
    return max(0, neuronValue)

#this is an implementation I've sourced from here: https://stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
#it is apparently a more "numerically stable" implementation
#supposedly accounts for extremely negative values of neuronValue

def SigmoidActivation(neuronValue):
    if(neuronValue >= 0):
        z = math.exp(-neuronValue)
        return 1 / (1 + z)
    else:
        z = math.exp(neuronValue)
        return z / (1 + z)

def TanhActivation(neuronValue):
    return math.tanh(neuronValue)




