#coding: UTF-8#设置编码
import os

source_path = '/data/user/bio18/Agswag/Gen/single_gene'
file_list = os.listdir(source_path)
for file in file_list:
    full_sou = os.path.join(source_path, file)
    full_tar = os.path.join(source_path, file)

    print("process:", full_sou)
    
    with open(full_sou, 'r') as f:
        context = f.readlines()
        context = list(map(lambda x: x.replace('\t','\n'),context))
    with open(full_tar, 'w') as f:
        f.writelines(context)
