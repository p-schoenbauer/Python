from sklearn.datasets import load_iris
import pandas as pd
import collections as col
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#####################################################
#####   IRIS example from MullerGuido   #############
#####################################################

### Prediction using KNeighbors from sklearn ###

def run():
    print("#####   Start IRIS   #####")
    print("#####   Reference: Muller, Guido, Chapter 1, pg.20")

    # Load data
    iris = load_iris()

    # print the keys
    print("Keys = {}".format(iris.keys()))
        # KEYS = ['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'

    # Number of Samples
    n_samples = len(iris["data"])
    print("Number of Samples: {}".format(n_samples))

    # Create DataFrame "data" to store X and y

    data = pd.DataFrame()


    ##### Analysis 'data' #####

    print("Analising 'data'...")
    #print(data[0:5])
    #print(type(data))
    #print(type(data[0]))

    feature_names = iris["feature_names"]

    print("Feature_names {}".format(feature_names))
    print("Creating a column for each feature in DataFrame 'data'")

    # Introduce simplified names for features
    f_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

    # Create a column for each feature
    for i in range(4):
        data[f_names[i]] = [d[i] for d in iris["data"]]

    ##### Analysis 'Target' #####

    print("Analising 'target'...")

    #print(type(iris["target"]))
    #print(type(iris["target"][0]))
    #print(iris["target"][0:5])

    # Create list of all possible targets
    target_all = [t for t in iris["target"]]
    target_unique_df = pd.DataFrame(target_all).drop_duplicates()
    target_unique = target_unique_df[0].to_numpy()
    print("List of all targets: {}".format(target_unique))

    # Count occurances of all targets
    target_counter = col.Counter(target_all)
    print("Target occurances: {}".format(target_counter.most_common()))

    print("There are 50 sample for each of the 3 targets")

    data["target"] = iris["target"]

    # --- Toying aroung

    # print(type(data["target"]))
    # print(type(data["target"].to_numpy()))
    # print(type(iris["target"]))

    # target_all_pd = [t for t in data["target"]]

    # print(type(target_all))
    # print(type(target_all_pd))

    # --- Toying over

    ##### Scatter plot #####

    print("Creating Scatter Plot...")

    # plt.scatter(data["sepal_length"], data["sepal_width"], c=data["target"])

    fig, ax = plt.subplots(3,3)

    for i in range(3):
        for j in range(3):
            ax[i,j].scatter(data[f_names[j]],data[f_names[i+1]], c=data["target"])
            if i == 2:
                ax[i,j].set_xlabel(feature_names[j])
            if j == 0:
                ax[i,j].set_ylabel(feature_names[i+1])
            if j>i:
                ax[i,j].set_visible(False)

    # plt.show()

    ##### Train-Test split #####

    print("Fitting the Model: KNeighbors")

    # Redue data to petal_width and petal_lengt. Clear from scatter plot that sepal dimensions are irrelevant
    X = data[["petal_width","petal_length"]]

    # Create a Train-Test split (75/25)
    X_train, X_test, y_train, y_test = train_test_split(X, iris["target"], random_state=0)

    # Try differnt number of Neighbors
    score = 0
    for i in range(5):
        knn = KNeighborsClassifier(n_neighbors=2*i + 1)
        knn.fit(X_train,y_train)

        score = knn.score(X_test, y_test)
        print("Score for kNeighbors={} is {}".format(2*i+1,score))

    print("There are {} instances in the test set. The score {} means that {} have (has) been missclassified.".format(len(X_test), score, int(round(len(X_test)*(1-score)))) )

    # Try different random seeds
    for rs in range(5):
        X_train, X_test, y_train, y_test = train_test_split(X, iris["target"], random_state=rs)
        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X_train,y_train)

        print("Score for Randomstate={} is {}".format(rs,knn.score(X_test, y_test)))


    print("#####   FINISHED   #####\n")

















