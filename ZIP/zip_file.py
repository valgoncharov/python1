from zipfile import ZipFile
from pathlib import Path

Path("my-files").mkdir()

with open("my-files/first.txt", 'w') as my_file:
    my_file.write("This is first file")

with open("my-files/second.txt", 'w') as my_file:
    my_file.write("This is second file")
