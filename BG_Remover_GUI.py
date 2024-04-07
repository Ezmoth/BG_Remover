import os
from PIL import Image
import rembg
import numpy as np
import tkinter


# GUI initialization
GUI = tkinter.Tk()
GUI.geometry("300x180")
GUI.title("BG Remover")

done = tkinter.StringVar()
done.set("")
progress = tkinter.StringVar()
progress.set("")
# File count on beginning
count_all = [f for f in os.listdir("To Process") if os.path.isfile(os.path.join("To Process", f))]
count_all_files = tkinter.StringVar()
count_all_files.set(f"Files to process: {len(count_all)}")
lbl_count_files = tkinter.Label(GUI, textvariable=count_all_files)

lbl_info = tkinter.Label(GUI, text="Make sure all pictures are in \"To Process\" folder.")
lbl_progress = tkinter.Label(GUI, textvariable=progress)
lbl_done = tkinter.Label(GUI, textvariable=done)

# File count on beginning
count_all = [f for f in os.listdir("To Process") if os.path.isfile(os.path.join("To Process", f))]
lbl_count_files = tkinter.Label(GUI, text=f"Files to process: {len(count_all)}")

# Core engine of the program
def remover():
    # Initialize all variables
    to_process_folder = "To Process\\"
    done_folder = "Done\\"
    file_name_list = [f for f in os.listdir("To Process") if os.path.isfile(os.path.join("To Process", f))]
    n = 0
    
    # Update label for file_count
    count_all_files.set(f"Files to process: {len(file_name_list)}")

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
        progress.set(f"Image {n} of {len(file_name_list)} processed.")
        GUI.update()

    # Message when finished
    done.set("Done!")


# Making buttons
bnt_BGRemove = tkinter.Button(GUI, text="Remove Background!", command=remover)
bnt_exit = tkinter.Button(GUI, text="Exit", command=GUI.quit)


# Grid placement
lbl_info.grid(row=0, column=0, padx=10)
lbl_count_files.grid(row=1, column=0, padx=10, pady=2, sticky="W")
bnt_BGRemove.grid(row=2, column=0, padx=10, pady=2)
lbl_progress.grid(row=3, padx=10, pady=2)
lbl_done.grid(row=4, padx=10, pady=2)
bnt_exit.grid(row=10, column=0, padx=10, pady=4)

GUI.mainloop()