import os

def ensure_image_extension(file_name):
    image_extensions = ['png', 'jpg', 'jpeg', 'heic', 'gif', 'bmp', 'tiff']

    # Default behavior when no extension is given: assume it is a HEIC image

    if "." not in file_name:
        file_name = file_name + ".HEIC"
    else:
        file_extension = file_name.split(".")[-1].lower()

        if file_extension not in image_extensions:
            raise ValueError(f"Invalid image file extension: {file_extension}. Supported extensions are: {', '.join(image_extensions)}")
    
    return file_name

def get_image_path_from_name(file_name):
    current_path = os.getcwd()

    file_name = ensure_image_extension(file_name) 
    # Raises an error if not true, stoping the program (because no try block)

    file_path = os.path.join(current_path, file_name)

    return file_path
