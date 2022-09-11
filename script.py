import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

configuration = {
    'delete_harakat': False,
    'use_unshaped_instead_of_isolated': True,
}
reshaper = ArabicReshaper(configuration=configuration)

names_file = pd.read_csv('names/names.csv')
names = names_file['الاسم ثلاثي'].tolist()
places = names_file['المركز'].tolist()

certificatesImages = [
    './png-certificates/pass.png',
    './png-certificates/first-place.png',
    './png-certificates/second-place.png',
    './png-certificates/third-place.png',
]


GOLD = '#ab802c'
RED = '#cf403a'

FONT = './fonts/Changa.ttf'


def print_pass_certificate(name):
    img = Image.open(certificatesImages[0])
    image_editable = ImageDraw.Draw(img)
    text = reshaper.reshape(name)
    text_to_display = get_display(text)
    font = ImageFont.truetype(FONT, 60)
    poss = (250, 300)
    image_editable.text(poss, text_to_display, font=font, fill=RED)
    img.save("./output/pass/" + name + ".png")


def print_place_certificate(place, name):
    img = Image.open(certificatesImages[place])
    image_editable = ImageDraw.Draw(img)
    text = reshaper.reshape(name)
    text_to_display = get_display(text)
    font = ImageFont.truetype(FONT, 110)
    poss = (500, 1200)
    image_editable.text(poss, text_to_display, font=font, fill=GOLD, direction='rtl')
    img.save("./output/" + str(place) + "/" + name + ".png")


for index, name in enumerate(names):
    if index == 0:
        if places[index] > 0 and places[index] < 4:
            print_place_certificate(places[index], name)

        print_pass_certificate(name)
