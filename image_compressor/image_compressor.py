import argparse
from PIL import Image

from ..utils import get_image_path_from_name


def compress_image(input_file, downscale_factor=2, output_file=None, quality=1, file_format="png"):
    if quality == 1:
        resampling = Image.Resampling.LANCZOS
    elif quality == 0:
        resampling = Image.Resampling.NEAREST
    else:
        raise ValueError(
            "Invalid quality argument. It only accepts 0 (for fastest) and 1 (for highest quality))")

    input_image_path = get_image_path_from_name(input_file, file_format)

    temp_img = Image.open(input_image_path)
    img_height = int(temp_img.height/downscale_factor)
    img_width = int(temp_img.width/downscale_factor)
    # the resize does not accept floats

    output_image = temp_img.resize((img_width, img_height), resampling)

    output_path = ""

    if output_file == None:
        output_path = input_image_path.replace(
            f".{file_format}", f"_c.{file_format}")
    else:
        output_path = f"{output_file}.{file_format}"

    output_image.save(output_path)

    print(f"\n{input_file} was converted compressed into {output_path}\n")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Compress Image")
    parser.add_argument("input_file", type=str, help="Name of Input Image")
    parser.add_argument("-d", "--downscale_factor", type=int,
                        help="Downscale Factor for Compression", default=2)
    parser.add_argument("-o", "--output_file", type=str,
                        help="Name of output image", default=None)
    parser.add_argument("-q", "--quality", type=int,
                        help="Format of Image after Conversion", default=1)
    parser.add_argument("-f", "--file_format", type=str,
                        help="Format of Image after Conversion", default="png")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    compress_image(args.input_file, args.downscale_factor,
                   args.output_file, args.quality, args.file_format)

    return 0


if __name__ == "__main__":
    main()
