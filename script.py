import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

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
    './png-certificates/0.jpeg',
    './png-certificates/1.jpeg',
    './png-certificates/2.jpeg',
    './png-certificates/3.jpeg',
]

# Colors and font settings
# GOLD = '#ab802c'
GOLD = '#000'
RED = '#cf403a'
FONT = './fonts/Changa.ttf'

def print_certificate(place, name):
    img = Image.open(certificatesImages[place])
    image_editable = ImageDraw.Draw(img)
    # Reshape and apply bidi algorithm for correct Arabic display
    text = reshaper.reshape(name)
    text_to_display = get_display(text)
    font = ImageFont.truetype(FONT, 50)
    # Calculate the bounding box of the text
    bbox = image_editable.textbbox((0, 0), text_to_display, font=font)
    text_width = bbox[2] - bbox[0]
    # Calculate x-coordinate to center the text
    poss = ((img.width - text_width) / 2, 670)
    image_editable.text(poss, text, font=font, fill=GOLD)
    img.save("./output/" + str(place) + "/" + name + ".png")

# Generate certificates for each name and place
for index, name in enumerate(names):
    place = places[index]
    if place > 3:
        print_certificate(0, name)
    else:
        print_certificate(place, name)