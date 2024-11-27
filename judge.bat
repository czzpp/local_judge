@echo off
python .\GetTest.py %2 %4 %5
C:\\"Program Files (x86)"\\Embarcadero\\Dev-Cpp\\TDM-GCC-64\\bin\\g++.exe %1.cpp -o %1.exe -std=c++14 -O2 -Wall
%1.exe < %2 > %3
fc.exe %3 %4 > diff.txt
del %1.exe