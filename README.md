# How to run this

## 1. Create ./config directory and insert the following files:
- raspios.img - download newest version from https://www.raspberrypi.com/software/
- authorized_keys - generate ssh keys and paste public key into this file
- userconf.txt - https://github.com/raspberrypi/documentation/blob/develop/documentation/asciidoc/computers/configuration/headless.adoc
- wpa_supplicant.conf
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

## 3. Manual steps
### SSH into the machine using the login and password from userconf and:
- create ``~/.ssh/authorized_keys``
- run ``raspi-config`` and enable legacy camera support 

## 4. Setup the streaming server
- ``cd survilance-unit``
- ``ansible-playbook -i production server.yml``

## 5. Just run the server (after install and restart)
``ansible-playbook -i production server.yml --tags run``