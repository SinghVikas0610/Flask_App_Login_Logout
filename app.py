from flask import Flask , render_template, request
import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
save_dir="images/"
app = Flask(__name__)
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
@app.route('/')
def hello_world():
    query="akshay kumar"
    response=requests.get(f"https://www.google.com/search?q={query}&sca_esv=583632294&tbm=isch&sxsrf=AM9HkKk-SBcWfSjPaOWppYCj6j-3yvjckQ%3A1700321798255&source=hp&biw=1366&bih=651&ei=BtpYZeqtDZKo2roP9LSt2AU&iflsig=AO6bgOgAAAAAZVjoFkxcOaMm25SMH-XbLbN36Zs8BEuv&oq=&gs_lp=EgNpbWciACoCCAEyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCcyBxAjGOoCGCdIpA9QAFgAcAF4AJABAJgBAKABAKoBALgBA8gBAIoCC2d3cy13aXotaW1nqAII&sclient=img")
    soup=BeautifulSoup(response.content,'html.parser')
    images_tages=soup.find_all("img")
    del images_tages[0]
    for i in images_tages:
        images_url=i["src"]         # src and link is like key and value pair
        image_data=requests.get(images_url).content
        with open(os.path.join(save_dir,f"{query}_{images_tages.index(i)}.jpg"),"wb") as f:
            f.write(image_data)
    return None