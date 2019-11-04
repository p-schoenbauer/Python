import numpy as np
from keras import models
from keras import layers
from keras.datasets import reuters
from keras.utils import to_categorical
import matplotlib.pyplot as plt
import tensorflow as tf


(train_data,train_labels), (test_data, test_labels) = reuters.load_data(num_words = 10000)

word_index = reuters.get_word_index()
reverse_word_index = {value:key for (key,value) in word_index.items()}

K = 5;

decoded = [0] * K;
for i in range(K):
    decoded[i] = " ".join([(reverse_word_index[i-3] if i>=3 else "") for i in train_data[i]])
    print(decoded[i])

print(train_data.shape)
print(len(train_data[0]))

def vec_seq(seq, dim=10000):
    results = np.zeros((len(seq), dim))
    for i, s in enumerate( seq ):
        results[i,s] = 1;
    return results

trainL = to_categorical( train_labels )
trainD = vec_seq( train_data )
testL = to_categorical( test_labels )
testD = vec_seq( test_data )

model = models.Sequential()
model.add(layers.Dense(64, activation="relu", input_shape=(10000,)))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(46, activation="softmax"))

model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

trainLv = trainL[:1000]
trainLa = trainL[1000:]
trainDv = trainD[:1000]
trainDa = trainD[1000:]

history = model.fit(trainDa, trainLa, epochs=10, batch_size=512, validation_data=(trainDv, trainLv))

his = history.history
loss = his['loss']
vloss = his['val_loss']
epochs = range(1, len(loss) + 1)

testL = to_categorical( test_labels )
testD = vec_seq( test_data )

result = model.evaluate(testD, testL)

print(result)

plt.plot( epochs, loss, 'bo')
plt.plot( epochs, vloss, 'rx')

plt.show()

#### SAVE weights and JSON

model.save_weights( "C:\\_Data\\Python\\DeepLearning\\MyFirstDeepLearning\\data\\ReutersWeights.h5" )
jsonString = model.to_json()
file = open( "C:\\_Data\\Python\\DeepLearning\\MyFirstDeepLearning\\data\\ReutersJson.h5" , "w")
file.write( jsonString )
file.close()