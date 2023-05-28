@echo off

REM This script will install the required packages from requirements.txt

echo Starting the installation process...

for /F "delims=#" %%i in (requirements.txt) do (
    echo Installing %%i...
    pip install %%i
    if errorlevel 1 (
        echo An error occurred during the installation of %%i.
        echo Please make sure you have pip installed and try again.
    ) else (
        echo Successfully installed %%i.
    )
)

echo Installation process completed.

pause
