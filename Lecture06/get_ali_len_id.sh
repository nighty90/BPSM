#! /bin/bash
unset IFS
IFS=$'\t'
flag=1
while read q_acc s_acc id ali_len mismat gap q_s q_e s_s s_e evalue bit_score
do
	if [ ${q_acc:0:1} == "#" ]
	then
		echo "ignore"
	else
		if [[ ${flag} == 1 ]]
		then
			echo -e "alignment length\tpercent ID" > ali_len_id.txt
			flag=0
		fi
		echo -e "${ali_len}\t${id}" >> ali_len_id.txt
	fi
done < blastoutput2.out
