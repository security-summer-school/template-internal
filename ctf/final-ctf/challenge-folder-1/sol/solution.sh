#!/bin/bash

HOST="141.85.224.108"
PORT=8001

if [[ $# -eq 0 ]]
then
    echo "Please provide at least one argument, \"local\" or \"remote\" depending on where you want to run the solution."
    echo "To run the solution for a different server, you can put \$1 = IP, \$2 = PORT."
fi

if [[ "$1" == "local" ]]
then
    url='http://127.0.0.1:'"$PORT"
elif [[ "$1" == "remote" ]] && [[ -z "$2" ]]
then
    url='http://'"$HOST"':'"$PORT"
else
    url="$1"':'"$2"
fi
