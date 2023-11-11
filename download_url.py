import os
import requests


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR , exist_ok=True)
DOWNLOAD_IMGPATH = os.path.join(DOWNLOADS_DIR,"img1.jpg")
url ='https://imgs.search.brave.com/_WeRILENZZFx6eKV9kucdS5BKhWdlAmvtWsy2flVs8o/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTI5/NzE1OTM2NS9waG90/by9wb3J0cmFpdC1v/Zi15b3VuZy1zbWls/aW5nLXdvbWFuLWZh/Y2UtcGFydGlhbGx5/LWNvdmVyZWQtd2l0/aC1mbHlpbmctaGFp/ci1pbi13aW5keS1k/YXktc3RhbmRpbmcu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PUkxNmNfWnpRSEVl/R29QVVZyVlA5cFB1/c1N6c215bXZWS2RR/VmdQdVZkRG89'

r =requests.get(url, stream=True)
r.raise_for_status() #if not 200 raise error

with open(DOWNLOAD_IMGPATH, 'wb') as f:
    f.write(r.content)
    
