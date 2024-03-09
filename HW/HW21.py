import os

directory = "C:\\Python317\\317\\Work"

files = []

files += os.listdir(directory)

print(sorted(files, reverse=True))
