#!/usr/bin/env bash

main () {
  NUM=$1
  LEN=${#NUM}
  SUM=0
  for (( i=0; i < ${LEN}; i++ ));
  do
    SUM=$(( $SUM + ${NUM:i:1} ** ${LEN} ));
  done;

  if [[ $SUM = $NUM ]]
  then
    echo "true"
  else
    echo "false"
  fi;
}

main "$@"
