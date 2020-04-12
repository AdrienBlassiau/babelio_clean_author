#!/bin/bash

cat res.txt >> data/data.txt && sort data/data.txt | uniq > tmp/data_tmp.txt && cat tmp/data_tmp.txt >data/data.txt