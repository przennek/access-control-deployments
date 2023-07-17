#!/bin/bash

if [ -z "$1" ]; then
  echo "usage: ./burn-image.sh [disk_name], e.g. ./burn-image.sh disk4"
else
  echo "Burning the SD card"
  sudo diskutil unmountDisk /dev/"$1" &&
      diskutil eraseDisk ExFAT temp "$1" &&
      diskutil unmountDisk /dev/"$1" &&
      echo "Copying the RaspiOS to the $1" &&
      sudo dd bs=4m if=config/raspios.img of=/dev/r"$1" &&
      # workaround to make sure the disk is already mounted
      diskutil unmountDisk /dev/"$1" &&
      diskutil mountDisk /dev/"$1" &&
      echo "Copying and creating necessary files on bootfs" &&
      cp config/userconf.txt /Volumes/bootfs/ &&
      cp config/wpa_supplicant.conf /Volumes/bootfs/ &&
      touch /Volumes/bootfs/ssh &&
      diskutil unmountDisk /dev/"$1"
fi