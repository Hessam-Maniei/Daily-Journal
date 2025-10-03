import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder_name = ext + "_files"
            folder_dir = os.path.join(folder_path, folder_name)

            if not os.path.exists(folder_dir):
                os.makedirs(folder_dir)

            shutil.move(file_path, os.path.join(folder_dir, filename))

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organize_files(folder)
    print("Files organized successfully!")
