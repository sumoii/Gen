#coding: UTF-8
import os
path = "/data/user/bio18/Agswag/E"
filenames=os.listdir(path)
f = open("/data/user/bio18/Agswag/Gen/gcfid.txt","w")
for filename in filenames:
    f.write( filename[0:13]+'\n' )
f.close    
