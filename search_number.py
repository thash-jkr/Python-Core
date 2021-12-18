import os
import re

pattern = r'\d{3}-\d{3}-\d{4}'


def search(file0, pattern0=r'\d{3}-\d{3}-\d{4}'):
    f0 = open(file0, 'r')
    text = f0.read()

    if re.search(pattern0, text):
        return re.search(pattern0, text)
    else:
        return ''


result = []

for folder, sub_folders, files in os.walk("C:\\Users\\aftha\\Desktop\\Coding "
                                          ")\\Python\\extracted_content2\\extracted_content"):

    for f in files:
        full_path = folder + '//' + f
        result.append(search(full_path))

print(result)
