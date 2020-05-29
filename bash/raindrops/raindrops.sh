#!/usr/bin/env bash

INPUT=$1
output=""

raindrops () {
    [ $(( $INPUT % 3 )) = 0 ] && output+="Pling"
    [ $(( $INPUT % 5 )) = 0 ] && output+="Plang"
    [ $(( $INPUT % 7 )) = 0 ] && output+="Plong"
    [[ $output = ""  ]] && output=$INPUT
}

main () {
    if [ -z "${1}" ]; then
        echo "no number given, you idiot."
        exit
    fi

    raindrops "$1"
    echo $output
}

main "$@"
