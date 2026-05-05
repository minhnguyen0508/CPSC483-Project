import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#import Categorical Naive Bayes Model
from sklearn.naive_bayes import CategoricalNB

#import Logistic Regression model 
from sklearn.linear_model import LogisticRegression

#import Decision Tree model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

#read dataset
data = pd.read_csv("student_digital_life.csv",  sep=",")

#drop unnecessary data from the data set
data.drop(columns=['parent_education_level'], inplace = True)
data.drop(columns=['internet_quality'], inplace = True)
data.drop(columns=['motivation_level'], inplace = True)
data.drop(columns=['exercise_hours'], inplace = True)
data.drop(columns=['caffeine_intake_cups'], inplace = True)
