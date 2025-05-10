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

W = np.random.randn(10, 784) * 0.01
b = np.zeros(10)
W_new, b_new = backprop_step(x, y, [W], [b], learning_rate=0.1)

print("Updated weights shape:", W_new[0].shape)  # Expected: (10, 784)
print("Updated bias shape:", b_new[0].shape)     # Expected: (10,)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    sx = sigmoid(x)
    return sx * (1 - sx)

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # stability
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def one_hot(y, num_classes=10):
    return np.eye(num_classes)[y]

def backprop_step_2layer(x, y, weights_list, bias_list, learning_rate):
    W1, W2 = weights_list    # W1: (n_hidden, 784), W2: (10, n_hidden)
    b1, b2 = bias_list       # b1: (n_hidden,), b2: (10,)

    # Forward pass
    z1 = x @ W1.T + b1        # (n_samples, n_hidden)
    a1 = sigmoid(z1)          # (n_samples, n_hidden)
    z2 = a1 @ W2.T + b2       # (n_samples, 10)
    y_hat = softmax(z2)       # (n_samples, 10)

    # One-hot encode true labels
    y_true = one_hot(y, num_classes=10)

    # Backpropagation
    dz2 = (y_hat - y_true) / x.shape[0]   # (n_samples, 10)
    dW2 = dz2.T @ a1                      # (10, n_hidden)
    db2 = np.sum(dz2, axis=0)            # (10,)

    da1 = dz2 @ W2                       # (n_samples, n_hidden)
    dz1 = da1 * sigmoid_derivative(z1)   # (n_samples, n_hidden)
    dW1 = dz1.T @ x                      # (n_hidden, 784)
    db1 = np.sum(dz1, axis=0)           # (n_hidden,)

    # Gradient descent update
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    return [W1, W2], [b1, b2]

W1 = np.random.randn(64, 784) * 0.01
b1 = np.zeros(64)
W2 = np.random.randn(10, 64) * 0.01
b2 = np.zeros(10)
W_new, b_new = backprop_step_2layer(x, y, [W1, W2], [b1, b2], learning_rate=0.1)
print("W1 shape:", W_new[0].shape)   # Expected: (64, 784)
print("b1 shape:", b_new[0].shape)   # Expected: (64,)
print("W2 shape:", W_new[1].shape)   # Expected: (10, 64)
print("b2 shape:", b_new[1].shape)   # Expected: (10,)

def backprop_multi_hidden(x, y, weights_list, bias_list, learning_rate):
    num_layers = len(weights_list)
    activations = [x]
    pre_activations = []

    for i in range(num_layers):
        z = activations[-1] @ weights_list[i].T + bias_list[i]
        pre_activations.append(z)
        a = sigmoid(z) if i < num_layers - 1 else softmax(z)
        activations.append(a)

    grads_W = [None] * num_layers
    grads_b = [None] * num_layers
    y_true = one_hot(y)
    delta = (activations[-1] - y_true) / x.shape[0]

    for i in reversed(range(num_layers)):
        grads_W[i] = delta.T @ activations[i]
        grads_b[i] = np.sum(delta, axis=0)
        if i > 0:
            da = delta @ weights_list[i]
            delta = da * sigmoid_derivative(sigmoid(pre_activations[i - 1]))

    for i in range(num_layers):
        weights_list[i] -= learning_rate * grads_W[i]
        bias_list[i] -= learning_rate * grads_b[i]

    return weights_list, bias_list

# Initialize 784 > 64 > 32 > 10
W1 = np.random.randn(64, 784) * 0.01
W2 = np.random.randn(32, 64) * 0.01
W3 = np.random.randn(10, 32) * 0.01
b1 = np.zeros(64)
b2 = np.zeros(32)
b3 = np.zeros(10)
weights, biases = backprop_multi_hidden(x, y, [W1, W2, W3], [b1, b2, b3], learning_rate=0.1)
print("All weight shapes:", [w.shape for w in weights])

