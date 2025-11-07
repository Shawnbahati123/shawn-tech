import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Synthetic data generator (creates random noise images labeled as cash/no-cash)

def generate_synthetic_dataset(path, n_samples=200):
    os.makedirs(path, exist_ok=True)
    import PIL.Image as Image
    for i in range(n_samples):
        arr = (np.random.rand(224,224,3)*255).astype('uint8')
        img = Image.fromarray(arr)
        img.save(os.path.join(path, f'sample_{i}.png'))


def build_and_train(data_dir):
    # This is a toy example; replace with real dataset
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train = datagen.flow_from_directory(data_dir, target_size=(224,224), batch_size=8, subset='training')
    val = datagen.flow_from_directory(data_dir, target_size=(224,224), batch_size=8, subset='validation')

    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(224,224,3)),
        tf.keras.layers.Conv2D(16,3,activation='relu'),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(train, validation_data=val, epochs=2)
    model.save('cash_detector.h5')

if __name__ == '__main__':
    # create a small dataset structure
    base = 'synthetic_cash_dataset'
    os.makedirs(os.path.join(base,'cash'), exist_ok=True)
    os.makedirs(os.path.join(base,'no_cash'), exist_ok=True)
    # generate a few synthetic images
    generate_synthetic_dataset(os.path.join(base,'cash'), n_samples=20)
    generate_synthetic_dataset(os.path.join(base,'no_cash'), n_samples=20)
    build_and_train(base)
