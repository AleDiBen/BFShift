#!/bin/bash
#
# Author: @AleDiBen
#
# EXAMPLE:
#     ./bfhift.sh 'the encoded string'

for i in {0..5}
do
	for j in {1..50}
	do
		./shift.py -a $i -s $j -d "$1" >> results
	done
done
