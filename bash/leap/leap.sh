#!/usr/bin/env bash

declare usage="Usage: leap.sh <year>"

function main () {
  YEAR=$1
  RES=''
  if ! [[ "$YEAR" =~ ^[0-9]+$ ]] || (($2)) || ! (($1))
    then
      echo $usage;
      exit 1;
  fi

  #if [[ $(($YEAR % 4)) = 0 ]]
  if ! (($YEAR % 4))
  then
    if ! (($YEAR % 100))
    then
      if ! (($YEAR % 400))
      then
        RES='true';
      else
        RES='false';
      fi
    else
      RES='true';
    fi
  else
    RES='false';
  fi

  echo $RES;
}

main "$@"
