'''
인공지능 2019
과제 3
20150439 소혜빈
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
import graphviz

#ignore warnings
import warnings
warnings.filterwarnings('ignore')

# prepare data
data = pd.read_csv('as3.csv') # read csv file in pandas dataframe
data1 = np.array(data) # change dataframe to numpy array
class_names = ['Horeca', 'Retail'] # python list of class name
feature_names = data.columns # get list of feature names from pandas dataframe

X = list(map(lambda x: x[1:], data1))
Y = list(map(lambda x: x[0], data1))

# random split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# 하단에 작성

#Decision Tree
from sklearn import tree

def myFunction1(cri):
    #train
    criterion = cri # cri : entropy or gini

    for num in np.arange(0.1, 0.6, 0.1): #num : 0.1~0.5
        min_impurity_split = num # impurity split threshold
        clf = tree.DecisionTreeClassifier(criterion=criterion,
                                          min_impurity_split=min_impurity_split)
        clf = clf.fit(x_train, y_train)

        #predict
        pred = clf.predict(x_test)

        #calculate scores
        prec = precision_score(y_test, pred, average=None)
        rec = recall_score(y_test, pred, average=None)
        f1 = f1_score(y_test, pred, average=None)

        print("\ncriterion: {}".format(criterion))
        print("impurity split threshold: {:.1f}".format(min_impurity_split))
        print("Precision_score: {:.2f},{:.2f}".format(prec[0], prec[1]))
        print("Recall_score:{:.2f},{:.2f}".format(rec[0], rec[1]))
        print("F1_score:{:.2f},{:.2f}".format(f1[0], f1[1]))

        # print graph
        dot_data = tree.export_graphviz(clf, out_file=None,
                                        feature_names=feature_names[1:8],
                                        class_names=class_names,
                                        filled=True, rounded=True,
                                        special_characters=True)

        graph = graphviz.Source(dot_data)
        graph.render("result_"+cri+"_"+str(num))

myFunction1('entropy')
myFunction1('gini')

#K Nearest Neighbor
from sklearn.neighbors import KNeighborsClassifier

def myFunction2(w):
    weights = w # w : 'uniform' or 'distance'
    for num in (1,5,10,20,30):
        k = num

        clf = KNeighborsClassifier(n_neighbors=k, weights=weights)
        clf = clf.fit(x_train, y_train)

        # predict
        pred = clf.predict(x_test)

        # calculate scores
        prec = precision_score(y_test, pred, average=None)
        rec = recall_score(y_test, pred, average=None)
        f1 = f1_score(y_test, pred, average=None)

        print("\nweights: {}".format(weights))
        print("k: {}".format(k))
        print("Precision_score: {:.2f},{:.2f}".format(prec[0], prec[1]))
        print("Recall_score:{:.2f},{:.2f}".format(rec[0], rec[1]))
        print("F1_score:{:.2f},{:.2f}".format(f1[0], f1[1]))

myFunction2('uniform')
myFunction2('distance')
