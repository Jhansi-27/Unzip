import zipfile
with zipfile.ZipFile(r"C:\Users\jhans\Downloads\files.zip", 'r') as zip_ref:
    zip_ref.extractall(r"C:\Users\jhans\Downloads\New folder")
print("hello")