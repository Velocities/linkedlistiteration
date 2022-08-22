@echo off
if exist results.txt (
    del results.txt
)
python main.py
python second.py
