#!/bin/bash

clear

for file in $(ls *.ipynb)
do
        echo "vuoi convertire il file $file? "
        read risposta
        clear
        if [[ $risposta == "y" ]];then
                jupyter nbconvert --to pdf $file 
                echo "ho convertito in PDF il file $file
        else
                echo "arrivederci e grazie"
                exit
        fi
done
