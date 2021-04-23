#!/bin/bash
for file in `ls $1`
    do
        filename=`echo "$file"`
        id=${filename: 0 : 13}
        sed -i "s/\.1/\.1$id/"  $file
done