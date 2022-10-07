#! /bin/bash
unset IFS
IFS=$'\t'
while read q_acc s_acc id ali_len mismat gap q_s q_e s_s s_e evalue bit_score
do
	if [ ${q_acc:0:1} == "#" ]
	then
		echo "ignore"
	else
		echo -e "${s_acc}" >> s_acc.txt
	fi
done < blastoutput2.out
