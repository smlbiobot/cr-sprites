#!/usr/bin/env python3

import json
import os

import PIL
from PIL import Image

# Stacked image composite
OUT_FOLDER = os.path.join(".", "out-stack")
with open("./config.json") as f:
    config = json.load(f)
SC_FOLDER = os.path.join(*config['sc_folder']['paths'])

for root, dirs, files in os.walk(SC_FOLDER):
    for dir_name in dirs:
        if dir_name.startswith('_'):
            continue
        folder = os.path.join(SC_FOLDER, dir_name)
        files = [
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))]
        file_paths = [
            os.path.join(folder, f) for f in files]

        image = None
        for i, file_path in enumerate(file_paths):
            try:
                img = Image.open(file_path)
                if i == 0:
                    image = img
                else:
                    if img and image:
                        image = Image.alpha_composite(img, image)

            except PIL.Image.DecompressionBombError:
                pass

        out_file = os.path.join(OUT_FOLDER, "{}.png".format(dir_name))
        if image:
            image.save(out_file)
            print(out_file)
