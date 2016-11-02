#!/usr/bin/env python
"""
Author: Guanduo
chmod +x clean.py
./clean.py will work base on shebang above
default is to clean all .pyc files recursively from current dir to all 

-all: clean all .pyc, .xml, .log
-xml: clean .pyc, .xml
-log: clean .pyc, .log
-db:  clean .db
"""
from __future__ import print_function
from sys import argv
import glob
from os import remove
from os.path import isdir
#add more search dir here
dirs = []
files = glob.glob('*')
for f in files:
    if isdir(f):
        dirs.append('./'+str(f)+'/')
#don't forgot current dir
dirs.append('./')

verbose = 0
for arg in argv:
    if arg == "-xml":
        clean_xml = 1
    else:
        clean_xml = 0
    if arg == "-log":
        clean_log = 1
    else:
        clean_log = 0
    if arg == '-db':
        clean_db = 1
    else:
        clean_db = 0
    if arg == '-v':
        verbose = 1
    if arg == "-all":
        clean_xml = 1
        clean_log = 1
        clean_db = 1
    

        #default clean log only
def clc_dir(path,xml=0,log=0,db=0):
    global verbose
    if verbose:
        print("found path="+path)
    files = glob.glob('%s*.pyc'%path)
    for i in files:
        print("del %s"%(i))
        remove("%s"%(i))
    if xml:
        files = glob.glob('%s*.xml'%path)
        for i in files:
            print("del %s"%(i))
            remove("%s"%(i))
    if log:
        files = glob.glob('%s*.log'%path)
        for i in files:
            print("del %s"%(i))
            remove("%s"%(i))
    if db:
        files = glob.glob('%s*.db'%path)
        for i in files:
            print("del %s"%(i))
            remove("%s"%(i))
          
for di in dirs:
    
    clc_dir('%s'%di,clean_xml,clean_log,clean_db)    
