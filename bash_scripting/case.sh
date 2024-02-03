#!/usr/bin/env bash

#Script that impements case statements

echo "Enter your username:"
read -r input_name

case ${input_name,,} in

	johnian)
		echo "Ooh der richtige Man kommt an!"
		echo "Bitte Schreiben das Passwort"
		read -sr input_code
		case $input_code in
			8800)
				echo "Willkommen Gute Herr"
				;;
			*)
				echo "Nein, nein, Sie sind nicht erlaubt"
		esac
		;;
	help)
		echo "Schade, du bist allein"
		;;
	*)
		echo "Was machst du hier"
esac
