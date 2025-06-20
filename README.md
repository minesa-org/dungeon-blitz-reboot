# 🏰 Dungeon Blitz - Flash Reboot

> Play Dungeon Blitz on your own computer — Flash is dead, but the game lives on.

## ⚡ What is this?

This repo lets you run **Dungeon Blitz**, the classic browser MMO, directly on your machine using **Flash emulator**. 

## 🖥 Required Local Servers

1. Go to:
  - Edit hosts file
```bash
Windows/System32/drivers/etc/hosts
```
2. Add these:
```bash
127.0.0.1  www.dungeonblitz.com 
127.0.0.1  db.bmgstatic.com
```

3. To make the game connect and function, you must run two scripts:
```bash
python server/main.py

python server/PolicyServer.py
```

4. Now Open FlashPoint (If you are having bugs/issues, try opening as Administrator):
  - Go to "Config" Tab on the Top Left navigation menu
  - Enable Editing 
  - Go to Curation
  - Create a curation
  - Fill required inputs
  - Open folder of curation
  - Replace all files & folders with what is inside of `game-files` folder
  - Launch Command:
  ```bash
  http://db.bmgstatic.com/p/cbv/DungeonBlitz.swf?fv=cbq&gv=cbv
  ```
  - Download [flashplayer-debugger/flashplayer32_0r0_465_sa_debug.exe](https://github.com/AngelMako/flash-reboot/blob/main/flashplayer-debugger/flashplayer32_0r0_465_sa_debug.exe) (Recommended version)

Example Config File:
![image](https://github.com/user-attachments/assets/6e730d36-bb72-4ddd-b2d5-aba4e304715c)

Enjoy! ✌🏻🥳

---

## 📁 Folder Structure

```bash
flash-reboot/
├── flashplayer-debugger/        # Flash Player
├── game-files/                  # SWF files and original assets of Dungeon Blitz (you need to use modified version of DungeonBlitz.swf)
├── server/                      # Scripts to start the game
└── README.md                    # This file
```

### 🧰 Requirements

- Windows PC (macOS/Linux not supported by Flashpoint)
- Flashpoint Infinity
- Terminal
- Python

### 📜 Legal Notice

This project is for **archival** and **educational purposes**. All assets belong to their original creators. We do not monetize, alter, or distribute copyrighted material.

If you're the rights holder and want this removed, open an issue.

### 🤝 Contributing

Have fixes or improvements? PRs are welcome. Check `docs/CONTRIBUTING.md` for more info (coming soon)
