import os.path
import sys
import glob
from lib2to3.fixer_util import String
import shutil
from shutil import copyfile
from importlib._bootstrap import SourceFileLoader

PythonVersion = int(sys.version[0])
if PythonVersion == 2:
    print('you have python version 2.x.x installed.\nCorrect modules will be loaded!')
    import HTMLparser
elif PythonVersion == 3:
    print('you have python version 3.x.x installed.\nCorrect modules will be loaded!')
    from html.parser import HTMLParser

###############################

class ScriptDriver():
    def __init__(self):
        self.sthGoneWrong = False
    
    def ActionOnFault(self, ErrorText, GlobalAffect=True):
        print(ErrorText)
        if GlobalAffect:
            self.sthGoneWrong = True
        
    def GetModuleState(self):
        return self.sthGoneWrong

class MyHTMLParser(HTMLParser):
    
    def __init__(self, WriteFileHandle):
        HTMLParser.__init__(self, False)
        self.handleF = WriteFileHandle
        self.MatchList = [[],[],[]]
        self.MatchCnt = 0
    
    def handle_starttag(self, tag, attrs):
        if tag == "head":
            self.Offset = self.getpos()
            self.TagText = self.get_starttag_text()
            self.MatchList.append([self.Offset[0], self.Offset[1], self.TagText]) 
            
    def handle_data(self, data):
        return 0
    
    def GetData(self):
        return self.MatchList



###############################

insertScriptString = '<script src="aligner.js"></script>'
insertjQString = '<script src="jquery-1.11.3.js"></script>'

Sd = ScriptDriver()

workDir = os.getcwd()
destinationDir = os.path.join(workDir, 'review')

print('trying to discover review file...');
WorkFile = glob.glob("*.htm")
if  len(WorkFile) == 0:
    Sd.ActionOnFault("No review file in work dir, unable to load")
elif len(WorkFile) > 1:
    Sd.ActionOnFault("Multiple files in work dir, unable to load")
else:
    print('trying to create /review subfolder for modified files...');
    reviewPath = os.path.join(os.getcwd(), 'review')
    result = os.path.exists(reviewPath)
    if os.path.exists(reviewPath):
        Sd.ActionOnFault("Path already exist! You may created before your /review dir. If no, remove /review")
    else:
        print('Crating blank file to embed JS files...')
        os.mkdir(destinationDir, mode=0o777)
        try:
            print(os.path.join(workDir, WorkFile[0]))
            print(os.path.join(destinationDir, WorkFile[0]))
            ReWriteFile = open( os.path.join(destinationDir, WorkFile[0]), "w" )
            #copyfile(WorkFile[0], os.path.join(destinationDir, WorkFile[0]))
        except:
            Sd.ActionOnFault('Creation was wrong...')
        print('Parsing source *.htm to obtain <head> markup')
        try:
            with open(os.path.join(workDir, WorkFile[0]), 'r') as SourceFile:
                SourceText = SourceFile.read()
            
        except:
            Sd.ActionOnFault('Copying data was incorrect...')
            sthGoneWrong = True;
            
if not Sd.GetModuleState():
    print("it's ok")
else:
    print("Results may be invalid")