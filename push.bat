@echo off
git add .
git commit -m '%date%-commit'
git push origin master
timeout 4