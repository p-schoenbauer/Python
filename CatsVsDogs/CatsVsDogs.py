from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

trainDir = "D:\\_Data\\dogs-vs-cats\\train"
valDir = "D:\\_Data\\dogs-vs-cats\\val"

modelFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\model2.h5"

#########################################################
########  Data preprocessing  ###########################
#########################################################

trainDatagen = ImageDataGenerator(
    rescale = 1./255,
    rotation_range = 40,
    width_shift_range = 0.2,
    height_shift_range= 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True )
valDatagen = ImageDataGenerator(rescale = 1./255)

trainGen = trainDatagen.flow_from_directory(
    trainDir,
    target_size = (150,150),
    batch_size = 20,
    class_mode = "binary" )

valGen = valDatagen.flow_from_directory(
    valDir,
    target_size = (150,150),
    batch_size = 20,
    class_mode = "binary" )

#########################################################
########  Model definition  #############################
#########################################################

model = models.Sequential()
model.add( layers.Conv2D( 32, (3, 3), activation = "relu", input_shape = (150,150,3) ) )
model.add( layers.MaxPooling2D( (2, 2) ) )
model.add( layers.Conv2D( 64, (3, 3), activation = "relu" ) )
model.add( layers.MaxPooling2D( (2, 2) ) )
model.add( layers.Conv2D( 128, (3, 3), activation = "relu" ) )
model.add( layers.MaxPooling2D( (2, 2) ) )
model.add( layers.Conv2D( 128, (3, 3), activation = "relu" ) )
model.add( layers.MaxPooling2D( (2, 2) ) )
model.add( layers.Flatten() )
model.add( layers.Dropout( 0.5 ) )
model.add( layers.Dense(512, activation = "relu" ) )
model.add( layers.Dense(1, activation = "sigmoid" ) )

model.summary()

model.compile( loss = "binary_crossentropy", optimizer = optimizers.RMSprop(lr=1e-4), metrics=["acc"] )

for data, labels in trainGen:
    print(data.shape)
    print(labels.shape)
    print(labels)
    break

#########################################################
########  Model fit  ####################################
#########################################################

history = model.fit_generator(
    trainGen,
    steps_per_epoch = 100,
    epochs = 20,
    validation_data=valGen,
    validation_steps=50)

model.save( modelFile )

#########################################################
########  MyPlot  #########################################
#########################################################

hist = history.history
acc = hist["acc"]
val_acc = hist["val_acc"]
loss = hist["loss"]
val_loss = hist["val_loss"]

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, "bo", label="Training acc")
plt.plot(epochs, val_acc, "b", label="Validation acc")

plt.figure()

plt.plot( epochs, loss, "bo", label="Training loss")
plt.plot( epochs, val_loss, "b", label="Validation loss")

plt.show()