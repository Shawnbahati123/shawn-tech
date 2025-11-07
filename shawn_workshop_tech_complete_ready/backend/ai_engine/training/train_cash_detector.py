import tensorflow as tf, os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

DATA_DIR = 'backend/ai_engine/training/synthetic'

def build_model():
    model = models.Sequential([
        layers.InputLayer(input_shape=(224,224,3)),
        layers.Conv2D(16,3,activation='relu'),
        layers.MaxPool2D(),
        layers.Conv2D(32,3,activation='relu'),
        layers.MaxPool2D(),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train():
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_gen = datagen.flow_from_directory(DATA_DIR, target_size=(224,224), batch_size=8, subset='training')
    val_gen = datagen.flow_from_directory(DATA_DIR, target_size=(224,224), batch_size=8, subset='validation')
    model = build_model()
    model.fit(train_gen, validation_data=val_gen, epochs=3)
    model.save('backend/ai_engine/models/cash_detection/tf_cash_model.h5')
    print('Model trained and saved.')

if __name__ == '__main__':
    train()
