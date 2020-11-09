#!/usr/bin/env bash

main () {
  ACRONYM=''
  WORDS="${1//[_*-]/ }"
  for word in $WORDS
  do
    ACRONYM=$ACRONYM${word:0:1};
  done

  echo $(tr a-z A-Z <<< $ACRONYM);
}

main "$@"
