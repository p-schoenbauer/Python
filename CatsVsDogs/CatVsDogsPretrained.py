from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras.applications import VGG16
import os
import numpy as np

#########################################################
########  Load pre-trained model  #######################
#########################################################

conv_base = VGG16( weights = "imagenet", include_top = False, input_shape = (150,150,3))
conv_base.summary()

#########################################################
########  Define Files   ################################
#########################################################

trainDir = "D:\\_Data\\dogs-vs-cats\\train"
testDir = "D:\\_Data\\dogs-vs-cats\\test"
valDir = "D:\\_Data\\dogs-vs-cats\\val"

modelFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\modelPretrained.h5"

#########################################################
########  Extract Features from pre-trained model  ######
#########################################################

datagen = ImageDataGenerator(rescale = 1./255)
batch_size = 20

def extract_features(dir, sN):
    features = np.zeros((sN, 4, 4, 512))
    labels = np.zeros(sN)
    generator = datagen.flow_from_directory(
        dir,
        target_size=(150,150),
        batch_size=batch_size,
        class_mode="binary"
    )
    for i in range(int(sN / batch_size)):
        inputs_batch, labels_batch = generator.next()
        features_batch = conv_base.predict( inputs_batch )
        features[i * batch_size : (i+1) * batch_size] = features_batch
        labels[i * batch_size : (i+1) * batch_size] = labels_batch
    return features, labels

trainFeatures, trainLabels = extract_features(trainDir, 2000)
valFeatures, valLabels = extract_features(valDir, 1000)
testFeatures, testLabels = extract_features(testDir, 1000)

#########################################################
########  Run own model  ################################
#########################################################

trainFeatures = np.reshape(trainFeatures, (2000,4*4*512))
valFeatures = np.reshape(valFeatures, (1000,4*4*512))
testFeatures = np.reshape(testFeatures, (1000,4*4*512))

model = models.Sequential()
model.add( layers.Dense( 256, activation="relu", input_dim=4*4*512 ) )
model.add( layers.Dropout(0,5))
model.add( layers.Dense( 1, activation = "sigmoid" ) )

model.compile(optimizer = optimizers.RMSprop(lr=2e-5) , loss = "binary_crossentropy", metrics=["acc"])
history = model.fit( trainFeatures, trainLabels, epochs=30, batch_size=20, validation_data=(valFeatures,valLabels))

model.save( modelFile )

#########################################################
########  MyPlot   ########################################
#########################################################

hist = history.history
loss = hist["loss"]
vLoss = hist["val_loss"]
acc = hist["acc"]
vAcc = hist["val_acc"]

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, "bo")
plt.plot(epochs, vLoss, "b")

plt.figure()

plt.plot(epochs, acc, "go")
plt.plot(epochs, vAcc, "g")

plt.show()





























