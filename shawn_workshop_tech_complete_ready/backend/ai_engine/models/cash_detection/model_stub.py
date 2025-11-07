# TensorFlow cash detection model stub
# Replace with real TF model training and inference code
import tensorflow as tf

def build_model():
    # simple placeholder CNN
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=(224,224,3)),
        tf.keras.layers.Conv2D(16,3,activation='relu'),
        tf.keras.layers.MaxPool2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def infer(image_array):
    model = build_model()
    # placeholder: return random prediction
    return {"cash_present": True, "confidence": 0.92}
