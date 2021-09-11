import os
import shutil
import stat


def delDir(path):
    os.chmod(path,stat.S_IWRITE)
    shutil.rmtree(path)

query = input('Path to dir: ')
delDir(f'{query}')