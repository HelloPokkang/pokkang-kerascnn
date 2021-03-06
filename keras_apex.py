from __future__ import print_function
# import keras
# from time import time
#
# from PIL import Image
# from keras import metrics, Model
# from keras.applications import VGG16
# from keras.callbacks import TensorBoard
from keras.models import Sequential
from keras.layers import Activation, Dense, Dropout, Flatten, ZeroPadding2D, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import datetime
import numpy as np
batch_size = 32
num_classes = 8
epochs = 200
folder = 'leaves_flavia_oriented_800_600/'

input_shape = (200, 400, 3)


model = Sequential([
    Conv2D(32, (3, 3), input_shape=input_shape, padding='same',
           activation='relu'),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    Conv2D(64, (3, 3), activation='relu', padding='same', ),
    Conv2D(64, (3, 3), activation='relu', padding='same', ),
    MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    Conv2D(128, (3, 3), activation='relu', padding='same', ),
    Conv2D(128, (3, 3), activation='relu', padding='same', ),
    MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    Conv2D(256, (3, 3), activation='relu', padding='same', ),
    Conv2D(256, (3, 3), activation='relu', padding='same', ),
    MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    Conv2D(512, (3, 3), activation='relu', padding='same', ),
    Conv2D(512, (3, 3), activation='relu', padding='same', ),
    MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(num_classes, activation='softmax')
])


# base_model = VGG16(include_top=False,weights='imagenet',input_shape=input_shape)
#
# for layer in base_model.layers:
#     layer.trainable = False
#
# x = base_model.output
# x = Flatten(input_shape=base_model.output_shape[1:])(x)
# x = Dense(512,activation='relu')(x)
# x = Dense(num_classes,activation='softmax')(x)
#
# model = Model(inputs=base_model.input,outputs=x)

sgd = SGD(lr=0.0001,momentum=0.9)
model.compile(loss = "categorical_crossentropy", optimizer =sgd,metrics=['accuracy'])
model.summary()
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30
)

#image = Image.open('leaves_data/full/1/1001.jpg')
#arr = np.asarray(image)
#arr = arr.reshape((1,) + arr.shape)
#i = 0

train_generator = train_datagen.flow_from_directory(folder+'apex/train',
                                                    target_size=(200, 400),
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    )
test_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30
)
validation_generator = test_datagen.flow_from_directory(folder+'apex/test',
                                                        target_size=(200, 400),
                                                        class_mode='categorical')



model_name = "keras_base_1.h5"
model.fit_generator(
    train_generator,
    steps_per_epoch=1514//batch_size,
    epochs=150,
    validation_data=validation_generator,
    validation_steps=393//batch_size,
)
model.save(model_name)
