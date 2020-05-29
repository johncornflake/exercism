#!/usr/bin/env bash

NAME=${1:-you}
main () {
    echo "One for $NAME, one for me."
}

main "$@"
