import tensorflow as tf
import numpy as np

# %%

(train_data, train_label), (test_data, test_label) = tf.keras.datasets.cifar100.load_data()

# %%

train_data = np.reshape(train_data, [50000, 32, 32, 3])
test_data = np.reshape(test_data, [10000, 32, 32, 3])

# %%

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=16, kernel_size=[3, 3], padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D(pool_size=[2, 2], padding='same'),
    tf.keras.layers.Conv2D(filters=32, kernel_size=[3, 3], padding='same'),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.MaxPooling2D(pool_size=[2, 2], padding='same'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(100),
    tf.keras.layers.Activation('softmax')
])

# %%

optimizer = tf.keras.optimizers.Adam(lr=0.0001)

model.compile(
    optimizer=optimizer,
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# %%

train_label_onehot = tf.keras.utils.to_categorical(train_label)
test_label_onehot = tf.keras.utils.to_categorical(test_label)

# %%

train_data = train_data.astype('float32')

model.fit(
    train_data, train_label_onehot, epochs=50
)

# %%

predicted = model.predict(train_data)

# %%

predicted_class = np.argmax(predicted, axis=1)

evaluate = (predicted_class == train_label)
num_correct = np.sum(evaluate)
