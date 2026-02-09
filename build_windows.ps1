$ErrorActionPreference = "Stop"

Write-Host "==> Creating build environment"
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Write-Host "==> Installing dependencies"
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn pandas openpyxl pyinstaller

Write-Host "==> Building standalone EXE"
pyinstaller --onefile --name M-tronome-V5 --collect-all pandas --hidden-import pandas._libs.tslibs.timedeltas run_app.py

Write-Host "==> Build complete: .\dist\M-tronome-V5.exe"
