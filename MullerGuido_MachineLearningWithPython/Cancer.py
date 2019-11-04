from sklearn.datasets import load_breast_cancer
import pandas as pd
import collections as col
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from statistics import mean

##############################################################
#####   Breast Cancer Example from Muller and Guido   ########
##############################################################

def run():
    print("\n#####   Start CANCER   #####")
    print("#####   Reference: Muller, Guido, Chapter 2, pg.40\n")

    cancer = load_breast_cancer()

    print("Keys: {}".format(cancer.keys()))

    data = pd.DataFrame()

    #####   Analising Data   #####

    print("Analising Data...")

    n_samples = len(cancer["data"])
    n_features = len(cancer["data"][0])

    print("Number of samples = {}".format(n_samples))
    print("Number of features = {}".format(n_features))

    # print(cancer["data"][0:5])

    print("Featur names = {}".format(cancer["feature_names"]))
    feature_names = cancer["feature_names"]

    # WARNING: cancer["data"][:,i] is different from cancer["data"][:][i]
    # The first accesses a column, the second a row
    for i in range(n_features):
       data[feature_names[i].replace(" ","_")] = cancer["data"][:,i]

    # Toying around
    # print(data["mean_radius"])
    # print(type(cancer["data"]))
    # print(cancer["data"].shape)
    # print(cancer["data"][:,0])

    #####   Analysing targets   #####

    target = cancer["target"]

    # Get list containing unique values (and optionally counts of these values) using numpy function np.unique()
    target_unique = np.unique(target)
    target_unique, counts = np.unique(target, return_counts = True)
    all_targets = dict(zip(target_unique, counts))

    print("All targets {}".format(all_targets))

    #####   Fit modell   #####

    # print((data.shape))

    rs_max = 20
    n_neighbors_max = 39
    N_n_neighbors = (int) ((n_neighbors_max-1)/2)

    # Initialise 2D list
    score = [[0 for b in range(1,n_neighbors_max,2)] for a in range(rs_max)]

    # print(type(score))

    for rs in range(rs_max):
        X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=rs)

        # Ensure that there is no line break at the end of print
        # print("RS = {}: ".format(rs), end=" ")

        for i in range(N_n_neighbors):
            knn = KNeighborsClassifier(n_neighbors = 2*i+1)
            knn.fit(X_train, y_train)

            score[rs][i] = knn.score(X_test, y_test)

            # print("Score with n_neighbors = {} is: {}".format(2*i+1, score))
            # print("\t{0:.2f}".format(score[i]), end=" ")

    score_avg = [0] * N_n_neighbors

    # WARNING: Access 2D list is different from 2D array!
    for i in range(N_n_neighbors):
        score_avg[i] = mean(score[:][i])

    print("Average Score")

    # Format floating point number
    for i in range(N_n_neighbors):
        print("n_neighbors = {}: score = {:.2f}".format(2*i+1, score_avg[i]))

    plt.plot(range(1,n_neighbors_max,2), score_avg)
    plt.show()

    print("\n#####   End CANCER   #####\n")






















