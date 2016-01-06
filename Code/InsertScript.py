import os.path
import sys
import glob

PythonVersion = int(sys.version[0])
if PythonVersion == 2:
    print('you have python version 2.x.x installed.\nCorrect modules will be loaded!')
    import HTMLparser
elif PythonVersion == 3:
    print('you have python version 3.x.x installed.\nCorrect modules will be loaded!')
    from html.parser import HTMLParser


print("Inserting scripts to HTML")

insertScriptString = '<script src="aligner.js"></script>'
insertjQString = '<script src="jquery-1.11.3.js"></script>'

res = glob.glob("*.htm")
if  len(res) == 0:
    print("No review file in work dir, unable to load")
elif len != 0:
    print("Multiple files in work dir, unable to load")




print("its ok")