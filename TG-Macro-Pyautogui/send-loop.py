#!/bin/python3
import pyautogui, pyperclip, time
from alive_progress import alive_bar

pyperclip.copy("😩👌")

for i in range(2,0,-1):
    print(f"starting in {i} seconds")
    time.sleep(1)

with open('commands.txt','r') as f:
    num_lines = sum(1 for line in f)
    print(f"total number of lines = {num_lines}")
    
with open('commands.txt','r') as f:
    with alive_bar(num_lines) as bar:
        for line in f:
            print(f"sending {line}")
            #pyautogui.hotkey("ctrl", "v")
            to_be_typed = f" /stop {line}"
            pyautogui.write(to_be_typed)
            pyautogui.press('enter')
            time.sleep(2)
            bar()