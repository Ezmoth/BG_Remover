import os
from PIL import Image, ImageOps
import numpy as np
import rembg

parts_folder = "Res\\"
done_folder = "Done\\"
to_process_folder = "To Process\\"
file_name_list = [f for f in os.listdir(to_process_folder) if os.path.isfile(os.path.join(to_process_folder, f))]
part_1 = parts_folder + "1.png"
part_2 = parts_folder + "2.png"


for pic in file_name_list:
    process_img = Image.open(to_process_folder + pic)
    process_img = ImageOps.exif_transpose(process_img)
    process_part_1 = Image.open(part_1)
    width_img = max(process_img.size[0], process_part_1.size[0])
    height_img = process_img.size[1] + process_part_1.size[1]
    new_img = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    new_img.paste(process_img)
    new_img.paste(process_part_1, ((process_img.size[0]//2 - process_part_1.size[0]//2), process_img.size[1]))
    new_img.save(done_folder + pic)

