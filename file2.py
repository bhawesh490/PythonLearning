
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
    print(today_minus_8)
    
    last_seven_days=[]
    seven_forteen_days=[]
    for i in range(1,8):
        last_seven_days.append(date.today() - timedelta(days=i))
    
    for i in range(8,15):
        seven_forteen_days.append(date.today() - timedelta(days=i))
    
    print(last_seven_days)
    print(seven_forteen_days)
    # outlet/date/camerano/
    # df=pd.DataFrame()
    datalist=[]
    # for i in outlets:
    
    count=0
    for object_summary in my_bucket.objects.filter(Prefix="PUN-1040/{}".format(today_minus_8)):
        count=count+1
        # print object_summary.key
        # break
        
    print(count)
        
except Exception as e:
    print(e)         
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
