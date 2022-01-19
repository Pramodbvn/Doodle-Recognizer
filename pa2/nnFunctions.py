import numpy as np
from scipy.optimize import minimize
from math import sqrt
import pickle
'''
You need to modify the functions except for initializeWeights() 
'''

def initializeWeights(n_in, n_out):
    '''
    initializeWeights return the random weights for Neural Network given the
    number of node in the input layer and output layer

    Input:
    n_in: number of nodes of the input layer
    n_out: number of nodes of the output layer

    Output:52
    W: matrix of random initial weights with size (n_out x (n_in + 1))
    '''
    epsilon = sqrt(6) / sqrt(n_in + n_out + 1)
    W = (np.random.rand(n_out, n_in + 1) * 2 * epsilon) - epsilon
    return W


def sigmoid(z):
    '''
    Notice that z can be a scalar, a vector or a matrix
    return the sigmoid of input z (same dimensions as z)
    '''
    # remove the next line and replace it with your code
    a=np.exp(-1*z)
    b=1+a
    return 1/b

def nnObjFunction(params, *args):
    '''
    % nnObjFunction computes the value of objective function (cross-entropy
    % with regularization) given the weights and the training data and lambda
    % - regularization hyper-parameter.

    % Input:
    % params: vector of weights of 2 matrices W1 (weights of connections from
    %     input layer to hidden layer) and W2 (weights of connections from
    %     hidden layer to output layer) where all of the weights are contained
    %     in a single vector.
    % n_input: number of nodes in input layer (not including the bias node)
    % n_hidden: number of nodes in hidden layer (not including the bias node)
    % n_class: number of nodes in output layer (number of classes in
    %     classification problem
    % train_data: matrix of training data. Each row of this matrix
    %     represents the feature vector of the corresponding instance 
    % train_label: the vector of true labels of training instances. Each entry
    %     in the vector represents the truee label of its corresponding training instance.
    % lambda: regularization hyper-parameter. This value is used for fixing the
    %     overfitting problem.

    % Output:
    % obj_val: a scalar value representing value of error function
    % obj_grad: a SINGLE vector (not a matrix) of gradient value of error function
    % NOTE: how to compute obj_grad
    % Use backpropagation algorithm to compute the gradient of error function
    % for each weights in weight matrices.
    '''
    # do not remove the next 5 lines
    n_input, n_hidden, n_class, train_data, train_label, lambdaval = args
    # First reshape 'params' vector into 2 matrices of weights W1 and W2

    W1 = params[0:n_hidden * (n_input + 1)].reshape((n_hidden, (n_input + 1)))
    W2 = params[(n_hidden * (n_input + 1)):].reshape((n_class, (n_hidden + 1)))



    # remove the next two lines and replace them with your code

    # hidden layer
    X1 = np.concatenate((train_data, np.ones((train_data.shape[0], 1))), axis=1)
    netJ = np.dot(X1, W1.T)
    zJ = sigmoid(netJ)

    # output layer
    X2 = np.concatenate((zJ, np.ones((zJ.shape[0], 1))), axis=1)
    netL = np.dot(X2, W2.T)
    oL = sigmoid(netL)


    #one of k encoding
    yL=np.zeros((train_data.shape[0],oL.shape[1]),)
    rows = np.arange(train_label.size)
    yL[rows,train_label.astype(int)]=1




    #objective function
    a=-1*np.sum(yL*np.log(oL)+(1-yL)*np.log(1-oL))
    b=a/train_data.shape[0]
    c=(np.sum(W1*W1)+np.sum(W2*W2))*lambdaval*(1/(2*train_data.shape[0]))
    obj_val = b+c



    #objective_gradient
    delta_L=oL-yL
    out_grad=(((delta_L.T).dot(X2)).flatten()+lambdaval*(W2.flatten()))*(1/train_data.shape[0])



    mern=W2.shape[1]-1
    z=np.zeros((n_hidden,n_input+1))
    c=np.zeros((2,2))
    for i in range(train_data.shape[0]):
        a=(1-((zJ[i].T).reshape(n_hidden,1)))
        b=((zJ[i].T).reshape(n_hidden,1))
        c=(delta_L[i].reshape(1,n_class))*((W2.T)[0:mern,0:mern])
        z=z+(np.sum(a*b*c,axis=1)).reshape(n_hidden,1)*(X1[i].reshape(1,n_input+1))


    z=(z+(lambdaval*W1))*(1/train_data.shape[0])
    

    obj_grad = np.concatenate((z.flatten(),out_grad))





    return (obj_val,obj_grad)

def nnPredict(W1, W2, data):
    '''
    % nnPredict predicts the label of data given the parameter W1, W2 of Neural
    % Network.

    % Input:
    % W1: matrix of weights for hidden layer units
    % W2: matrix of weights for output layer units
    % data: matrix of data. Each row of this matrix represents the feature vector for the corresponding data instance

    % Output:
    % label: a column vector of predicted labels
    '''


    # hidden layer
    X1=np.concatenate((data,np.ones((data.shape[0], 1))), axis=1)
    netJ=np.dot(X1,W1.T)
    zJ=sigmoid(netJ)

    # output layer
    X2 = np.concatenate((zJ, np.ones((data.shape[0], 1))), axis=1)
    netL=np.dot(X2,W2.T)
    zL=sigmoid(netL)
    labels = np.argmax(zL,axis=1)


    return labels
