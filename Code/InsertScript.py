import os.path
import sys
import glob
import re
from lib2to3.fixer_util import String
import shutil
from shutil import copyfile
from importlib._bootstrap import SourceFileLoader
import datetime

# Pre-Requirities for script
print('Obtaining Python version')
PythonVersion = int(sys.version[0])
if PythonVersion == 2:
    print('you have python version 2.x.x installed, correct modules will be loaded!')
    import HTMLparser
elif PythonVersion == 3:
    print('you have python version 3.x.x installed, correct modules will be loaded!')
    from html.parser import HTMLParser

###############################
### CLASSES ###################
###############################


class ScriptDriver():
    def __init__(self):
        self.sthGoneWrong = False
        self.insertScriptString = '<script type="text/javascript" src="../aligner.js"></script>'
        self.insertjQString = '<script type="text/javascript" src="../jquery-1.11.3.js"></script>'
               
    def DiscoverScripts(self, path = ""):
        pass
        
    
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
                            'openTag':          False, 
                            'closeTag':         False, 
                            'HeadPresent':      False,
                            'LocationOpen':     {'line':0,'offset':0},
                            'LocationClose':    {'line':0,'offset':0}
                            }
        self.TrCount = 0
        self.TdCount = 0
        self.RequirementHeaders = {'HeadersObtained': False, 'HeadersText': []}
        self.RequirementsHeadersObtained = False
        self.RequirementsHeaders = []
        
    def feed(self, data):
        print('\n\nParsing Requirements File! Hooray.\n\n')
        HTMLParser.feed(self, data)
    
    def handle_starttag(self, tag, attrs):
        if tag == "head":
            print('Matched <head>')
            self.HeadPresent['openTag'] = True
            self.HeadPresent['LocationOpen']['line'] = self.getpos()[0]
            self.HeadPresent['LocationOpen']['offset'] = self.getpos()[1]
        elif tag == 'tr':
            self.TrCount+=1
            if self.TrCount >= 2:
                self.RequirementsHeadersObtained = True
                self.RequirementHeaders['HeadersObtained'] = True
        elif tag == 'td':
            pass
            
    def handle_endtag(self, tag):
        if tag == "head":
            print('Match </head>')
            self.HeadPresent['closeTag'] = True
            self.HeadPresent['LocationClose']['line'] = self.getpos()[0]
            self.HeadPresent['LocationClose']['offset'] = self.getpos()[1]
            
    def handle_data(self, data):
        if  self.RequirementHeaders['HeadersObtained'] == False and data != '\n' and self.get_starttag_text().find('<title>'):
            self.RequirementHeaders['HeadersText'].append(data)
            self.TdCount+=1
        else:
            pass
    
    def GetHeaderTexts(self):
        return(self.RequirementHeaders['HeadersText'])
    
    def GetHeaderPresence(self):
        if self.HeadPresent['openTag'] and self.HeadPresent['closeTag']:
            return True
        else:
            return False

###############################
### CODE    ###################
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
    print('Review file fetched: ' + WorkFile[0]);
    reviewPath = os.path.join(os.getcwd(), 'review')
    if os.path.exists(reviewPath):  
        print('Review directory already exist. Only new work file will be created')
    else:
        print('Crating review directory...')
        os.mkdir(destinationDir, mode=0o777)

timeStamp = datetime.datetime.now().time()
timeStampFormatted = timeStamp.strftime('%H_%M_%S')     
try:
    ReWriteFile = open( os.path.join(destinationDir, WorkFile[0].split('.')[0]+timeStampFormatted + '.htm'), "w" )
except:
    Sd.ActionOnFault('Creation subfolder was wrong...')

print('Parsing source *.htm to obtain <head> markup')

SourceFile = open(os.path.join(workDir, WorkFile[0]), 'r')
SourceText = SourceFile.read()
parser = DoorsReqParser()      
parser.feed(SourceText)

parser.GetHeaderTexts()

if parser.GetHeaderPresence():
    print('Document already have <head> tag, inserting scripts...')
    for lines in SourceText.splitlines():
        ReWriteFile.write(lines + '\n')
        if lines.find(r'<head>') != (-1):
            ReWriteFile.write(Sd.insertjQString + '\n')
            ReWriteFile.write(Sd.insertScriptString + '\n')   
    ReWriteFile.close()
            
else:
    print('Document have no <head>...\nCreating <head> section and embedding scripts')
    for lines in SourceText:
        if lines.find(r'<title>') != (-1):
            ReWriteFile.write('<head>\n')
            ReWriteFile.write(Sd.insertjQString)
            ReWriteFile.write(Sd.insertScriptString)
            ReWriteFile.write('</head>\n')
        else:
            pass
        ReWriteFile.write(line)
    
if not Sd.GetModuleState():
    print("it's ok")
else:
    print("Results may be invalid")
