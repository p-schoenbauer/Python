from keras import models

modelFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\model2.h5"
weightFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\weight2.h5"
jsonFile = "C:\\_Data\\Python\\DeepLearning\\CatsVsDogs\\data\\json2.h5"

model = models.load_model( modelFile )

model.save_weights( weightFile )
jsonString = model.to_json()
file = open(jsonFile, "w")
file.write( jsonString )
file.close()