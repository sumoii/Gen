#!/bin/bash
while read line; do echo $line | grep -o 'WP' | wc -l; done < dump.data.mci.I14 > rowcount.txt
#输出每一行所包含多少个GCF
grep -ne '80' rowcount.txt | cut -d ":" -f 1 > 80row.txt
#输出每一行包含80个GCF的行号
for ((i=1;i<=80;i++))
do j=`sed -n "$i p" seqlist`
   grep -n "$j" dump.data.mci.I14 | cut -d ":" -f 1 > $i.txt
done
#将每一个GCF所在dump文件的所有行号输出到一个文件
for ((i=1;i<=80;i++))
do 
   common=`grep -f $i.txt 80row.txt`
done
#找出每一个文件与80row.txt共同具有的行
echo $common | sed 's/ /\n/g' > rows.txt