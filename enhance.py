import base64
import io as StringIO
import imageio
from PIL import Image
import numpy as np
import tensorflow as tf


from models import resnet
import utils





def leave():
    pass


high = 0
width = 0

IMAGE_HEIGHT = 0
IMAGE_WIDTH = 0
IMAGE_SIZE = 0


def toImage(strImg):
    global high, width, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_SIZE

    image = Image.open(StringIO.BytesIO(
        base64.b64decode(strImg)))

    tf.compat.v1.disable_v2_behavior()
    phone = "iphone_orig"
    resolution = "orig"
    use_gpu = "true"

    config = tf.compat.v1.ConfigProto(device_count={'GPU': 0}) if use_gpu == "false" else None

    with tf.compat.v1.Session(config=config) as sess:

        high, width = image.size

        res_sizes = {
            "iphone_orig": [width, high]
        }

        IMAGE_HEIGHT = res_sizes[phone][0]
        IMAGE_WIDTH = res_sizes[phone][1]
        IMAGE_SIZE = IMAGE_HEIGHT * IMAGE_WIDTH * 3

        # create placeholders for input images
        x_ = tf.compat.v1.placeholder(tf.float32, [None, IMAGE_SIZE])
        x_image = tf.reshape(x_, [-1, IMAGE_HEIGHT, IMAGE_WIDTH, 3])
        # generate enhanced image
        enhanced = resnet(x_image)

        saver = tf.compat.v1.train.Saver()
        saver.restore(sess, "models_orig/" + phone)


        image = np.float16(np.array(image)) / 255

        image_crop = utils.extract_crop(image, resolution, phone, res_sizes)
        image_crop_2d = np.reshape(image_crop, [1, IMAGE_SIZE])

        enhanced_2d = sess.run(enhanced, feed_dict={x_: image_crop_2d})
        enhanced_image = np.reshape(enhanced_2d, [IMAGE_HEIGHT, IMAGE_WIDTH, 3])

        imageio.imwrite("Image/enhanced.png", enhanced_image)

        toBase64 = open("Image/enhanced.png", "rb")
        toBase64 = base64.b64encode(toBase64.read())

        saver = tf.compat.v1.train.remove_checkpoint


        return toBase64
