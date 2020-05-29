#!/usr/bin/env bash

check_params () {
    if [[ ! ${1+x} ]] || [[ ! ${2+x} ]]; then
        echo "Usage: hamming.sh <string1> <string2>"
        exit 1
    elif (( ${#1} != ${#2} )); then
        echo 'left and right strands must be of equal length'
        exit 1
    fi
}

main () {
    local output=0
    check_params "$@"
    if [ "${output}" = "0" ]; then
        for (( i=0; i<${#1}; i++ )); do
            [ "${1:$i:1}" != "${2:$i:1}" ] && let "output+=1"
        done
    fi

    echo "${output}"
}

main "$@"
