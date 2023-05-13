import os

# mendefinisikan direktori sumber dan tujuan file
source = r'F:\CAPSTONE\dataset\dataset2'
target = r'F:\CAPSTONE\dataset\datasetrename1'

if not os.path.exists(target):
    os.makedirs(target)

list_file = os.listdir(source)
num = 0
for file_name in list_file:
    if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        new_file_name = f'images_{num}.jpg'
        source_file_path = os.path.join(source, file_name)
        target_file_path = os.path.join(target, new_file_name)
        os.rename(source_file_path, target_file_path)
        print(f"renamed and moved {file_name} to {new_file_name}")
        num += 1
# import os

# # Define source and target directories
# source_directory = r'F:\CAPSTONE\dataset\memorytray1'
# target_directory = r'F:\CAPSTONE\dataset\datasetrename'

# # Create target directory if it doesn't exist
# if not os.path.exists(target_directory):
#     os.makedirs(target_directory)

# # Get the list of files in the source directory
# file_list = os.listdir(source_directory)

# # Iterate over each file in the source directory
# for i, file_name in enumerate(file_list):
#     if file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
#         # Construct new file name with a unique index
#         new_file_name = f'images{i}'
        
#         # Build the paths for the source and target files
#         source_file_path = os.path.join(source_directory, file_name)
#         target_file_path = os.path.join(target_directory, new_file_name + os.path.splitext(file_name)[1])
        
#         # Rename and move the file
#         os.rename(source_file_path, target_file_path)
#         print(f"Renamed and moved {file_name} to {new_file_name}")
