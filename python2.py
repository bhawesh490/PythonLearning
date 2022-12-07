
# step1=assign a variable with python2 text
# step2=make a file2.py with this text 
# step3=convert with the 2to3 module within the code
# step4= extract the text from the converted file
import os 
python2='''
import sys    
try:
    import pandas as pd 
    global pd
    from io import StringIO
    global StringIO
    import re
    import boto3
    global re
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('outletipcam-new')
    outlets="select code from outlets"
    outlets=execute_query("ProdDB",outlets)['rows']
    
    from datetime import date,timedelta
    today = date.today() - timedelta(days=1)
    today_minus_8=date.today() - timedelta(days=8)
    print today_minus_8
    
    last_seven_days=[]
    seven_forteen_days=[]
    for i in range(1,8):
        last_seven_days.append(date.today() - timedelta(days=i))
    
    for i in range(8,15):
        seven_forteen_days.append(date.today() - timedelta(days=i))
    
    print last_seven_days
    print seven_forteen_days
    # outlet/date/camerano/
    # df=pd.DataFrame()
    datalist=[]
    # for i in outlets:
    
    count=0
    for object_summary in my_bucket.objects.filter(Prefix="PUN-1040/{}".format(today_minus_8)):
        count=count+1
        # print object_summary.key
        # break
        
    print count
        
except Exception as e:
    print e         
    print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
'''

myVar="file2"

x = open (myVar+".py", "w")
x.write(python2)
x.close()
os.system("Echo Hello World")
os.system("echo This is sample text > MyFile.txt")
os.system("2to3 -w file2.py")
# Note for Devops:Running this os.system(2to3 -w file2.py) command in virtual environment
# Run 2to3 file2.py

python3=''' '''
a="file2.py"
filetoopen=open(a,'r')
line=filetoopen.readline()

while(line!=""):
    python3=python3+line
    line=filetoopen.readline()
filetoopen.close()
print (python3)

