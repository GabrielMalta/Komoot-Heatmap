import pyautogui as pag
from time import sleep
import os

if pag.size()[1] != 2160:
    print("Single monitor setup, aborting")
    exit(-1)

# clear all downloaded files
os.system("rm gpx/*")

sleep(5)
pag.write('\t\t\t\t\t\t') #setup

for i in range(10):
    #next tour
    pag.press('tab', 4)
    # for _ in range(4): pag.press('tab')
    pag.press('enter')
    sleep(10)

    #press download button
    pag.click(1292, 1725)
    sleep(3)

    #press save
    pag.press('enter')

    #previous page
    pag.keyDown('alt')
    pag.press('left')
    pag.keyUp('alt')

    for _ in range(22): pag.press('tab')

    exit(0)
    print("hello")
