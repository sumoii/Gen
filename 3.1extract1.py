#-*- coding: UTF-8 -*- 
open_diff = open('dump.data.mci.I40', 'r')
diff_line = open_diff.readlines()

diff_match_split = diff_line[17:39] 

# 将切分的写入多个txt中
for i, j in zip(range(0, diff_match_split.__len__()), range(0, diff_match_split.__len__())):
    with open('single_gene%d.faa' % j, 'w+') as temp:
        for line in diff_match_split[i]:
            temp.write(line)