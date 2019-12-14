#!/bin/bash

for file in ./input/*
do
    bname=`basename $file`
    fname=`echo "$bname" | cut -d'.' -f1`
    outfile="./input_filtered/$fname.wav"
    outfile2="./input_processed/$fname.wav"
    sox $file $outfile 
    sox "$outfile" "$outfile2" compand .1,.2 -inf,-50.1,-inf,-50,-50 0 -80 .1 lowpass 4000 gain 5 highpass 1000
done