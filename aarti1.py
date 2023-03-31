import os
import glob

folder_path = "C:/Users/Dipak/Desktop/python"


files = glob.glob(os.path.join(folder_path, '*'))


files.sort(key=os.path.getmtime, reverse=True)

# keep only the latest 5 files
latest_files = files[:5]

# delete all the other files
for file in files[5:]:
    os.remove(file)
