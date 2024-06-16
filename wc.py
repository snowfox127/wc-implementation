import os
import sys
fileName = sys.argv[2]

def getByteSize(txt):
    st = os.stat(txt)
    return st.st_size

def getTotalLines(txt):
    with open(txt) as f:
        for i,_ in enumerate(f,1):
            pass
    return i

def getAllWords(txt):
    wordCount = 0
    with open(txt) as f:
        data = f.read()
        lines = data.split()
        wordCount += len(lines)
    return wordCount
        

if(sys.argv[1] == "-c"):
    print(getByteSize(fileName),fileName)
    
elif(sys.argv[1] == "-l"):
    print(getTotalLines(fileName),fileName)
    
elif(sys.argv[1] == "-w"):
    print(getAllWords(fileName),fileName)
    
    



        
    