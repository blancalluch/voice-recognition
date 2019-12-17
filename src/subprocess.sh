#!/bin/bash
#applying sox filter to each audio
path=${1}
for file in $path
do
    bname=`basename $file`
    fname=`echo "$bname" | cut -d'.' -f1`
    outfile="../input_filtered/$fname.wav"
    outfile2="../input_processed/$fname.wav"
    #sox $file -r 24000 $outfile2
    sox $file -r 24000 $outfile 
    sox "$outfile" "$outfile2" compand .1,.2 -inf,-50.1,-inf,-50,-50 0 -80 .1 
    #lowpass 4000 gain 5 highpass 1000
done
