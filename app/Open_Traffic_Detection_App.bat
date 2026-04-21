@echo off
setlocal

cd /d "%~dp0"

rem Try a local virtual environment first if one exists.
if exist "%~dp0.venv\Scripts\python.exe" (
    "%~dp0.venv\Scripts\python.exe" -m streamlit run app.py --server.headless false
    goto :end
)

rem Fall back to the Windows Python launcher.
where py >nul 2>&1
if %errorlevel%==0 (
    py -3 -m streamlit run app.py --server.headless false
    goto :end
)

rem Fall back to python if py is not available.
where python >nul 2>&1
if %errorlevel%==0 (
    python -m streamlit run app.py --server.headless false
    goto :end
)

echo Python was not found on this computer.
echo Install Python and then install the app requirements first.
echo.
echo Example:
echo pip install -r requirements.txt
pause

:end
