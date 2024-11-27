python GetTest.py $2 $4 $5 &\
g++ $1.cpp -o $1 -std=c++14 -O2 -Wall &\
./$1 < $2 > $3 &\
diff $3 $4 > diff.txt &\
rm $1