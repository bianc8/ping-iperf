#!/bin/bash
for i in {1..15}
do
    echo "TTL $i"
    ping -t "$i" -c 1 88.80.187.84
done