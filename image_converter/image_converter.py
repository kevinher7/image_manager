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
            output_image_path = input_image_path.replace(".HEIC", f".{output_format}")
        else:
            output_image_path = f"{output_file}.{output_format}"
        
        temp_img.save(output_image_path)

        print(f"\n{input_file} was converted succesfully into {output_image_path}")

    else:
        print("This file format is not supported yet:(")
    
    return 0


def main():
    parser = argparse.ArgumentParser(description="Convert Image Formats")
    parser.add_argument("input_file", type=str, help="Name of Input Image")
    parser.add_argument("-o", "--output_file", type=str, help="Name of output image", default=None)
    parser.add_argument("-f", "--format", type=str, help="Format of Image after Conversion", default="png")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    convert_image(args.input_file, args.output_file, args.format)

    return 0

if __name__ == "__main__":
    main()
