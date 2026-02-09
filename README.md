# M-tronome-V5

## Build Windows executable (autonomous)

Prerequisites on a Windows build machine:
- Python 3.11+
- `pip install fastapi uvicorn pandas openpyxl pyinstaller`

Build:
```powershell
pyinstaller --onefile --name M-tronome-V5 --collect-all pandas --hidden-import pandas._libs.tslibs.timedeltas run_app.py
```

Run:
```powershell
.\dist\M-tronome-V5.exe
```

Optional environment variables:
- `METRONOME_HOST` (default `0.0.0.0`)
- `METRONOME_PORT` (default `8090`)
