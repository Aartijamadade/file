import os
import glob

folder_path = "C:/Users/Dipak/Desktop/python"


files = glob.glob(os.path.join(folder_path, '*'))


files.sort(key=os.path.getmtime, reverse=True)


latest_files = files[:5]

for file in files[5:]:
    os.remove(file)
