#! usr/bin/bash
unset IFS
IFS=$'\t'
flag=1
while read line
do
	if [ ${q_acc:0:1} == "#" ]
	then
		echo "ignore"
		continue
	fi
	
	if [ $flag -eq 1 ]
	then
		echo "s_acc" > s_acc.txt
		flag=0
	fi
	
	read q_acc s_acc id ali_len mismat gap q_s q_e s_s s_e evalue bit_score <<< ${line}
	echo -e "${s_acc}" >> s_acc.txt
	
done < blastoutput2.out
