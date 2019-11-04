import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import layers as lay
from keras import models
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import sys
import MyPlot.MyPlot as myPlot

train_dir = "D:\\_Data\\IMDB\\Train"
glove_dir = "D:\\_Data\\IMDB\\glove"
modelFile = "D:\\_Data\\IMDB\\models\\IMDBmodel1000LSTMnoDense2"

##########   Load Data   #############

labels = []
texts = []

for lab in ["neg","pos"]:
    dir = os.path.join(train_dir, lab)
    for file_name in os.listdir(dir):
        # UniCode can't decode certain characters found in the file. Ignore for now.
        file = open(os.path.join(dir,file_name), "r", errors="ignore")
        str = file.read()

        texts.append( str )
        file.close()
        labels.append( 0 if lab == "neg" else 1)

##########   Tokenize Data   #############

maxlen = 100        #Cut every review after maxlen words
Ntraining = 2000     #Train on Ntraining samples
Nval = 10000        #Validates on Mval samples
num_words = 10000   #Consider only the max_words most used words

tokenizer = Tokenizer(num_words = num_words)
tokenizer.fit_on_texts( texts )
sequences = tokenizer.texts_to_sequences( texts )

word_index = tokenizer.word_index
print("Found %s unique tokens." %len(word_index))

data = pad_sequences(sequences, maxlen = maxlen)

labels = np.asarray( labels )
print("Shape of data tensor: ", data.shape)
print("Shape of label tensor: ", labels.shape)


##########   Split into train and test data   #############

# Randomize first
indices = np.arange( data.shape[0] )
np.random.shuffle( indices )
data = data[ indices ]
labels = labels[ indices ]

data_train = data[:Ntraining]
labels_train = labels[:Ntraining]
data_val = data[Ntraining:Ntraining+Nval]
labels_val = labels[Ntraining:Ntraining+Nval]


##########   Paring the GloVe   #############

embeddings_index = {}
file = open (os.path.join(glove_dir, "glove.6B.100d.txt"), errors="ignore")
for line in file:
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray( values[1:], dtype="float32" )
        embeddings_index[word] = coefs
    except:
        print("Error!", sys.exc_info())
file.close()

print("Found %s word vectors" % len(embeddings_index))

###########   Embedding matrix   ###########

embedding_dim = 100

embedding_matrix = np.zeros( (num_words, embedding_dim))

for word, i in word_index.items():
    if i < num_words:
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector


############ Designing the model   ##########

model = models.Sequential()
model.add( lay.Embedding(num_words, embedding_dim, input_length=maxlen) )
model.add( lay.LSTM(32) )
#model.add( lay.Dense(32, activation="relu"))
model.add( lay.Dense(1, activation="sigmoid"))
model.summary()

model.layers[0].set_weights( [embedding_matrix] )
model.layers[0].trainable = False;

###########   Learning the model   ###########

model.compile( optimizer="rmsprop", loss="binary_crossentropy", metrics=["acc"])
history = model.fit( data_train, labels_train, epochs = 10, batch_size=128, validation_data=(data_val, labels_val))

try:
    model.save( modelFile )
except:
    print(sys.exc_info())

#########################################################
########  MyPlot  #########################################
#########################################################

myPlot.plotHistory( history )








