#!/usr/bin/env bash

# Installs youtube-dl to /usr/local/bin/youtube-dl
# Sets up directories and files required by music_fetcher but ignored by git

# Must run as root
if [ "$EUID" -ne 0 ]; then
    echo "> [ERROR]: Must be run as root."
    exit
fi

# Install youtube-dl
echo "> [INFO]: Installing youtube-dl to /usr/local/bin/youtube-dl"
wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
chmod a+rx /usr/local/bin/youtube-dl
echo "> [INFO]: Upgrading youtube-dl with any available updates."
sudo -H pip install --upgrade youtube-dl

# Add sources files ignored by git
if [ ! -d "downloaded" ]; then
    echo "> [INFO]: Creating downloaded directory."
    mkdir downloaded
fi

if [ ! -e "downloaded/sources" ]; then
    echo "> [INFO]: Creating sources file."
    touch sources
fi

echo "> [SUCCESS]: music_fetcher installed successfully."