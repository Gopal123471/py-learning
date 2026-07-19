import os

directory = "C:\mountain"

contents = os.listdir(directory)

for item in contents:
    print(item)