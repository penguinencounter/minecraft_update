# Minecraft (server) auto-updater

## Install
To install the server, you need Anaconda (Python 3.x).
Download from `https://www.anaconda.com/distribution/`.

To automatically fetch the server software, run `python download.py`. This will make 2 requests to `minecraft.net` and `launcher.mojang.com` to find the server software.

Instructions for starting the server can be found on the [Minecraft website](https://www.minecraft.net/en-us/download/server).

## Cron
Use `cron` and `crontab` to schedule automatic updates:
`crontab -e  # you may be asked to choose an editor`

Add `[minute] [hour] * * 1 python3 /absolute/path/to/download.py` for a weekly update.

That's all!
