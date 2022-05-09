#!/bin/bash
for i in {51..1500..50}
do
    echo "ping $i"
    ping -s "$i" -c 100 -M dont 88.80.187.84 > "results/$i.txt"
done