# Import statements
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

# Import the train test split
# http://scikit-learn.org/0.16/modules/generated/sklearn.cross_validation.train_test_split.html
from sklearn.model_selection  import train_test_split

# Read the data.
data = np.asarray(pd.read_csv('datalesson8-1.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y.
X = data[:,0:2]
y = data[:,2]

# Use train test split to split your data
# Use a test size of 25% and a random state of 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# TODO: Create the decision tree model and assign it to the variable model.
model = DecisionTreeClassifier()

# TODO: Fit the model to the training data.
model.fit(X_train,y_train)

# TODO: Make predictions on the test data
y_pred = model.predict(X_test)

# TODO: Calculate the accuracy and assign it to the variable acc. on the test data
acc = accuracy_score(y_test, y_pred)
