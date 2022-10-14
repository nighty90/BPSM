#! /usr/bin/bash
complete_line=""
touch fixed_NCBI.fasta
while read line
do
	if [[ ${line} == ">"* ]]
	then
		echo ${line} >> fixed_NCBI.fasta
		complete_line=""
	elif [[ ${line} == "" ]]
	then	
		echo ${complete_line} >> fixed_NCBI.fasta
	else
		complete_line=${complete_line}${line^^}
	fi
done < mock_NCBI.fasta
