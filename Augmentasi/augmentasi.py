import os
import cv2
import imgaug.augmenters as iaa

# Mendefinisikan direktori sumber dan tujuan
source_directory = r"F:\CAPSTONE\dataset\create\edit2"
target_directory = r"F:\CAPSTONE\dataset\Train\2"

# Membuat direktori tujuan jika belum ada
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Membaca daftar file gambar dari direktori sumber
file_list = os.listdir(source_directory)

# Mendefinisikan augmenter
augmenter = iaa.Sequential([
    iaa.Affine(rotate=(-50, 50)),
    iaa.Fliplr(0.9),
    # iaa.Zoom(0.2)
])

# Loop melalui setiap file gambar
for file_name in file_list:
    # Membaca gambar dari direktori sumber
    image_path = os.path.join(source_directory, file_name)
    image = cv2.imread(image_path)

    # Melakukan augmentasi pada gambar
    augmented_images = augmenter.augment_images([image])

    # Menyimpan gambar yang dihasilkan ke direktori tujuan
    for i, augmented_image in enumerate(augmented_images):
        new_file_name = f"a5{file_name}"
        new_image_path = os.path.join(target_directory, new_file_name)
        cv2.imwrite(new_image_path, augmented_image)

print("image saved!")
