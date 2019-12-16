#!/bin/bash
path=${1}
if [ "$path" == "./input/*" ] 
then
    for file in $path
    do
        bname=`basename $file`
        fname=`echo "$bname" | cut -d'.' -f1`
        outfile="./input_filtered/$fname.wav"
        outfile2="./input_processed/$fname.wav"
        sox $file -r 24000 $outfile 
        sox "$outfile" "$outfile2" compand .1,.2 -inf,-50.1,-inf,-50,-50 0 -80 .1 
        #lowpass 4000 gain 5 highpass 1000
    done
else
    for file in $path
    do
        bname=`basename $file`
        fname=`echo "$bname" | cut -d'.' -f1`
        outfile="./audio_received/$fname.wav"
        outfile2="./audio_processed/$fname.wav"
        #sox $file $outfile 
        sox "$outfile" "$outfile2" compand .1,.2 -inf,-50.1,-inf,-50,-50 0 -80 .1 lowpass 4000 gain 5 highpass 1000
        echo "perfeee"
    done 
fi