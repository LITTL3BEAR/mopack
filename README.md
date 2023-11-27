# Pack code for deploy

This document outlines the steps to pack code prepare for deploy on prod.

## Setup 

1. Install [Git](https://git-scm.com/downloads)
2. Install [NVM](https://github.com/coreybutler/nvm-windows/releases)
3. Setup moken
  ```bash
  mkdir "C:\Program Files\moken" && copy moken.exe "C:\Program Files\moken\moken.exe"
  ```
4. Add moken Environment Path : `C:\Program Files\moken`
5. Run `mopack.exe` as admin

## Development

1. Clone: `git clone https://github.com/LITTL3BEAR/code-packer.git`
2. Install
  ```bash
  pip install -r requirements.txt
  ```
3. Build
  ```bash
  pyinstaller --onefile --name mopack --distpath . main.py
  ```
