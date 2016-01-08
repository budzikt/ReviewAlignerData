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
        self.insertScriptString = '<script src="aligner.js"></script>'
        self.insertjQString = '<script src="jquery-1.11.3.js"></script>'
        
    
    def ActionOnFault(self, ErrorText, GlobalAffect=True):
        print(ErrorText)
        if GlobalAffect:
            self.sthGoneWrong = True
        
    def GetModuleState(self):
        return self.sthGoneWrong

class DoorsReqParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self, False)
        self.HeadPresent = {
                            'openTag':False, 
                            'closeTag':False, 
                            'HeadPresent':False,
                            'LocationOpen': {'line':0,'offset':0},
                            'LocationClose': {'line':0,'offset':0}
                            }
        self.TrCount = 0
        self.TdCount = 0
        self.RequirementsHeadersObtained = False
        self.RequirementsHeaders = []
        self.FirstRowString = ''
        
    
    def handle_starttag(self, tag, attrs):
        if tag == "head":
            self.HeadPresent['openTag'] = True
            self.HeadPresent['LocationOpen']['line'] = self.getpos()[0]
            self.HeadPresent['LocationOpen']['offset'] = self.getpos()[1]
        elif tag == 'tr':
            self.TrCount+=1
            if self.TrCount >= 2:
                self.RequirementsHeadersObtained = True
        elif tag == 'td':
            pass
            
    def handle_endtag(self, tag):
        if tag == "head":
            self.HeadPresent['closeTag'] = True
            self.HeadPresent['LocationClose']['line'] = self.getpos()[0]
            self.HeadPresent['LocationClose']['offset'] = self.getpos()[1]
            
    def handle_data(self, data):
        if self.RequirementsHeadersObtained == False and data != '\n':
            self.RequirementsHeaders.append(data)
            self.TdCount+=1
        else:
            pass
    
    def GetHeaders(self):
        print(self.RequirementsHeaders)
    
    def GetHeaderPresence(self):
        if self.HeadPresent['openTag'] and self.HeadPresent['closeTag']:
            return True
        else:
            return False

###############################

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
        print('Crating review directory...')
        os.mkdir(destinationDir, mode=0o777)
        try:
            print(os.path.join(workDir, WorkFile[0]))
            print(os.path.join(destinationDir, WorkFile[0]))
            ReWriteFile = open( os.path.join(destinationDir, WorkFile[0]), "w" )
            
        except:
            Sd.ActionOnFault('Creation subfolder was wrong...')
        print('Parsing source *.htm to obtain <head> markup')

        SourceFile = open(os.path.join(workDir, WorkFile[0]), 'r')
        SourceText = SourceFile.read()
        
        #Creata parser instance
        parser = DoorsReqParser()
        #Feed parser with DOORS document to verify, does it have header
        parser.feed(SourceText)
        if parser.GetHeaderPresence():
            pass
            
if not Sd.GetModuleState():
    print("it's ok")
else:
    print("Results may be invalid")
