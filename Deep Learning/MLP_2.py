class Sigmoid:
    def __call__(self, x):
        return 1 / (1 + np.exp(-x))

    def derivative(self, x):
        sig = self.__call__(x)
        return sig * (1 - sig)

class Softmax:
    def __call__(self, x):
        e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return e_x / e_x.sum(axis=1, keepdims=True)

class CrossEntropyLoss:
    def __call__(self, y_pred, y_true):
        m = y_pred.shape[0]
        log_likelihood = -np.log(y_pred[range(m), y_true])
        return np.sum(log_likelihood) / m

    def derivative(self, y_pred, y_true):
        m = y_pred.shape[0]
        grad = y_pred.copy()
        grad[range(m), y_true] -= 1
        return grad / m

import pandas as pd
import numpy as np

def load_mnist_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()  # remove rows with missing columns
    y = df.iloc[:, 0].astype(int).to_numpy()
    x = df.iloc[:, 1:].to_numpy() / 255.0  # normalize pixel values
    return x, y

import numpy as np

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # stability
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def one_hot(y, num_classes=10):
    return np.eye(num_classes)[y]

def backprop_step(x, y, weights_list, bias_list, learning_rate):
    W = weights_list[0]  # Shape: (10, 784)
    b = bias_list[0]     # Shape: (10,)

    # Forward pass
    z = x @ W.T + b            # Shape: (n_samples, 10)
    y_hat = softmax(z)         # Shape: (n_samples, 10)

    # One-hot encode true labels
    y_true = one_hot(y, num_classes=10)

    # Backward pass: compute gradients
    dz = (y_hat - y_true) / x.shape[0]       # Shape: (n_samples, 10)
    dW = dz.T @ x                            # Shape: (10, 784)
    db = np.sum(dz, axis=0)                  # Shape: (10,)

    # Gradient descent update
    W -= learning_rate * dW
    b -= learning_rate * db

    return [W], [b]

x, y = load_mnist_csv("/media/mnist_train.csv")
print("Shape of x:", x.shape)   # Expected: (60000, 784)
print("Shape of y:", y.shape)   # Expected: (60000,)
print("First label:", y[0])
print("First image vector (first 10 pixels):", x[0][:10])

# x, y from Problem 1
# Initialize weights and biases
np.random.seed(42)
W = np.random.randn(10, 784) * 0.01
b = np.zeros(10)

# Perform a backpropagation step
updated_W, updated_b = backprop_step(x, y, [W], [b], learning_rate=0.1)