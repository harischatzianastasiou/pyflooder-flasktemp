#!/bin/sh

snap/bin/mining-flasktemp/mining.py &
snap/bin/mining-flasktemp/flasktemp.py
P1=$!
P2=$!
wait $P1 $P2
