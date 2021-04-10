import keras
from keras.preprocessing import image
import numpy as np


network = keras.models.load_model("C:\\Users\\t659699\\Tools\\PortableGit\\repo\\Cat_Or_Not\\CNN\\my_catdog_model")

def predict_image():

    network.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    import_image_dir = 'C:\\Users\\t659699\\Tools\\PortableGit\\repo\\Cat_Or_Not\\cats\\statics\\cat_dog.jpg'
    test_image = image.load_img(import_image_dir, target_size=(150, 150))
    test_image_array = image.img_to_array(test_image)
    test_image_array = np.expand_dims(test_image_array, axis=0)

    predicted = network.predict(test_image_array)
    print(predicted)
    return int(predicted[0][0])




