from pathlib import Path

files = []
for item in Path('.').iterdir():
    if item.is_file():
        files.append(item.name)
print(sorted(files))