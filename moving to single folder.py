import os
import shutil

input_folders = [
    "/content/final/content/Final/Helmet",
    "/content/NOH/content/OIDv4_ToolKit/NoHelmet",
    "/content/final/content/Final/Person",
    "/content/final/content/Final/Motorcycle",
    "/content/final/content/Final/VehicleRegNumber"
]

output_folder = "/content/single"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

file_counter = 1

for input_folder in input_folders:
    for filename in os.listdir(input_folder):
        base_name, ext = os.path.splitext(filename)
        if ext == ".txt":
            txt_path = os.path.join(input_folder, filename)
            jpg_path = os.path.join(input_folder, base_name + ".jpg")
            
            if os.path.exists(jpg_path):
                new_txt_name = f"{file_counter}.txt"
                new_jpg_name = f"{file_counter}.jpg"
                
                new_txt_path = os.path.join(output_folder, new_txt_name)
                new_jpg_path = os.path.join(output_folder, new_jpg_name)
                
                shutil.copy2(txt_path, new_txt_path)
                shutil.copy2(jpg_path, new_jpg_path)
                
                file_counter += 1

print("Files copied and renamed in", output_folder)
