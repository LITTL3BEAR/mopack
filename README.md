# Mopack

MO project code pack for deploy to production.


## Setup

1. Install [Git](https://git-scm.com/downloads)
2. Install [NVM](https://github.com/coreybutler/nvm-windows/releases)
3. Clone Repo
  ```bash
  git clone https://github.com/LITTL3BEAR/code-packer.git
  ```
4. Copy **moken.exe**
  ```bash
  mkdir "C:\Program Files\moken" && copy moken.exe "C:\Program Files\moken\moken.exe"
  ```
5. Add Environment Path : `C:\Program Files\moken`
6. Run **mopack.exe** as admin


## Build

1. Install pyinstaller
  ```bash
  pip install pyinstaller
  ```
2. Run Build
  ```bash
  pyinstaller --onefile --name mopack --distpath . mopack.py
  ```
