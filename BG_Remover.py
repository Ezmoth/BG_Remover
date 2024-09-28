import os
from PIL import Image
import rembg
import Parts

# Core engine of the program
def remover():
    # Initialize all variables
    to_process_folder = "To Process\\"
    done_folder = "Done\\"
    parts_folder = "Res\\"
    file_name_list = [f for f in os.listdir("To Process") if os.path.isfile(os.path.join("To Process", f))]
    n = 0
    # Show how many files are there to process
    print(f"Files to process: {len(file_name_list)}")

    for pic in file_name_list:
        n += 1 # Counter for displaying progress
        to_do_pic = Image.open(to_process_folder + pic)
        processed_pic = rembg.remove(to_do_pic)
        if pic[-6:-4].upper() == "P2":
            Parts.parts_2(done_folder, parts_folder, processed_pic, pic)
        elif pic[-6:-4].upper() == "P3":
            Parts.parts_3(done_folder, parts_folder, processed_pic, pic)
        elif pic[-6:-4].upper() == "P4":
            Parts.parts_4(done_folder, parts_folder, processed_pic, pic)
        elif pic[-6:-4].upper() == "P5":
            Parts.parts_5(done_folder, parts_folder, processed_pic, pic)
        elif pic[-6:-4].upper() == "P6":
            Parts.parts_6(done_folder, parts_folder, processed_pic, pic)
        else:
            Parts.parts_1(done_folder, processed_pic, pic)
        
        # Show progress
        print(f"Image {n} of {len(file_name_list)} processed.")

    # Message when finished
    print("\nDone!")
    print("-" * 30 + "\n")

# Menu - for now if input doesn't start at "y" 
# it closes the app after pressing "ENTER" key
print("Make sure all files are in \"To Process\" folder.")
start = input("Start the program? (Y/N): ").upper()
while start == "Y":
    remover()
    start = input("Press \"ENTER\" to exit or \"Y\" to start again: ").upper()
