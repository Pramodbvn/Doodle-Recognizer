

**Programming Assignment-2 Report**

**Group number 22**

**Course number 574**

**Members** Meghana Raj Kalidindi(50385493)

Prashant Jitendra Kalyani(50388408)

Venkata Naga Pramod Bikkina (50366406)

**Neural-networks**

While we can use ‘basis function expansion’ or ‘kernel methods’ for building a non-

linear modelling, in real life scenarios it is very difficult to choose what functions to

use for either of these methods. On the other hand, Neural networks captures the

non-linear relationship between Input data and the output labels naturally, and thus

they are very powerful.

**Report-1**

\1. the evaluation of the implemented neural network with hidden layer having 50

nodes is as below (for this specific run).

**Train accuracy**

**Test accuracy**

**runtime**

**65.16%**

**63.04%**

**110.81 seconds**

\2. Below are the test and train accuracies for various number of hidden layer units

ranging from 10 to 100 with a step value of 10.

**Number of Nodes**

**Train accuracy Test accuracy**

**Generalization error**

0.73%

10

20

30

40

50

60

70

80

90

100

46.09%

57.50%

60.90%

65.68%

66.55%

67.87%

68.52%

69.02%

70.26%

71.45%

45.36%

55.84%

58.76%

63.04%

63.62%

64.95%

65.14%

64.79%

66.60%

67.19%

1.66%

2.14%

2.64%

2.93%

2.92%

3.38%

4.23%

3.66%

4.26%





Number of hidden layer Units vs Accuracy

80.00%

70.00%

60.00%

50.00%

40.00%

30.00%

20.00%

10.00%

0.00%

10

20

30

40

50

60

70

80

90

100

Number of hidden layer units

Train accuracy

Test accuracy

Generalization error

300

250

200

150

100

50

0

10

20

30

40

50

60

70

80

90

100

Number of hidden layer nodes

**Observation:**

a) From the plot, it can be observed that the optimal number of hidden layer

units(**M)** is **100** as both test and train accuracies are highest when compared

with rest of the values.

**Optimal value of M 100**





b) It is worth to mention that, for M=90, also has similar accuracies as M=100

with less generalization error. Since the difference in generalization error is

not significant, M=100 is chosen as an optimal value. *In case if the*

*accuracies for any two models are same, it is better to choose a simpler*

*model to avoid over-fitting*.

\*since the initial weights are selected by using NumPy random function, the values above may vary

during each run due to the fact that while finding the optimal weights, gradient descent may end up at

different local optimum based on the initial weights. However, a similar trend has been observed on

multiple runs.

3.The train and test accuracies for different values of lambda are shown below

along with generalization error where number of hidden layer units **M =100**.

**Lambda**

**Test Accuracy**

69.78%

**Train Accuracy**

65.82%

**generalization error**

3.96%

0

2

4

6

8

10

12

14

16

18

20

70.21%

70.90%

71.56%

71.18%

71.10%

71.21%

71.06%

68.48%

71.24%

71.62%

66.10%

66.55%

66.93%

66.52%

66.31%

66.90%

66.45%

64.87%

66.75%

67.31%

4.11%

4.35%

4.63%

4.66%

4.79%

4.31%

4.61%

3.61%

4.49%

4.31%





Lambda values vs accuracies

80.00%

70.00%

60.00%

50.00%

40.00%

30.00%

20.00%

10.00%

0.00%

0

2

4

6

8

10

12

14

16

18

20

Lambda

Test Accuracy

Train Accuracy

generalization error

Training time vs Lambda values

230

225

220

215

210

205

200

195

190

185

180

0

5

10

15

20

25

lambda

**Observation**: for this particular run, Lambda=20 gave the highest test and train

accuracy with a generalization error of 4.31%. For this reason, it is chosen as an

optimal value. For different set of runs, optimal lambda value is varying. We

observed Lambda values {6,18,20} as optimal for multiple runs where optimal

lambda to be 20 is observed in most of the cases.





**Optimal value of**

**Lambda**

**20**

\4. For optimal values, M=100 and lambda=20, **We observed that our model**

**makes more mistakes on the class ‘arm’.** On Visual inspection, we understand

that model is confusing between the classes **‘banana’** and **‘arm’** because of the

similarity in the drawings.

We can further improve the performance of our model by the following:

➔ Increasing the number of hidden layers

➔ Changing the activation function at either hidden layer or at output layer or

both

➔ Using a different architecture for neural network instead of multi-layer

perceptron

**Report-2**

**1.**Fixing the number of hidden layer units at 100, below are the accuracies we got

by varying the number of hidden layers from 1 to 5

**Number of hidden Train**

**layers(L) accuracy**

**generalization**

**error**

**Test Accuracy**

**Training time**

1

2

3

4

5

78.64%

82.55%

80.24%

79.46%

78.28%

74.22% 56.07 seconds

76.59% 59.41 seconds

76.08% 66.29 seconds

75.60% 72.10 seconds

74.69% 74.81 seconds

4.42%

5.96%

4.16%

3.86%

3.59%





Number of hidden layers vs Accuracies

90.00%

80.00%

70.00%

60.00%

50.00%

40.00%

30.00%

20.00%

10.00%

0.00%

1

2

3

4

5

Train accuracy

Test Accuracy

generalization error

Training time vs Number of hidden layers

80

70

60

50

40

30

20

10

0

0

1

2

3

4

5

6

Number of hidden layers

**Observation:** It is observed that for L=2, the test and train accuracies are the

highest as well with a less training time. So, Number of layers equals 2 looks like

an optimal value

**Optimal number of 2**

**hidden layers**





\2.

**activation function**

**Train accuracy**

82.55%

**test accuracy**

76.59%

Sigmoid

Tanh

79.92%

76.05%

Relu

74.71%

63.78%

The best activation function to use for this problem is ”**Sigmoid”**

