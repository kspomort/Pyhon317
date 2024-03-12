# import os
#
# directory = "C:\\Python317\\317\\Work"
#
# files = []
#
# files += os.listdir(directory)
#
# print(sorted(files, reverse=True))
import os

root = "C:\\Python317\\317\\Work"
objs = os.listdir(root)
# print(objs)
objs = list(map(lambda i: os.path.join(root, i), objs,))
# print(objs)

obj_sort = sorted(objs, key=os.path.isfile, reverse=True)
print(obj_sort)