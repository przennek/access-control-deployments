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
- run ``./burn-image.sh`` (mac only), supply the name of the disk. See ``diskutil list`` to determine the 
  name of the disk for the SD card. Example: ``./burn-image.sh disk5``.
- make sure that your ssh keys are loaded via ``ssh-add``
- make sure rootfs ext4 partition is mounted, I use ```extFS for mac```.

## 3. Deploy ssh keys
- ``./deploy_ssh_keys.sh user@ip_address``
Use password supplied via ``userconf.txt`` file. 

## 4. Manual steps
### SSH into the machine:
- run ``raspi-config`` and enable legacy camera support
- run ``sudo rpi-update``
- run ``echo /opt/vc/lib/ | sudo tee /etc/ld.so.conf.d/vc.conf``
- run ``sudo ldconfig``
- run ``curl https://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -``
- run ``echo "deb https://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main" | sudo tee /etc/apt/sources.list.d/uv4l.list``
- run ``sudo apt-get update``

## 5. Run the ansible to finish the setup
- ``./deploy.sh <arch>``
supported archs are ``armv7`` and ``armv6`` but the latter was not tested and probably doesnt work.

## 6. Reboot