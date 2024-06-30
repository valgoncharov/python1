from pathlib import Path

file_path = Path('test.txt')

print([m for m in dir(file_path)
       if not m.startswith('_')])

print(Path.cwd())

# For mac and unix

print(Path('usr').joinpath('local').joinpath('bin'))

print(Path('usr')/'local'/'bin')

# For windows

print(Path('C:/').joinpath('Users').joinpath('Valik'))
print(Path('C:/')/'Users'/'Valik')

# Exists file

print(Path('main.py').exists())
print(Path('/Users/Valik/Desktop').exists())
print(Path('other.py').exists())

# Is dir or file

print(Path('main.py').is_file())
print(Path('../python').is_file())
print(Path('../python').is_dir())

# List file

for f in Path('.').iterdir():
    print(f)


cwd = Path('.')
cwd_new = Path('/Users')/'Valik'/'python'


print(cwd.__str__)
print(isinstance(cwd, Path))
print(type(cwd))

print(Path.__subclasses__())

print(dir(cwd))
print(cwd.absolute())

if not cwd_new.exists():
    cwd_new.mkdir()

if cwd_new.exists():
    cwd_new.rmdir()
