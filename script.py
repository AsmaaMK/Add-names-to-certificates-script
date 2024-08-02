import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from arabic_reshaper import ArabicReshaper

# Configuration for reshaping Arabic text
configuration = {
    'delete_harakat': False,
    'use_unshaped_instead_of_isolated': True,
}
reshaper = ArabicReshaper(configuration=configuration)

# Read the CSV file containing names and places
names_file = pd.read_csv('names/names.csv')
names = names_file['اسمك'].tolist()
places = names_file['المركز'].tolist()

# Paths to certificate images
certificatesImages = [
    './png-certificates/pass.png',
    './png-certificates/1.png',
    './png-certificates/2.png',
    './png-certificates/3.png',
]

# Colors and font settings
GOLD = '#ab802c'
RED = '#cf403a'
FONT = './fonts/Changa.ttf'

def print_pass_certificate(name, index):
    img = Image.open(certificatesImages[0])
    image_editable = ImageDraw.Draw(img)
    # Reshape and apply bidi algorithm for correct Arabic display
    text = reshaper.reshape(name)
    font = ImageFont.truetype(FONT, 60)
    poss = (250, 300)
    image_editable.text(poss, text, font=font, fill=RED)
    img.save("./output/pass/" + str(index) + "_" + name + ".png")

def print_place_certificate(place, name):
    img = Image.open(certificatesImages[place])
    image_editable = ImageDraw.Draw(img)
    # Reshape and apply bidi algorithm for correct Arabic display
    text = reshaper.reshape(name)
    font = ImageFont.truetype(FONT, 110)
    poss = (500, 1070)
    image_editable.text(poss, text, font=font, fill=GOLD)
    img.save("./output/" + str(place) + "/" + name + ".png")

# Generate certificates for each name and place
for index, name in enumerate(names):
    place = places[index]
    if place > 3:
        print_pass_certificate(name, index)
    else:
        print_place_certificate(place, name)