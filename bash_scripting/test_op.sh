#!/usr/bin/env bash

#Script that demonstrates test operations and if/elif/else

echo "Username:"
read -r input_name

if [ "${input_name,,}" = johnian ]
then
	echo "Welcome Big Boss Man"
	echo "Passcode:"
	read -rs input_code
	if [ "$input_code" -eq 8800 ]
	then
		echo "Wilkommen, gut Sir"
	else
		echo "Naaah"
	fi

elif [ "${input_name,,}" = help ]
then
	echo "No one to save you huuh!"

else
	echo "Tief Mann, wa ya doin here"
fi
