import os

with open('result.txt', 'w', encoding='utf-8') as outfile:
    for filename in ['file1.txt', 'file2.txt']:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
print("The file is merged into result.txt")
