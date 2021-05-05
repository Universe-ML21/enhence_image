import base64

from enhance import toImage


def img2base64(img):
    with open(img, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read())
        new_img = toImage(base64_str)
        return new_img


img2base64("Image/main.jpg")
img2base64("Image/main.jpg")
