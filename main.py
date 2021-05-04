import base64

import tf as tf

from enhance import toImage


def img2base64(img):
    with open(img, "rb") as img_file:
        # convert to base64
        base64_str = base64.b64encode(img_file.read())
        new_img = toImage(base64_str)
        return new_img


def newImg(new_img):
    img_data = base64.b64decode(new_img)
    with open("Image/new_img.png", "wb") as f:
        f.write(img_data)


def covertImg2base64(img):
    with open(img, "rb") as img_file:
        # convert to base64
        base64_str = base64.b64encode(img_file.read()).decode()
        print(type(base64_str))
    file = open("test.txt", "w").write(base64_str)


# covertImg2base64("Image/main.jpg")

# from enhance import toImage
#
# file = open("test.txt", "r").read()
# toImage(file)
# print("hello")



# import tensorflow as tf
# c = tf.constant()