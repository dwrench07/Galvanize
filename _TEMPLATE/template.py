"""Python Project Template
This is a sample project template for Data Science Projects

Problem Statement
# TODO: Reiterate the problem this project/model is trying to solve...

"""


"""Load libraries"""
import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


"""Load Data

Pandas is a standard here. However, if getting the data into an digestible format is needed.
Look into using 'Odo' from the Blaze Ecosystem (http://blaze.pydata.org/).
"""
filename = '/Users/david/Projects/data/phreakwatch/AllCArriers.csv'

"""
Sometimes it is good to supply your own column names. For instance when:
- column names are non-pythonic
- not supplied
- non-intuitive
- etc.
"""
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(filename, names=names)


"""Summarize Data"""

def summarize(dataset):
    """Summarize the dataset based on commonly used methods.

    :param dataset:
    :return None:
    """
    print(f"Dataset Shape:\n{dataset.shape}\n")

    print(f"Dataset Head:\n{dataset.head()}\n")

    print(f"Numeric Data Descriptions:\n{dataset.describe()}\n")

    print(f"Object Data Descriptions:\n{dataset.describe(exclude=[np.number])}\n")


# look at class distributions
print(dataset.groupby('class').size())

# Data visualizations


"""Prepare Data"""
# Data Cleaning
# Feature Selection
# Data Transforms

"""Evaluate Algorithms"""
# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y,
    test_size=validation_size, random_state=seed)

# Test options and evaluation metric

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=10, random_state=seed)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

# Compare Algorithms
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()


"""Improve Accuracy"""
# a) Algorithm Tuning
# b) Ensembles

"""Finalize Model"""
# Predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

#  Create standalone model on entire training dataset
# Save model for later use