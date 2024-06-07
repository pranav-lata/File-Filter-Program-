import os 
import shutil 

# Define the target directory name
targert_dir = "Filtered_Files"

#Making the desktop path for the folder
desktop_dir = os.path.join(os.path.expanduser("~"),r"C:\Users\Pranav\Desktop\File_Filter_Program")

#Making the target directory path complete
target_dir_path = os.path.join(desktop_dir,targert_dir)

#Making the target folder if it does not exists
if  os.path.exists(target_dir_path):
    print("Directory already Exists")
else:
    os.mkdir(target_dir_path)
    print("Directory created Successfully")

#Defining the Folders
text_folder = os.path.join(target_dir_path, "text")
pdf_folder = os.path.join(target_dir_path, "pdf")
image_folder = os.path.join(target_dir_path, "image")

#Creating the Folders
if not os.path.exists(text_folder):
    os.mkdir(text_folder)
if not os.path.exists(pdf_folder):
    os.mkdir(pdf_folder)
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

          
#Naming the Extensions
text_file = (".txt")
image_files = ('.jpeg','.png','.jpg')
pdf_files = ('.pdf')

#Source of all the files 
source = r"C:\Users\Pranav\Desktop\File_Filter_Program\All Files"

#Logic to move the folders from source file to destination file 
for file_name in os.listdir(source):
    source_path = os.path.join(source, file_name)
    destination = None 
    if file_name.lower().endswith(text_file):
        destination = text_folder
    if file_name.lower().endswith(pdf_files):
        destination = pdf_folder
    if file_name.lower().endswith(image_files):
        destination = image_folder

    if destination is not None:
        destination_path = os.path.join(destination, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved '{file_name}' successfully")

     