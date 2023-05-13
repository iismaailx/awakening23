import cv2
import numpy as np
import imgaug.augmenters as aug
import random
import shutil
import os
import time

# membuat fungsi untuk menyalin gambar
def duplicate(sourcepath, targetpath, n):
    image = cv2.imread(sourcepath)
    # membuat salinan gambar
    duplicate_images = [image.copy() for i in range(n)]
    # membuat direktori baru
    os.makedirs(targetpath, exist_ok= True)
    # menyimpan seluruh gambar scara lokal
    for j, duplicate_image in enumerate(duplicate_images):
        outputFileName = os.path.join(targetpath, f'images{j}.jpg')
        cv2.imwrite(outputFileName, duplicate_image)

    print(f"Images in duplicate {n} pieces")
    
def aug_images(source_directory, target_directory):
    #Membuat direktori tujuan jika belum ada
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Membaca daftar file gambar dari direktori sumber
    file_list = os.listdir(source_directory)

    # Mendefinisikan augmenter
    augmenter = aug.Sequential([
        aug.Affine(rotate=(-35, 35)),
        aug.Fliplr(0.5),
        aug.Flipud(0.5),
        aug.Grayscale(alpha=0.5)
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

def moveddata(source_dir, folder):
    # Ganti seusuai dengan path yang di inginkan
    pathtrain = r'F:\CAPSTONE\dataset\RAM\Train'
    pathtest = r'F:\CAPSTONE\dataset\RAM\Test'
    pathval = r'F:\CAPSTONE\dataset\RAM\Val'
    filelist = os.listdir(source_dir)
    random.shuffle(filelist)
    os.makedirs(os.path.join(pathtrain, str(folder)), exist_ok= True)
    os.makedirs(os.path.join(pathtest, str(folder)), exist_ok= True)
    os.makedirs(os.path.join(pathval, str(folder)), exist_ok= True)
    num_files = len(filelist)
    num_train = int(0.7*num_files)
    num_val = int(0.2*num_files)
    num_test = num_files-num_train-num_val

    # Memisahkan file gambar ke dalam folder train, val, dan test
    train_files = filelist[:num_train]
    val_files = filelist[num_train:num_train+num_val]
    test_files = filelist[num_train+num_val:]


    # memindahkan file
    for file in train_files:
        sourcepath = os.path.join(source_dir, file)
        targetpath = os.path.join(pathtrain, str(folder), file)
        shutil.move(sourcepath, targetpath) 

    for file in val_files:
        sourcepath = os.path.join(source_dir, file)
        targetpath = os.path.join(pathval, str(folder), file)
        shutil.move(sourcepath, targetpath) 

    for file in test_files:
        sourcepath = os.path.join(source_dir, file)
        targetpath = os.path.join(pathtest, str(folder), file)
        shutil.move(sourcepath, targetpath) 

    print("remove file sucessfull")

folder = str(50) # ganti sesuai nama datanya apa
# menentukan path yang di pakai
path1 = r'F:\CAPSTONE\dataset\ramresize\20230505_133731.jpg'
path2 = fr"F:\CAPSTONE\dataset\mencobacodebaru\{folder}"
path3 = fr"F:\CAPSTONE\dataset\Augmentasi\{folder}"
path4 = fr"F:\CAPSTONE\dataset\Done\{folder}"

jumlah = 100

try:
    duplicate(path1, path2, jumlah)
    #time.sleep(1/10)
    aug_images(path2, path3)
    #time.sleep(1/10)
except Exception as e:
    print(f" We got some error : {str(e)}" )
    raise e
finally:
    moveddata(path3, folder)
    print(f"augemtasi gambar ke - {folder}")

# ini buat foldernya manual, nanti tinggal copy as path aja ya
