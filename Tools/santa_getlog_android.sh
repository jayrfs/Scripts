#!/bin/bash
mkdir -p ./logs
adb shell su -c dmesg > ./logs/dmesg_$(date +"%FT%T")_$USER.log
adb shell su -c cat /sys/fs/pstore/console-ramoops-0 > ./logs/ramoops_$(date +"%FT%T")_$USER.log
adb shell logcat -d > ./logs/logcat_$(date +"%FT%T")_$USER.log
