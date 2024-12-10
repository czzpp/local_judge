python3 GetTest.py $2 $4 $5 \
&& g++ $1.cpp -O2 -Wall -std=c++14 -o $1 \
&& ./$1 < $2 > $3 \
&& diff $3 $4 > diff.txt \
&& rm $1
