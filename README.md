# Setup and Development Guide

## Setup

1. Install [Git](https://git-scm.com/downloads)
2. Install [NVM](https://github.com/coreybutler/nvm-windows/releases)
3. Setup moken
  - Run `mkdir "C:\Program Files\moken" && copy moken.exe "C:\Program Files\moken\moken.exe"`
  - Add Environment Path : `C:\Program Files\moken`
4. Run `cpacker.exe` as admin

## Development

- Clone: `git clone https://github.com/LITTL3BEAR/code-packer.git`
- Install: `pip install -r requirements.txt`
- Build: `pyinstaller --onefile --name cpacker --distpath . main.py`
  
## Note

- npm run start