import os
from PIL import Image
import rembg
import numpy as np

# Core engine of the program
def remover():
    # Initialize all variables
    to_process_folder = "To Process\\"
    done_folder = "Done\\"
    file_name_list = [f for f in os.listdir("To Process") if os.path.isfile(os.path.join("To Process", f))]
    n = 0
    # Show how many files are there to process
    print(f"Files to process: {len(file_name_list)}")

    for pic in file_name_list:
        n += 1 # Counter for displaying progress
        to_do_pic = Image.open(to_process_folder + pic)
        processed_pic = rembg.remove(to_do_pic)

        # Numpy magic! Makes an array from picture
        pic_np = np.array(processed_pic)
        rows = np.any(pic_np, axis=1)
        cols = np.any(pic_np, axis=0)
        rows_min, rows_max = np.where(rows)[0][[0, -1]]
        cols_min, cols_max = np.where(cols)[0][[0, -1]]

        # Finding the dimensions of an object and cropping to 10px on each side
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

        # Show progress
        print(f"Image {n} of {len(file_name_list)} processed.")

    # Message when finished
    print("\nDone!")
    print("-" * 30 + "\n")

# Menu - for now if input doesn't start at "y" 
# it closes the app after pressing "ENTER" key
print("Make sure all files are in \"To Process\" folder.")
start = input("Start the program? (Y/N): ").upper()
while start[0] == "Y":
    remover()
    start = input("Press \"ENTER\" to exit or \"Y\" to start again: ").upper()


