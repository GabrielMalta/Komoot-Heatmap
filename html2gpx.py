from bs4 import BeautifulSoup
import pyautogui as pag
import pyperclip as clip
from time import sleep
import os


with open("tours.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

tours = soup.find_all("a", {"data-test-id":"tours_list_item_title"})
url_list = ["https://www.komoot.com" + tour.get("href") + "/download" for tour in tours]
tour_id = [url.split("/")[-2] for url in url_list]
already_downloaded = [filename.split("_")[1] for filename in os.listdir("gpx")]

# clear all downloaded files
# os.system("rm gpx/*")
sleep(5)


for url,tour_id in zip(url_list, tour_id):

    if tour_id in already_downloaded:
        continue

    clip.copy(url)
    pag.hotkey('ctrl','t')
    pag.hotkey('ctrl','v')
    pag.press('enter')