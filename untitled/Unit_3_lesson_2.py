import logging
import os
import argparse

os.mknod("/home/elias/PycharmProjects/untitled/dir1/delfile.py")
path = "/home/elias/PycharmProjects/untitled/dir1"
names = os.listdir(path)
for name in names:
    fullname = os.path.join(path, 'delfile.py')
    if os.path.isfile(fullname):
        os.remove(fullname)

args = parser.parse_args()