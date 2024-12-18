import os
import argparse

from PIL import Image
from pillow_heif import register_heif_opener

from ..utils import get_image_path_from_name

def convert_image(input_file, output_file=None, output_format="png"):
    input_image_path = get_image_path_from_name(input_file)

    file_extension = input_image_path.split(".")[-1].lower()

    if file_extension == "heic":
        register_heif_opener()
        temp_img = Image.open(input_image_path)
        output_image_path = ""

        if output_file == None:
            output_image_path = input_image_path.replace(".HEIC", f".{output_format.lower()}")
        else:
            output_image_path = f"{input_image_path.split('.', 1)[0]}.{output_format}"

        temp_img.save(output_image_path)

    else:
        print("This file format is not supported yet:(")
    
    return 0


def main():
    print(convert_image("IMG_1815"))

if __name__ == "__main__":
    main()
