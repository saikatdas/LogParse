import sys,os
strKeyWord=str(sys.argv[1])
print(strKeyWord)
#select all log files present in current working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    programfilename= str(f)
    isPythonExtension=programfilename.endswith('.py')
    if(not isPythonExtension): #we don't want to open python file 
        print("===============Opening================")
        print(f)
        print("--------------------------------------")
        count=0
        fileline = open(f,"r")
        for x in fileline:
            result=x.find(strKeyWord)
            if(result!=-1):
                count+=1
                print("line ",count,": ",x)
        fileline.close()
        print(count," lines are selected")
print("===============Closed================")


