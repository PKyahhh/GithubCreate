@echo off

cd \
cd YOUR PATH
echo Readme >> README.md
set begin=%1
python create.py %begin%
