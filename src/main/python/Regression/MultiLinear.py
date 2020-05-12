import numpy as np


class LinearRegression:

    def __init__(self):
        self.intercept_ = None
        self.coef_ = None

    def fit(self, _x, _y):
        """
        to find the intercept and coefficients
        :param _x: independent variable nD-Array
        :param _y: dependent variable 1D-Array
        :update: updates the class variables coef_ and intercept_
        """
        #  θ0 is the intercept, θ1, θ2, θ3, θ4 and θ5 are the coefficients
        row, col = _x.shape
        x_ones = np.ones((row, 1))
        X_train = np.append(x_ones, _x, axis=1)

        x_transpose = np.transpose(X_train)
        x_transpose_dot_x = x_transpose.dot(X_train)

        var1 = np.linalg.inv(x_transpose_dot_x)
        var2 = x_transpose.dot(_y)

        theta = var1.dot(var2)

        self.intercept_ = theta[0]
        self.coef_ = theta[1:]

        return

    def predict(self, _x):
        """
        predicts the dependent variable values based on independent variable, uses intercept and coefficients
        which are calculated from fit function
        :param _x: independent variable nD-Array
        :return: returns the predicted values.
        """
        if self.coef_ is None or self.intercept_ is None:
            return None
        row, col = _x.shape
        x_ones = np.ones((row, 1))
        X_test = np.append(x_ones, _x, axis=1)
        theta = list(self.coef_)
        theta.insert(0, self.intercept_)
        predicted_values = np.dot(X_test, theta)
        return predicted_values
