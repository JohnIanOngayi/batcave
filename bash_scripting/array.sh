#!/bin/bash

#Script demonstrates how to define and print elements of an array

my_array=( 1 2 3 4 5 6 )

#Print first element
echo ${my_array[0]}

#Print second element
echo ${my_array[1]}

#Print all elements
echo ${my_array[*]}
echo ${my_array[@]}

#Iterate using a for loop
for item in ${my_array[@]}
do
	echo "${item}"
done
