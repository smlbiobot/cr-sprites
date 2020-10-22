#!/usr/bin/env python3

import json
import os

import PIL
from PIL import Image

# Animated GIF
OUT_FOLDER = os.path.join(".", "out-gif")
with open("./config.json") as f:
    config = json.load(f)
SC_FOLDER = os.path.join(*config['sc_folder']['paths'])

for root, dirs, files in os.walk(SC_FOLDER):
    for dir_name in dirs:
        folder = os.path.join(SC_FOLDER, dir_name)
        files = [
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))]
        file_paths = [
            os.path.join(folder, f) for f in files]

        # images = [
        #     Image.open(f) for f in file_paths]

        images = []
        for f in file_paths:
            try:
                image = Image.open(f)
            except PIL.Image.DecompressionBombError:
                continue
            else:
                images.append(image)

        out_file = os.path.join(OUT_FOLDER, "{}.gif".format(dir_name))
        if images:
            image = images[0]
            image.save(
                out_file, save_all=True, append_images=images[1:], duration=4, loop=0)
            print(out_file)
