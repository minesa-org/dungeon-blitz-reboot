# Setup

<img src="/assets/ss.png" width="35rem" style="vertical-align: middle;">

## 1. Editing your `hosts` file

Add these to your `hosts` file depending on your OS.

### Windows 🟦

`Windows/System32/drivers/etc/hosts`

### Linux 🐧

`/etc/hosts`

### MacOS 🍎

`/private/etc/hosts`

```sh
127.0.0.1  www.dungeonblitz.com 
127.0.0.1  db.bmgstatic.com
```

## 2. Setting up [Python 3.xx](https://www.python.org/downloads/release/python-3135/)

## 3. Setting up Flashpoint

### [Windows 🟦](https://github.com/FlashpointProject/FlashpointComponentTools/releases/latest/download/FlashpointInstaller.exe)

### Linux 🐧

You can install Flaspoint via your distribution's package manager

```sh
yay -S flashpoint-launcher-bin
```

### MacOS 🍎

Run this on your terminal.

```sh
mkdir -p ~/Downloads && curl -fL https://download.flashpointarchive.org/upload/fp14.0.2_mac.txz | tar xC ~/Downloads
```

> [!IMPORTANT] 
> Skip the 4th step if you're not going to host the server yourself.

## 4. Setting up the server (Skip this step if you're not hosting)

- Run these commands

```sh
git clone https://github.com/minesa-org/flash-reboot 
cd flash-reboot\server
# Replace the forward slash with a backward one on linux/MacOS
sudo python main.py
```

You should have a server up and running after this step.

## 4.1 Inserting files inside Flashpoint

- Open up Flashpoint

- Go to `Config` and enable `Enable Editing`

- Go to `Curate` and click to `New Curation`

- Click open folder (As of writing this doesn't work on Linux/MacOS, you need to go to the directory yourself)

- Copy everything inside `server/content` to your game's folder click replace when asked.

- Tap to `Run`

> [!WARNING]  
> Flash 32 (which is the default) tends to not run on MacOS. You might try different flash versions if you're on MacOS. (e.g. `flashplayer11_9r900_152_win_sa_debug.exe` )

### Public Instances/Servers to join

```sh
# maybe later
```
