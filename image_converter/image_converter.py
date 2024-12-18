import argparse

from ..utils import get_image_path_from_name

def convert_image(input_file, output_file=None):
    return get_image_path_from_name(input_file)

def main():
    print(convert_image("IMG_1815"))

if __name__ == "__main__":
    main()
