import os
import cv2
import imgaug.augmenters as aug
from PIL import Image


new_width = 800
new_height = 600

# mendefinisikan direktori sumber dan tujuan
source_directory = r"F:\CAPSTONE\dataset\memorytray"
target_directory = r'F:\CAPSTONE\dataset\ramresize'

# membuat direktori tujuan jika belum ada
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# membaca file gambar yang ada dari direcory sumber
datafile = os.listdir(source_directory)

for file_name in datafile:
    imagepath = os.path.join(source_directory, file_name)
    #image = cv2.imread(imagepath)
    images = Image.open(imagepath)
    width, height = images.size
    resized_image = images.resize((new_width, new_height), Image.LANCZOS)
    
    # simpan semua gambar yang sudah di agumentasi
    new_file_name = f"{file_name}"
    new_image_path = os.path.join(target_directory, new_file_name)
    resized_image.save(new_image_path)
    
print(f"{new_file_name} saved!")

