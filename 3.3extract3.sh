for line in $(cat gcfid.txt);  
do
   sed -n '/'$line'/{n;p}' newall_put.faa > $line.faa 
   awk '{printf("%s",$0)}' $line.faa | sed 's/\ //g' $1 > new_$line.faa
   sed -i '1i\'$line'' new_$line.faa
   echo"" >> new_$line.faa
done  
