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

class DenseLayer:
    def __init__(self, input_size, output_size, activation):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.biases = np.zeros((1, output_size))
        self.activation = activation()

    def forward(self, X):
        self.input = X
        self.z = np.dot(X, self.weights) + self.biases
        self.output = self.activation(self.z)
        return self.output

    def backward(self, grad_output, learning_rate):
        activation_derivative = self.activation.derivative(self.z)
        grad = grad_output * activation_derivative
        grad_w = np.dot(self.input.T, grad)
        grad_b = np.sum(grad, axis=0, keepdims=True)

        self.weights -= learning_rate * grad_w
        self.biases -= learning_rate * grad_b

        return np.dot(grad, self.weights.T)

class NeuralNetwork:
    def __init__(self):
        self.layers = []

    def add(self, layer):
        self.layers.append(layer)

    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def backward(self, grad, learning_rate):
        for layer in reversed(self.layers):
            grad = layer.backward(grad, learning_rate)

    def train(self, X, y, loss_fn, epochs=10, learning_rate=0.01):
        for epoch in range(epochs):
            out = self.forward(X)
            loss = loss_fn(out, y)
            print(f"Epoch {epoch + 1}, Loss: {loss:.4f}")
            grad = loss_fn.derivative(out, y)
            self.backward(grad, learning_rate)

import pandas as pd
import numpy as np

def load_mnist_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()  # remove rows with missing columns
    y = df.iloc[:, 0].astype(int).to_numpy()
    x = df.iloc[:, 1:].to_numpy() / 255.0  # normalize pixel values
    return x, y

x, y = load_mnist_csv("/media/mnist_train.csv")
print("Shape of x:", x.shape)   # Expected: (60000, 784)
print("Shape of y:", y.shape)   # Expected: (60000,)
print("First label:", y[0])
print("First image vector (first 10 pixels):", x[0][:10])