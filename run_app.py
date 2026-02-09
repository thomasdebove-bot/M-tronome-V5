from __future__ import annotations

import os

import uvicorn


def main() -> None:
    host = os.getenv("METRONOME_HOST", "0.0.0.0")
    port = int(os.getenv("METRONOME_PORT", "8090"))
    uvicorn.run("app:app", host=host, port=port)


if __name__ == "__main__":
    main()
