#!/usr/bin/env bash

#Script demonstartes how positional arguments are fed in bash

#Fetch first pos-arg
echo "$1"

#Fetch second pos-arg
echo "$2"

#Fetch third pos-arg
echo "$3"

#Fetch all pos-args
echo "$*"
echo "$@"

#Fetch no. of pos-args
echo "$#"
