#!/bin/bash
for i in {1..10}
do
    iperf -c 88.80.187.84 -p 22088
done