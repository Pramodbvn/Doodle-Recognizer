# Doodle-Recognizer
Neural-networks
While we can use ‘basis function expansion’ or ‘kernel methods’ for building a non- linear modelling, in real life scenarios it is very difficult to choose what functions to use for either of these methods. On the other hand, Neural networks captures the non-linear relationship between Input data and the output labels naturally, and thus they are very powerful.
Report-1
1. the evaluation of the implemented neural network with hidden layer having 50 nodes is as below (for this specific run).
  Train accuracy Test accuracy runtime
65.16%
63.04% 110.81 seconds
      2. Below are the test and train accuracies for various number of hidden layer units ranging from 10 to 100 with a step value of 10.
    Number of Nodes
      10
      20
      30
      40
      50
      60
      70
      80
Train accuracy
46.09% 57.50% 60.90% 65.68% 66.55% 67.87% 68.52% 69.02%
Test accuracy
45.36% 55.84% 58.76% 63.04% 63.62% 64.95% 65.14% 64.79%
Generalization error
0.73% 1.66% 2.14% 2.64% 2.93% 2.92% 3.38% 4.23%
                                
90
70.26%
66.60%
3.66%
100
71.45%
67.19%
4.26%
  80.00% 70.00% 60.00% 50.00% 40.00% 30.00% 20.00% 10.00%
0.00%
Number of hidden layer Units vs Accuracy
           10 20 30 40 50 60 70 80 90 100 Number of hidden layer units
Train accuracy Test accuracy Generalization error
  300
250
200
150
100
50
0
10 20 30 40 50 60 70 80 90 100
Number of hidden layer nodes
        Observation:
a) From the plot, it can be observed that the optimal number of hidden layer units(M) is 100 as both test and train accuracies are highest when compared with rest of the values.
Optimal value of M 100
    Training time(seconds) Accuracy

b) It is worth to mention that, for M=90, also has similar accuracies as M=100 with less generalization error. Since the difference in generalization error is not significant, M=100 is chosen as an optimal value. In case if the accuracies for any two models are same, it is better to choose a simpler model to avoid over-fitting.
*since the initial weights are selected by using NumPy random function, the values above may vary during each run due to the fact that while finding the optimal weights, gradient descent may end up at different local optimum based on the initial weights. However, a similar trend has been observed on multiple runs.
3.The train and test accuracies for different values of lambda are shown below along with generalization error where number of hidden layer units M =100.
    Lambda
Test Accuracy
0 69.78% 2 70.21% 4 70.90% 6 71.56% 8 71.18%
10 71.10% 12 71.21% 14 71.06% 16 68.48% 18 71.24%
Train Accuracy
65.82% 66.10% 66.55% 66.93% 66.52% 66.31% 66.90% 66.45% 64.87% 66.75%
generalization error
3.96% 4.11% 4.35% 4.63% 4.66% 4.79% 4.31% 4.61% 3.61% 4.49%
                                          20
   71.62%
   67.31%
   4.31%
 
  80.00% 70.00% 60.00% 50.00% 40.00% 30.00% 20.00% 10.00%
0.00%
Lambda values vs accuracies
           0 2 4 6 8 10 12 14 16 18 20 Lambda
Test Accuracy Train Accuracy generalization error
  230 225 220 215 210 205 200 195 190 185 180
Training time vs Lambda values
                  0 5 10 15 20 25 lambda
Observation: for this particular run, Lambda=20 gave the highest test and train accuracy with a generalization error of 4.31%. For this reason, it is chosen as an optimal value. For different set of runs, optimal lambda value is varying. We observed Lambda values {6,18,20} as optimal for multiple runs where optimal lambda to be 20 is observed in most of the cases.
Training time(seconds) Accuracy

  Optimal value of 20 Lambda
4. For optimal values, M=100 and lambda=20, We observed that our model makes more mistakes on the class ‘arm’. On Visual inspection, we understand that model is confusing between the classes ‘banana’ and ‘arm’ because of the similarity in the drawings.
We can further improve the performance of our model by the following:
➔Increasing the number of hidden layers
➔Changing the activation function at either hidden layer or at output layer or
both
➔Using a different architecture for neural network instead of multi-layer
perceptron
Report-2
1.Fixing the number of hidden layer units at 100, below are the accuracies we got by varying the number of hidden layers from 1 to 5
       Number of hidden layers(L)
1
3 4 5
Train
accuracy Test Accuracy
78.64% 74.22%
80.24% 76.08% 79.46% 75.60% 78.28% 74.69%
Training time
56.07 seconds
66.29 seconds 72.10 seconds 74.81 seconds
generalization error
4.42%
4.16% 3.86% 3.59%
       2
   82.55%
   76.59%
   59.41 seconds
   5.96%
                
  90.00% 80.00% 70.00% 60.00% 50.00% 40.00% 30.00% 20.00% 10.00%
0.00%
Number of hidden layers vs Accuracies
            12345 Train accuracy Test Accuracy generalization error
  80
70
60
50
40
30
20
10
Training time vs Number of hidden layers
                0
0123456
Number of hidden layers
 Observation: It is observed that for L=2, the test and train accuracies are the highest as well with a less training time. So, Number of layers equals 2 looks like an optimal value
Optimal number of 2 hidden layers
    Training time(seconds)

2.
   activation function
Tanh Relu
Train accuracy
79.92% 74.71%
test accuracy
76.05% 63.78%
Sigmoid
82.55%
76.59%
      The best activation function to use for this problem is ”Sigmoid”
