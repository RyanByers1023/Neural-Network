#activation functions are required for achieving a value between 0 and 1. Values between 0 and 1 are useful in probability type problems. Neural networks therefore can output probabilities relative to recognition/prediction problems. Eg. there is a x% chance this is one thing compared to another/or the best next thing I should say relative to this input (text/image) is probably this and there is a x% certainty that i am correct in this analysis.
#what problem do i want to solve: TBD

#Non-linear activation functions are required for backpropagation
#EX: f(x) = x (this is a linear function b/c the value of the highest exponent relative to an unknown value x is 1) f'(x) = 1. f''(x) = 0. f'''(x) = 0... there is no way to extract information from this via taking the derivative of f(x)...
#this is why I must use a non-linear activation function like ReLu

#backpropagation involves the automatic adjustment of biases and weights relative to a partiuclar neuron in order to achieve the goal of minimization of error
#error is determined by calculating the difference between the output (probablities something is one thing vs another) the neural network provided vs. what the output SHOULD be.
#this difference can be represented as a function (the error function)
#therefore, minimization of this function is the primary goal of the backpropagation process
#minimization of any function is determined by the negative gradient, the gradient is the direction of greatest ascent, the negative of this is then the direction of greatest descent, represented by a vector
#"To find the gradient, take the derivative of the function with respect to x, then substitute the x-coordinate of the point of interest in for the x values in the derivative." -socratic.org
#use this as a pointer to determine which weights to reduce/increase and which biases to reduce/increase for each individual layer.

#it is clear that this process must include data with known outputs so the error function can be determined, and the network can be trained.
#i need to find somewhere to source this data...

