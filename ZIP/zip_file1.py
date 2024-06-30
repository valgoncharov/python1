from zipfile import ZipFile
from pathlib import Path

with ZipFile('my-files.zip', mode='w') as my_zip_file:
    print(my_zip_file)
    for file in Path('my-files').iterdir():
        print(file)
        my_zip_file.write(file)
