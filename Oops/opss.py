
#Traversing file system 

import os

"""OS.walk() generate the file names in a directory tree by walking the tree either top-down or bottom-up.
For each directory in the tree rooted at directory top (including top itself), 
it yields a 3-tuple (dirpath, dirnames, filenames)."""
 
 
for dirpath, dirnames, filenames in os.walk('/home/panda/'):
    print('Current Path:',dirpath)
    print('Current Path:',dirnames)
