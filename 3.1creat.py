# -*- coding: utf-8 -*-

import os    
 
path = "/data/user/bio18/Agswag/Gen/single_gene"

filenames=os.listdir(path)#将path路径下的所有文件名存入列表filenames
for filename in filenames:#循环遍历每个文件  
       outf = open("/data/user/bio18/Agswag/Gen/Blastsingle_gene/%s"%filename,'w')  
