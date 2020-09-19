import pandas as pd
from fsspec.implementations.sftp import SFTPFileSystem
from io import StringIO
import os
import sys


#Connect to sftp site
fs = SFTPFileSystem(host=" ",username= "",password = "")

#Read and retrieve file 
with fs.open(" [#FileRetrieved] ") as f:
	content = f.read()


s = str(content,'utf-8')
data = StringIO(s)
yourDf = pd.read_csv(data)

directory ='[location in directory]'


yourDf = yourDf.rename(columns = {"col1":"COL1"})



for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        list_r = pd.read_csv(directory+'/'+filename,engine='python') 
        list_df = list_r 
        test_merge = inovaytDf.merge(list_df, how='inner', on='COL1')
        test_merge = test_merge.rename(columns = {"COL1":"col1"})
        test_merge.to_csv(directory+'directory'+'(You choose)'+filename, index = False, date_format="%Y-%m-%d")