import glob
import os

def delete_files(pattern):
  files = glob.glob(pattern)
  for file in files:
    os.remove(file)
