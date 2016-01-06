import os.path
import sys
import glob
from lib2to3.fixer_util import String
import shutil
from shutil import copyfile

PythonVersion = int(sys.version[0])
if PythonVersion == 2:
    print('you have python version 2.x.x installed.\nCorrect modules will be loaded!')
    import HTMLparser
elif PythonVersion == 3:
    print('you have python version 3.x.x installed.\nCorrect modules will be loaded!')
    from html.parser import HTMLParser

insertScriptString = '<script src="aligner.js"></script>'
insertjQString = '<script src="jquery-1.11.3.js"></script>'

workDir = os.getcwd()
destinationDir = os.path.join(workDir, 'review')
sthGoneWrong = False;

print('trying to discover review file...');
WorkFile = glob.glob("*.htm")
if  len(WorkFile) == 0:
    print("No review file in work dir, unable to load")
    sthGoneWrong = True;
elif len(WorkFile) > 1:
    print("Multiple files in work dir, unable to load")
    sthGoneWrong = True;
else:
    print('trying to create /review subfolder for modified files...');
    reviewPath = os.path.join(os.getcwd(), 'review')
    result = os.path.exists(reviewPath)
    if os.path.exists(reviewPath):
        print("Path already exist! You may created before your /review dir. If no, remove /review")
        sthGoneWrong = True;
    else:
        print('Crating blank file to embed JS files...')
        os.mkdir(destinationDir, mode=0o777)
        try:
            print(os.path.join(workDir, WorkFile[0]))
            print(os.path.join(destinationDir, WorkFile[0]))
            ReWriteFile = open( os.path.join(destinationDir, WorkFile[0]), "w" )
            #copyfile(WorkFile[0], os.path.join(destinationDir, WorkFile[0]))
        except:
            print('Creation was wrong...')
            sthGoneWrong = True;
        try:
            print('')
        except:
            print('Copying data was incorrect...')
            sthGoneWrong = True;
            
if not sthGoneWrong:
    print("it's ok")
else:
    print("Results may be invalid")