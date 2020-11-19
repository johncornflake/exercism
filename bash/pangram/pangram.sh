#!/usr/bin/env bash

main () {
  local alphabet=("a b c d e f g h i j k l m n o p q r s t u v w x y z")
  local input=$(echo $1 | sed 's/[^a-zA-Z]//g' | tr '[:upper:]' '[:lower:]')
  local is_pangram='true'

  for a in $alphabet
  do
    if [[ $input != *"$a"* ]]
    then
      is_pangram='false'
      break
    fi;
  done;

  echo $is_pangram

}

main "$@"
