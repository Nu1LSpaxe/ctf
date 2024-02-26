#!/bin/bash

up="local in function"
since="not use local in function"

showtime(){
	local up=$(uptime -p | cut -c4-)
	since=$(uptime -s)
	cat << EOF
-----------------------------------------------
This machine hase been up for ${up}
It has been running since ${since}
-----------------------------------------------
EOF
}

echo $up ", " $since

showtime

echo $up ", " $since
