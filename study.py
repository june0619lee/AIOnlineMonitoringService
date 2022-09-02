from operator import index
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# model load

model = load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# image read
image = Image.open('poodle.jpg')
image = ImageOps.fit(image, (224, 224), Image.ANTIALIAS)

# convert to np.ndarray type
image_array = np.asarray(image)

if image_array.shape[2] > 3:
    image_array = image_array[:, :, :3]

normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

# run inference
prediction = model.predict(data)
print(prediction)

index2category = {
    0: 'pome' ,
    1: 'jindo' ,
}

for i, prob in enumerate(prediction[0].tolist()):
    print(index2category[i], '{:,4f}'.format(prob))