@echo off
start "C:\Program Files (x86)>start firefox.exe" http://localhost:8000
python -m http.server --directory docs
