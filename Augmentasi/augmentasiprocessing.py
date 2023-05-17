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
    print("-"*30)
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
    print("-"*30)
    print("Image saved!".center(30))

def moveddata(source_dir, folder, pathTrain, pathTest, pathVal):
    #Membuat direktori tujuan jika belum ada
    if not os.path.exists(pathTrain):
        os.makedirs(pathTrain)

    if not os.path.exists(pathTest):
        os.makedirs(pathTest)   

    if not os.path.exists(pathVal):
        os.makedirs(pathVal)

    
    filelist = os.listdir(source_dir)
    random.shuffle(filelist)
    os.makedirs(os.path.join(pathTrain, str(folder)), exist_ok= True)
    os.makedirs(os.path.join(pathTest, str(folder)), exist_ok= True)
    os.makedirs(os.path.join(pathVal, str(folder)), exist_ok= True)
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
        targetpath = os.path.join(pathTrain, str(folder), file)
        shutil.move(sourcepath, targetpath) 

    for file in val_files:
        sourcepath = os.path.join(source_dir, file)
        targetpath = os.path.join(pathVal, str(folder), file)
        shutil.move(sourcepath, targetpath) 

    for file in test_files:
        sourcepath = os.path.join(source_dir, file)
        targetpath = os.path.join(pathTest, str(folder), file)
        shutil.move(sourcepath, targetpath) 
    print("-"*30)
    print("Remove file sucessfull".center(30))

folder = str(200) # ganti sesuai nama datanya apa, misalnya 1, maka hasil foldernya train = 1, val = 1, test = 1

# sipakan path / directory / folder untuk spilt data train, val, test [70, 20, 10]
pathTrain = r'F:\CAPSTONE\dataset\RAM\Train'
pathVal = r'F:\CAPSTONE\dataset\RAM\Val'
pathTest = r'F:\CAPSTONE\dataset\RAM\Test'

# menentukan path yang di pakai
sourceImage = r"F:\CAPSTONE\dataset\PERSON\Sample1_1.jpg"
targetReproducePath = fr"F:\CAPSTONE\dataset\UJI\{folder}"
targetAugemtasiPath = fr"F:\CAPSTONE\dataset\AUG\{folder}"
# jumlah gambar yang ingin di perbanyak
jumlah = 1

try:
    # ini bisa di kasih comment pakai "#" kalo gambarnya udah banyak dan perlu proses augmentasi aja
    duplicate(sourceImage, targetReproducePath, jumlah)
    #time.sleep(1/10)
    # ini buat di augmentasi jadi dikasih effect rotate, grayscale dll
    aug_images(targetReproducePath, targetAugemtasiPath)
    print("-"*30)
    print(f"Augemtasi gambar ke - {folder}")
    #time.sleep(1/10)
except Exception as e:
    print(f" We got some error : {str(e)}" )
    raise e
finally:
    # ini buat splitdata gambar yang udah di augmentasi
    moveddata(targetAugemtasiPath, folder,pathTrain, pathVal, pathTest)
    print("-"*30)
# ini buat foldernya manual, nanti tinggal copy as path aja ya
