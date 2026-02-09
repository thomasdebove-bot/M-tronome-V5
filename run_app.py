from __future__ import annotations

import os
import sys
import threading
import webbrowser
from pathlib import Path

import uvicorn


def main() -> None:
    exe_dir = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    sys.path.insert(0, str(exe_dir))
    host = os.getenv("METRONOME_HOST", "0.0.0.0")
    port = int(os.getenv("METRONOME_PORT", "8090"))

    def open_browser() -> None:
        webbrowser.open(f"http://127.0.0.1:{port}")

    threading.Timer(1.5, open_browser).start()
    uvicorn.run("app:app", host=host, port=port)


if __name__ == "__main__":
    main()
