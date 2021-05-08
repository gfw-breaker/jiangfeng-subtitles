#!/bin/bash

key=$1

files=$(grep $key zh/*/*.txt | grep -v readme | grep -v tw.txt | cut -d':' -f1 | sort | uniq)

for path in $files;	 do
	folder=$(dirname $path)
	episode=$(basename $path | cut -d'.' -f1)
	title=$(grep $episode $folder/readme.txt | cut -d'.' -f2)
	echo $title
done


