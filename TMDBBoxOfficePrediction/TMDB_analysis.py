import ast      #   Conversion of string to dict
import numpy as np
import pandas as pd
import datetime
import os
import time

"""
RESULTS OF ANALYSIS:

Keep only: "Id","belongs_to_collection","budget","genres","original_language","popularity","runtime","cast","production_countries","production_companies"
Maybe: "release_date" 
"""


def runAnalysis(data_train,data_test):
    print("\n################################")
    print("#####   RESTART ANALYSIS   #####")
    print("################################\n")

    n_samples = len(data_train["id"])

    print("Number of samples: {}".format(n_samples))

    header = data_train.columns.values

    print("Header: ", header)

    print("Preprocessing...")
    time_start_prep = time.time()

    ####   Preprocess Collections   ####
    # The function ast.literal_eval throws a "SyntaxError: unexpected EOF while parsing" if the ipnut is an empty string.

    collections = data_train["belongs_to_collection"]
    collections = preproc_collections(collections)
    collections_test = data_test["belongs_to_collection"]
    collections_test = preproc_collections(collections_test)

    collections_rmvNA = [c for c in collections if c != "NA"]
    collections_df = pd.DataFrame( collections_rmvNA )
    collections_df = collections_df[["id","name"]]

    collections = keep_only_id_collections(collections)
    collections_test = keep_only_id_collections(collections_test)

    ####   Preprocess Genres   ####

    genres = data_train["genres"]
    genres_test = preproc( data_test["genres"] )
    genres = preproc( genres )

    genres_all = [q for p in genres for q in p if p != "NA"]
    genres_df = pd.DataFrame(genres_all).drop_duplicates()


    print(genres_all)

    genres = keep_only_id_genres( genres )
    genres_test = keep_only_id_genres( genres_test )

    ####   Preprocess Language   ####

    lang = data_train["original_language"].copy()
    lang = lang.unique()

    ####   Preprocess production_companies   ####

    prod_comp = preproc(data_train["production_companies"])
    prod_comp_test = preproc(data_test["production_companies"])

    prod_comp_all = [q for p in prod_comp for q in p if p != "NA"]
    print(len(prod_comp_all))
    prod_comp_df = pd.DataFrame( prod_comp_all )

    prod_comp = keep_only_id_companies( prod_comp )
    prod_comp_test = keep_only_id_companies( prod_comp_test )


    ####   Preprocess production_countries   ####

    prod_countries = data_train["production_countries"]
    prod_countries_test = data_test["production_countries"]

    prod_countries = preproc(prod_countries)
    prod_countries_test = preproc(prod_countries_test)

    prod_countries_all = [q for p in prod_countries for q in p if p != "NA"]
    prod_countries_df = pd.DataFrame(prod_countries_all).drop_duplicates()

    prod_countries = keep_only_id_countries( prod_countries )
    prod_countries_test = keep_only_id_countries( prod_countries_test )

    ####   Preprocess Release Date   ####

    date = data_train["release_date"]
    date = [datetime.datetime.strptime(d, '%m/%d/%y') for d in date]

    ####   Preprocess cast   ####

    cast = data_train["cast"]
    cast_test = data_test["cast"]

    cast = preproc(cast)
    cast_test = preproc(cast_test)

    cast_all = [q for p in cast for q in p if p != "NA"]
    cast_df = pd.DataFrame(cast_all).drop_duplicates()
    cast_df = cast_df[["id","name"]]

    cast = keep_only_id_companies( cast )
    cast_test = keep_only_id_companies( cast_test )

    time_stop_prep = time.time()
    print("Preprocessing End. Time ={}".format(time_stop_prep - time_start_prep))

    #####################################
    ###### Save Preprocessed data   #####
    #####################################


    data_train_output = data_train[["id","belongs_to_collection","budget","genres","original_language","popularity","runtime","cast","revenue"]]
    data_test_output = data_test[["id","belongs_to_collection","budget","genres","original_language","popularity","runtime","cast"]]


    data_train_output["belongs_to_collection"] = collections
    data_train_output["genres"] = [str(g)[1:-1] for g in genres]
    data_train_output["production_countries"] = [str(g)[1:-1] for g in prod_countries]
    data_train_output["production_companies"] = [str(g)[1:-1] for g in prod_comp]
    data_train_output["cast"] = [str(g)[1:-1] for g in cast]

    data_test_output["belongs_to_collection"] = collections_test
    data_test_output["genres"] = [str(g)[1:-1] for g in genres_test]
    data_test_output["production_countries"] = [str(g)[1:-1] for g in prod_countries_test]
    data_test_output["production_companies"] = [str(g)[1:-1] for g in  prod_comp_test]
    data_test_output["cast"] = [str(g)[1:-1] for g in cast_test]


    dir = "C:\\_Data\\Python\\MachineLearning\\TMDBBoxOfficePrediction\\data"
    data_train_outputfile = os.path.join(dir,"train_preproc2.csv")
    data_test_outputfile = os.path.join(dir,"test_preproc2.csv")
    data_target_outputfile = os.path.join(dir,"target.csv")

    write = True;
    if os.path.isfile(data_train_outputfile):
        print("File {} exists. Overwrite?".format(data_train_outputfile))
        ans = input()
        if ans == "y" or ans == "Y":
            os.remove( data_train_outputfile )
        else:
            write=False

    if write:
        data_train_output.to_csv(data_train_outputfile, index=False)

    write = True;
    if os.path.isfile(data_test_outputfile):
        print("File {} exists. Overwrite?".format(data_test_outputfile))
        ans = input()
        if ans == "y" or ans == "Y":
            os.remove( data_test_outputfile )
        else:
            write=False

    if write:
        data_test_output.to_csv(data_test_outputfile, index=False)









    print("\n################################")



def preproc_collections(collections):
    # Default values are numpy NaN - only keep strings
    # Remove square brackets at beginning and end
    collections = [c[1:-1] if isinstance(c, str) else "NA" for c in collections ]
    collections = [ast.literal_eval(c) if c != "NA" else "NA" for c in collections]
    return collections

def keep_only_id_collections(collections):
    collections = [c.get("id") if c != "NA" else "NA" for c in collections]
    return collections

def keep_only_id_genres(genres):
    genres = [[h.get("id") for h in g] if g != "NA" else "NA" for g in genres]
    return genres

def preproc(prod_comp):
    prod_comp = [p[1:-1] if isinstance(p,str) else "NA" for p in prod_comp ]
    prod_comp = [p.split("}") if p != "NA" else "NA" for p in prod_comp]
    prod_comp = [ [q if q[0]=="{" else q[2:] for q in p if len(q)>0] if p != "NA"  else "NA" for p in prod_comp]
    prod_comp = [ [q if q[-1]=="}" else q+"}" for q in p if len(q)>0] if p != "NA"  else "NA" for p in prod_comp]
    prod_comp = [[ast.literal_eval(q) for q in p] if p != "NA"  else "NA" for p in prod_comp]
    return prod_comp

def keep_only_id_companies(prod_comp):
    return [[h.get("id") for h in g] if g != "NA" else "NA" for g in prod_comp]

def keep_only_id_countries(prod_countries):
    return [[h.get("iso_3166_1") for h in g] if g != "NA" else "NA" for g in prod_countries]

