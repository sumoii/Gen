#coding: UTF-8#设置编码
import os
path = "/data/user/bio18/schj/genomic_p/mcl/seq_source"
filenames=os.listdir(path)#将path路径下的所有文件名存入列表filenames
for filename in filenames:#循环遍历每个文件
    f2 = open("/data/user/bio18/schj/genomic_p/mcl/seq_out/%s"%filename,"w")#%s格式化字符串
    with open(filename,"r") as f1:
         for line in f1:
             if ">" in line:
                line_list=list(line)
                line_list.insert(15,":"+filename[0:13])
                line=''.join(line_list)
                print(line)
             f2.write(line)