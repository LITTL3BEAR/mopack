## SETUP
1. install Git (https://git-scm.com/downloads)
2. install NVM (https://github.com/coreybutler/nvm-windows/releases)
3. setup moken
  - run CMD as admin
  - mkdir "C:\Program Files\moken" && copy moken.exe "C:\Program Files\moken\moken.exe"
  - setx /M path "%path%;C:\Program Files\moken"
4. run CodePacker.exe as admin

## DEV
- pip install -r requirements.txt
- pyinstaller --onefile --name CodePacker --distpath . main.py
