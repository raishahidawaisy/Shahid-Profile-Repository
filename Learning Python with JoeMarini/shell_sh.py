#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    source = path.realpath("textfile.txt")

    
    # let's make a backup copy by appending "bak" to the name
    destination = source + ".bak"
    
    # copy over the permissions, modification times, and other info
    #shutil.copy(source,destination)
    # line 20 will only copy the content of the file, if other data like 
    # modification time + other metadata related to file needs copy use
    #shutil.copystat(source,destination)

    # rename the original file
    #os.rename("textfile.txt.bak", "newfile.txt")
    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(source)
    # shutil.make_archive("archive","zip", root_dir)
    # line 31 will make an archive of the whole directory

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip","w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("newfile.txt")

      
if __name__ == "__main__":
  main()
