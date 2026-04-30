import numpy as np 
import pandas as pd

#import Categorical Naive Bayes Model
from sklearn.naive_bayes import CategoricalNB

#import Logistic Regression model 
from sklearn.linear_model import LogisticRegression

#import Decision Tree model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier