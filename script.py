import pandas as pd
from PIL import Image, ImageFont, ImageDraw
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

configuration = {
    'delete_harakat': False,
    'use_unshaped_instead_of_isolated': True,
}
reshaper = ArabicReshaper(configuration=configuration)

names_file = pd.read_csv('names.csv')
names = names_file['الاسم ثلاثي'].tolist()

for index, name in enumerate(names):
    # if index == 0:
        print(name)
        img = Image.open("img.png")
        text = reshaper.reshape(name)
        image_editable = ImageDraw.Draw(img)
        title_font = ImageFont.truetype('Changa.ttf', 60)
        text_to_display = get_display(text)
        image_editable.text((250, 300), text_to_display,
                            font=title_font, fill='#cf403a')
        img.save("./output/" + str(index) + '- ' + name + ".png")
