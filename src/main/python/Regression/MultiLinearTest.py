import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from Regression.MultiLinear import LinearRegression
from sklearn import metrics
from sklearn.datasets import load_boston
# import matplotlib.pyplot as plt
# import seaborn as sns


def test_function(x, y, test_size_=0.3, random_state_=101):
    """
    testing the regression according to the papams passed
    :param x: independent variable nD-Array
    :param y: dependent variable 1D-Array
    :param test_size_: size or fraction of the test data to the total data, [0.0-0.1] or [absolute num of test cases]
    :param random_state_: seed used by the random number generator in train_test_split function
    """
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size_, random_state=random_state_)
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    print('Intercept: ', lr.intercept_)
    print('Coefficients: ', lr.coef_)
    predictions = lr.predict(X_test)
    # print('Predictions: ', predictions)
    print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, predictions))
    print('Mean Squared Error: ', metrics.mean_squared_error(y_test, predictions))
    print('Root Mean Squared Error: ', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# ---------------------------Test 1------------------------------------
print('Test 1')

df1 = pd.read_csv('USA_Housing.csv')
print('Info of the dataset: \n', df1.info())
# df.head()
# df.describe()
# print(df.columns)
# sns.pairplot(df)
# sns.distplot(df['Price'])
# sns.heatmap(df.corr())
# sns.heatmap(df.corr(),annot=True)
# print(df.columns)
x1 = df1[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
          'Area Population']]
y1 = df1['Price']
test_function(x1, y1, 0.4, 101)
# ---------------------------End of Test 1------------------------------------

# ---------------------------Test 2------------------------------------
print('\nTest 2')

df2 = pd.read_csv('Ecommerce Customers')
print('Info of the dataset: \n', df2.info())
x2 = df2[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]
y2 = df2['Yearly Amount Spent']
test_function(x2, y2, 0.3, 101)
# ---------------------------End of Test 2------------------------------------

# ---------------------------Test 3------------------------------------
print('\nTest 3')

x3, y3 = load_boston(return_X_y=True)
test_function(x3, y3, 0.3, 101)
# ---------------------------End of Test 3------------------------------------
