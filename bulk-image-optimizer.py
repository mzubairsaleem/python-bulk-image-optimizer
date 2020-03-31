import os
import subprocess
from pathlib import Path
from PIL import Image

CONVERT_PNG_TO_JPG = False


def compress(location):
    for r, d, f in os.walk(location):
        for item in d:
            compress(location + os.sep + item)

        for image in f:
            path = location
            input_path = path + os.sep + image
            out_path = path.replace(r'input', r'output')
            if image.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                if os.path.isfile(input_path):
                    opt = Image.open(input_path)
                    print(input_path)
                    print(opt.size)
                    Path(out_path).mkdir(parents=True, exist_ok=True)
                    out_path = out_path + os.sep + image
                    # Convert .pgn to .jpg
                    if CONVERT_PNG_TO_JPG and image.lower().endswith('.png'):
                        im = opt
                        rgb_im = im.convert('RGB')
                        out_path = out_path.replace(".png", ".jpg")
                        rgb_im.save(out_path)
                        opt = Image.open(out_path)
                    opt.save(out_path, optimize=True, quality=90)
                    opt = Image.open(out_path)
                    print(opt.size)
            else:
                if os.path.isfile(input_path):
                    print('File not image, copying instead: ' + input_path)
                    subprocess.call('cp ' + input_path + ' ' + out_path, shell=True)


if __name__ == '__main__':
    start_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + r"input"
    # ask if .pgn images should automatically converted to .jpg
    CONVERT_PNG_TO_JPG = input('Would you like to convert .png images to .jpg? (y/n): ') == 'y'
    compress(start_path)
