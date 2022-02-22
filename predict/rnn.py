from tensorflow.keras import optimizers, layers, models
import numpy as np
import matplotlib.pyplot as plt


class DNN(models.Sequential):
    def __init__(self, layer_size):
        super().__init__()
        self.add(layers.LSTM(10, activation='relu', input_shape=(82, 200)))
        self.add(layers.Dense(5))
        self.add(layers.Dense(1))
        self.add(layers.Dense(1, activation='sigmoid'))
        optimizer = optimizers.Nadam(learning_rate=0.0000005)
        self.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])


if __name__ == '__main__':
    si = 16400
    fr = 1

    model = DNN(si)
    print('Load Model Done!')
    train = np.loadtxt("dataset/simple/train.csv", delimiter=',', dtype=np.float32)
    test = np.loadtxt("dataset/simple/test.csv", delimiter=',', dtype=np.float32)
    print('Load Dataset Done!')
    train_data = train[:, fr:]
    train_label = train[:, 0]
    train_label = train_label / 4 - 0.25
    train_label = np.around(train_label)
    train_label = train_label.reshape(-1, 1)
    train_data = train_data.reshape(-1, 82, 200)

    test_data = train[:, fr:]
    test_label = train[:, 0]
    test_label = train_label / 4 - 0.25
    test_label = np.around(train_label)
    test_label = train_label.reshape(-1, 1)
    test_data = test_data.reshape(-1, 82, 200)
    results = model.fit(train_data, train_label, epochs=200, batch_size=32, validation_split=0.2)

    plt.plot(results.history['accuracy'])
    plt.plot(results.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(results.history['loss'])
    plt.plot(results.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    plt.show()

    test_loss, test_acc = model.evaluate(test_data, test_label)
    print('test_acc: ', test_acc)
