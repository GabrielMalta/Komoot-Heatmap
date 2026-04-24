#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 16:23:42 2022

Original author: Nishad Mandlik

line Edited on 2026-03-10 by GabrielMalta
"""

from getpass import getpass
from komPYoot import API, TourType, TourStatus, Sport, TourOwner
from time import sleep
import os

_DOWNLOAD_DIR = "./gpx"


def main():
    print("Please enter your Komoot account credentials.")

    email_id = input("Email ID: ")
    password = getpass("Password (hidden input): ")

    a = API()
    a.login(email_id, password)

    # Get list of tours with the given filters
    tours = a.get_user_tours_list(tour_type=TourType.RECORDED)

    already_downloaded = []

    if not os.path.exists(_DOWNLOAD_DIR):
        os.makedirs(_DOWNLOAD_DIR)
    for f in os.listdir(_DOWNLOAD_DIR):
        if f.endswith('.gpx'):
            already_downloaded.append(f.split(".")[0].split("_")[0])

    # Get the ID of the first tour in the list
    for tour in tours:
        tour_id=tour["id"]

        if str(tour_id) in already_downloaded: continue
        
        file_name = a.download_tour_gpx(tour_id, _DOWNLOAD_DIR)
        os.rename(os.path.join(_DOWNLOAD_DIR,file_name), os.path.join(_DOWNLOAD_DIR,str(tour_id)+'.gpx'))
        print(tour_id)

    return


if __name__ == '__main__':
    tours = main()
