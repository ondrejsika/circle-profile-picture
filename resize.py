import sys
from PIL import Image, ImageOps, ImageDraw

def resize(input_file_name, output_file_name, size):
    im = Image.open(input_file_name)
    im = im.resize((size, size))
    im.save(output_file_name)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write("ERR: Run \"python resize.py input.jpg output.jpg size\"\n")
        sys.stderr.flush()
        sys.exit(1)
    resize(sys.argv[1], sys.argv[2], int(sys.argv[3]))
