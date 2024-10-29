#!/usr/bin/bash

printf "Welcome to inkscout"
printf "\n\nThis is an app built with Bash and Python."
printf "\nIt uses the Shodan API to search for HP printers with an open port 9100.\n"

printf "\nTo begin, please select an option.\n"

printf "\n1 - Search for HP printers in Canada (recommended)"
printf "\n2 - Search worldwide for HP printers\n\n"

echo -e "Type a number to start, or type q to quit"
read choice


if [ $choice == "q" ]
then exit
fi

python3 crawl.py $choice

printf "\nDue to Shodan account limits, this application can only return 100 results at a time. To view, press v, or q to quit.\n"

echo -e " "
read view

if [ $view == "v" ]
then echo "$(<results.txt )"
fi

if [ $view == "q" ]
then exit
fi