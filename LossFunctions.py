#I will implement a loss function called: "MSE" "Mean Squared Error"
#L = 1/n * summation from 1 to n of((y-hat - y)^2)
#1/2 can be substituted for 1/n for simplicity in the calculation of the derivative
#y-hat = x * weight
#x represents the raw data that was streamed in to this particular neuron
#y is representative of the target value
#n represents the number of neurons in the output layer

#this function calculates a value called loss, which represents how far off the output is from the expected output y