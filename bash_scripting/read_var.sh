#!/usr/bin/env bash

#Script demonstrates how to read variables from terminal

echo "First Name:"
read first_name

echo "Last Name:"
read last_name

echo -e "Hallo $first_name $last_name\nDu bist Herr/ Frau $last_name"
