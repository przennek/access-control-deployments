# How to run this [MAC]

# Deployment

## 1. Create ./config directory and insert the following files:
- raspios.img - download newest version from https://www.raspberrypi.com/software/
- authorized_keys - generate ssh keys and paste public key into this file
- userconf.txt - https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/computers/configuration/headless.adoc
- wpa_supplicant.conf:
    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=PL

    network={
        ssid="SSID"
        psk="PASSWORD"
    }
    ```            

## 2. Burn the image on the SD card
- run ./burn-image.sh (on mac), supply the name of the disk. See ``diskutil list`` to determine the 
  name of the disk for the SD card. Example: ``./burn-image.sh disk5``.
- make sure that your ssh keys are loaded via ``ssh-add``
- make sure rootfs ext4 partition is mounted, I use ```extFS for mac```.

## 3. Run the ansible to finish the setup
- ``./enable_ssh_keys.sh user@ip_address``
- ``./deploy.sh <arch>``

You will be asked for the user password **once**. After the user and group is set by```hch.sh``` 
the ssh key will be used. After this single execution of ```hch.sh```, it won't have to be executed anymore.

## 4. Manual steps
### SSH into the machine:
- run ``raspi-config`` and enable legacy camera support
- run ```systemctl --user enable pulseaudio```
- run ```systemctl --user start pulseaudio```
- run ./bin/install_uv4l.sh

#TODO Automate
1.
sudo vim /etc/bluetooth/main.conf
ControllerMode = le

2.
vim "/etc/uv4l/uv4l-raspicam.conf"

server-option = --port=8001
server-option = --use-ssl=yes
server-option = --ssl-private-key-file=/home/pc/app/ssl_certificates/server.key
server-option = --ssl-certificate-file=/home/pc/app/ssl_certificates/server.crt