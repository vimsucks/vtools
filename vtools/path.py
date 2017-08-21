import os
import sys
import inspect

def create_file_if_not_exists(path):
    if not os.path.exists(path):
        os.mknod(path)

def create_dir_if_not_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)

def same_dir_file(file_name):
    return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), file_name)
