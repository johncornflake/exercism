#!/usr/bin/env bash

declare greetee=$1
declare usage="Usage: ./error_handling <greetee>"

main () {
    if [ ${#@} != 1 ]; then
        echo ${usage}
    else
        echo "Hello, ${greetee}"
    fi
}

main "$@"
