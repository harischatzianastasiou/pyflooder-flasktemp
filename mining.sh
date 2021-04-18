#!/bin/sh

$SNAP/bin/mining.py &
$SNAP/bin/flasktemp.py $1 $2
P1=$!
P2=$!
wait $P1 $P2
