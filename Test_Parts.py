from PIL import Image
import numpy as np


def parts_1(done_folder, processed_pic, pic):
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])
    white_bg.save(done_folder + pic)

    return white_bg

def parts_2(done_folder, parts_folder, processed_pic, pic):
    numbers = parts_folder + "2.png"
    process_part1 = Image.open(numbers)
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    # Finding the dimensions of an object
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])

    width_img = max(white_bg.size[0], process_part1.size[0])
    height_img = white_bg.size[1] + process_part1.size[1]
    parts_image = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    parts_image.paste(white_bg)
    parts_image.paste(process_part1, ((white_bg.size[0]//2 - process_part1.size[0]//2), white_bg.size[1]))
    parts_image.save(done_folder + pic)

    return parts_image

def parts_3(done_folder, parts_folder, processed_pic, pic):
    numbers = parts_folder + "3.png"
    process_part1 = Image.open(numbers)
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    # Finding the dimensions of an object
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])

    width_img = max(white_bg.size[0], process_part1.size[0])
    height_img = white_bg.size[1] + process_part1.size[1]
    parts_image = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    parts_image.paste(white_bg)
    parts_image.paste(process_part1, ((white_bg.size[0]//2 - process_part1.size[0]//2), white_bg.size[1]))
    parts_image.save(done_folder + pic)

    return parts_image

def parts_4(done_folder, parts_folder, processed_pic, pic):
    numbers = parts_folder + "4.png"
    process_part1 = Image.open(numbers)
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    # Finding the dimensions of an object
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])

    width_img = max(white_bg.size[0], process_part1.size[0])
    height_img = white_bg.size[1] + process_part1.size[1]
    parts_image = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    parts_image.paste(white_bg)
    parts_image.paste(process_part1, ((white_bg.size[0]//2 - process_part1.size[0]//2), white_bg.size[1]))
    parts_image.save(done_folder + pic)

    return parts_image

def parts_5(done_folder, parts_folder, processed_pic, pic):
    numbers = parts_folder + "5.png"
    process_part1 = Image.open(numbers)
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    # Finding the dimensions of an object
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])

    width_img = max(white_bg.size[0], process_part1.size[0])
    height_img = white_bg.size[1] + process_part1.size[1]
    parts_image = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    parts_image.paste(white_bg)
    parts_image.paste(process_part1, ((white_bg.size[0]//2 - process_part1.size[0]//2), white_bg.size[1]))
    parts_image.save(done_folder + pic)

    return parts_image

def parts_6(done_folder, parts_folder, processed_pic, pic):
    numbers = parts_folder + "6.png"
    process_part1 = Image.open(numbers)
    # Numpy magic! Makes an array from picture
    pic_np = np.array(processed_pic)
    rows = np.any(pic_np, axis=1)
    cols = np.any(pic_np, axis=0)
    # Finding the dimensions of an object
    rows_min, rows_max = np.where(rows)[0][[0, -1]]
    cols_min, cols_max = np.where(cols)[0][[0, -1]]

    # Finding the dimensions of an object and cropping to 10px on each side of an object
    rows_min = max(0, rows_min - 10)
    rows_max = min(pic_np.shape[0], rows_max + 10)
    cols_min = max(0, cols_min -10)
    cols_max = min(pic_np.shape[1], cols_max + 10)

    # Cropping the picture and converting it from array back to image
    cropped_pic_np = pic_np[rows_min:rows_max, cols_min:cols_max]
    cropped_pic = Image.fromarray(cropped_pic_np)

    # Creating white background, pasting the image on top and saving to "Done" folder
    white_bg = Image.new("RGB", cropped_pic.size, (255, 255, 255))
    white_bg.paste(cropped_pic, mask=cropped_pic.split()[3])

    width_img = max(white_bg.size[0], process_part1.size[0])
    height_img = white_bg.size[1] + process_part1.size[1]
    parts_image = Image.new("RGB", (width_img, height_img), (255, 255, 255))

    parts_image.paste(white_bg)
    parts_image.paste(process_part1, ((white_bg.size[0]//2 - process_part1.size[0]//2), white_bg.size[1]))
    parts_image.save(done_folder + pic)

    return parts_image