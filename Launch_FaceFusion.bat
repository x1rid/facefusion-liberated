@echo off
setlocal

set "ROOT=%~dp0"
set "PYTHON=%ROOT%miniconda3\envs\facefusion\python.exe"

title FaceFusion Liberated

if not exist "%PYTHON%" (
    echo ERROR: FaceFusion Python environment not found.
    pause
    exit /b 1
)

cd /d "%ROOT%"
"%PYTHON%" "%ROOT%launch_facefusion.py"

pause
