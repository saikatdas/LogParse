import sys,os
length=len(sys.argv)
if(length==1):
    print ("Kindly enter anytext to search")
    sys.exit(0)
strKeyWord=str(sys.argv[1])
print(strKeyWord)
#select all log files present in current working directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    programfilename= str(f)
    isPythonExtension=programfilename.endswith('.txt')
    if(isPythonExtension): #we don't want to open python file or screenshot , just open txt file
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


