@echo off
if exist results.txt (
    del results.txt
    main.py
    second.py
) else (
    main.py
    second.py
)