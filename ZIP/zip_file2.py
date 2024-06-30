from zipfile import ZipFile
from pathlib import Path

with ZipFile('my-files.zip') as my_zip_file:
    my_zip_file.extractall('my-files-unzipped')

with ZipFile('my-files.zip') as my_zip_file:
    my_zip_file.extractall('my-files-second')

with ZipFile('my-files.zip') as my_zip_file:
    print(my_zip_file.infolist())

with ZipFile('my-files.zip') as my_zip_file:
    print(my_zip_file.filename)
