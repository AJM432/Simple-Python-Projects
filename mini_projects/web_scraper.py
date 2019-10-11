#! python3
# web_scraper.py

import webbrowser as wb
import pyperclip as pclip

adress = pclip.paste()


wb.open('https://www.google.com/maps/place/' + adress)

# wb.open('https://www.reddit.com/r/meditation/')
# wb.open('https://www.reddit.com/r/luciddreaming/')
# wb.open('https://www.reddit.com/r/awakened/')

# 21 bologna rd
