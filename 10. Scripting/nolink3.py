#!/bin/env python3
import requests
import pytesseract
import shutil
from PIL import Image

BASE_URL = "http://35.196.167.142:8083/article/"

# I just kept updating the below two numbers with hand-corrected values when OCR failed.
uuid = "f30fbc03-54a5-4dd4-828a-e10e673698f8"
img_count = 95

filename = f"pics2/{img_count}_{uuid}.png"

while True:
    res = requests.get(BASE_URL + uuid, stream=True)
    
    if res.headers['content-type'] == 'image/png':
        res.raw.decode_content = True

        with open(filename, 'wb') as f:
            shutil.copyfileobj(res.raw, f)

        uuid = pytesseract.image_to_string(Image.open(filename), config="--psm 7 tconf")
        uuid = uuid.strip().replace('@', '0').replace(" ", "").replace("£", "f").replace('G', '0').replace('O', '0').replace('F', 'f').replace('l', '1').replace('C', 'c').replace('¢', 'c').replace('©', 'c')
        img_count += 1
        filename = f"pics2/{img_count}_{uuid}.png"

        print(uuid)
    else:
        print(res.text)
        break