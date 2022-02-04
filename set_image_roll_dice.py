import random
from PyQt5.QtGui import QPixmap


def set_image_roll_dice_to_label(label):
    name_img = f'{random.randint(1, 6)}.jpg'

    img = QPixmap(name_img)
    img = img.scaled(380, 380)
    label.setPixmap(img)
