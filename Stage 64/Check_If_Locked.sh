#!/bin/bash
while :
do
	s=$(date +%s)
	while read line
	do
		if [[ $(echo $line | sed 's/[0-9]\{1,2\}\. //') == 'LOCKED - US' ]]
		then
			s="$s -"
		else
			s="$s X"
			echo "$line" > echo "$line" > "$(echo "$line"|sed 's/\..*//')"
		fi
	done < <(curl -u $(curl -s http://averyhardtest.com/421563647 | grep -Po "[0-9]{2,4}(?=:)"):$(curl -s ipinfo.io/ip) -s averyhardtest.com:64 | egrep \[0-9\]\{1,2\}\\.)
	echo "$s" >> logfile
	sleep 30
done	