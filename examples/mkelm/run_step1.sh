#!/bin/bash

#awk -v elem=$1 '{if($1==elem){print $0}}' table.txt
Xx=`awk -v elem=$1 '{if($1==elem){print $1}}' table.txt`
addor=`awk -v elem=$1 '{if($1==elem){print $2}}' table.txt`
adde=`awk -v elem=$1 '{if($1==elem){print $3}}' table.txt`
remor=`awk -v elem=$1 '{if($1==elem){print $4}}' table.txt`
remne=`awk -v elem=$1 '{if($1==elem){print $5}}' table.txt`
echo ${Xx}" "${addor}" "${adde}" "${remor}" "${remne}

cp step1_Xx.elm.py step1_$1.elm.py

sed -i "s/Xx/${Xx}/g" step1_$1.elm.py
sed -i "s/addor/${addor}/g" step1_$1.elm.py
sed -i "s/adde/${adde}/g" step1_$1.elm.py
sed -i "s/remor/${remor}/g" step1_$1.elm.py
sed -i "s/remne/${remne}/g" step1_$1.elm.py

python step1_$1.elm.py
rm -f -r step1_$1.elm.py

