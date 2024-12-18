# Image Manager

Python package for image handling, mainly conversion between different image types.

# Requirements

The only dependency in this project is `pilow-heif`, which can be obtained by doing

```bash
pip install pillo-heif
```

In order to run as a batch script from anywhere in the computer (accesing from the terminal), refer to my other repository PDF-Editor, which defines the following steps:

1. Clone (or manually paste) this whole repository somewhere in your PC

2. Add this directory (as in where you pasted this repository) to the PATH environmental variable

3. Create a `.bat` file with the following contents

```topng.bat
@echo off
set PYTHONPATH=C:\kev-scripts

:GETOPTS

cmd /k python -m image_manager.image_converter.image_converter %*
exit /B
```

and replace the value of `PYTHONPATH` to the project directory (aka the same directory added to the PATH).

4. Keep in mind that the name of the batch file is the command that you wull need to execute in the terminal, for example in the case you name it `topng.bat`, you'd need to run

```bash
topng my_image
```

5. Run `topng -h` in order to learn ho to use this command

# TODO

-   Add a repository for Image Manager and script functionality
-   Explain what the batch file is doing (?)
