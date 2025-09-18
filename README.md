RemoveWatermarkPro - Ready-to-build repo for Windows 64-bit installer
================================================================

Important: I cannot produce a Windows .exe installer from this environment due to cross-compilation and runtime limitations.
Instead, this repository is fully prepared so you can build locally or via GitHub Actions (the workflow included will produce a Windows installer automatically when pushed to 'main').

How to build locally on Windows:
1. Clone or extract this repo on a Windows machine.
2. Install Python 3.10+, Node.js 18+, and Git, and ensure ffmpeg is in PATH.
3. In backend/: create venv and pip install -r requirements.txt
4. In electron/: run 'npm ci' then 'npm run dist' (this uses electron-builder to produce an NSIS installer .exe).
5. Alternatively, push to GitHub and trigger the included GitHub Actions workflow to build on windows-latest runner and download artifact from Actions.

Note on legality: only remove watermarks for content you own or have rights to modify.
