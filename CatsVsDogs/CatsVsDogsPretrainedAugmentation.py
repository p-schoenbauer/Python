from keras import models
from keras import layers
from keras.applications import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import matplotlib.pyplot as plt

##############   Files   ######################

trainDir = "D:\\_Data\\dogs-vs-cats\\train"
valDir = "D:\\_Data\\dogs-vs-cats\\val"

modelFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\modelPretrainedAugmentation.h5"

##############   Models   #####################

convBase = VGG16( weights = "imagenet", include_top = False, input_shape = (150,150,3))
convBase.trainable = False;

model = models.Sequential()
model.add( convBase )
model.add( layers.Flatten() )
model.add( layers.Dense( 256, activation="relu" ) )
model.add( layers.Dense( 1, activation = "sigmoid" ) )

trainDatagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

testDatagen = ImageDataGenerator(rescale=1./255)

trainGenerator = trainDatagen.flow_from_directory( trainDir, target_size=(150,150), batch_size=20, class_mode="binary" )
vGenerator = testDatagen.flow_from_directory( valDir, target_size=(150,150), batch_size=20, class_mode="binary" )

model.compile(loss="binary_crossentropy", optimizer=optimizers.RMSprop(lr=2e-5), metrics=["acc"])

history = model.fit_generator(
    trainGenerator,
    steps_per_epoch=80,
    epochs=20,
    validation_data=vGenerator,
    validation_steps=50 )

model.save( modelFile )


################   MyPlot   ###################

hist = history.history
acc = hist["acc"];
vAcc = hist["val_acc"];
loss = hist["loss"]
vLoss = hist["val_loss"]
epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, "bo")
plt.plot(epochs, vAcc, "o")

plt.figure()

plt.plot(epochs, loss, "go")
plt.plot(epochs, vLoss, "g")

plt.show()





