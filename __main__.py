import sys
from PIL import Image, ImageOps, ImageDraw

def round_background(input_file_name, output_file_name, color):
    size = (500, 500)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    im = Image.open(input_file_name)
    round = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    round.putalpha(mask)
    round = round.resize((440, 440))

    background = Image.new('RGB', size, "#%s" % color)
    background.paste(round, (30, 30), round)
    background.save(output_file_name)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.stderr.write("ERR: Run \"python . input.jpg output.jpg color\"\n")
        sys.stderr.flush()
        sys.exit(1)
    round_background(sys.argv[1], sys.argv[2], sys.argv[3])
