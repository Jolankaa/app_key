import requests
from bs4 import BeautifulSoup
from datetime import datetime , timedelta
import requests
import json
from urllib.request import urlopen
import re
import socket
import random

def dns_query():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    dns_data = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
    
    return dns_data

def dns_api(ip):
    url = "http://ip-api.com/json/{}".format(ip)
    request_value = requests.get(url)
    data = json.loads(request_value.text)
    array = str(data['city'])
    array = array.upper()
    
    return array

def filter_end():
    from datetime import date 
    ini_time_for_now = date.today()

    return ini_time_for_now

def filter_start():
    from datetime import date 
    ini_time_for_now = date.today()

    bir_gün_öncesi = ini_time_for_now - \
                    timedelta(days= 1)
    
    return str(bir_gün_öncesi)
    

def request(start,end):
    url = f"https://api.orhanaydogdu.com.tr/deprem/live.php?limit=100"
    request_value= requests.get(url,)
    data = json.loads(request_value.text)
    
    dosya_adı_seçmek_için_sayı = random.randint(1,9999)
    json_zaman = str(filter_end())


    dosya_adi = "{}{}.json".format(json_zaman,dosya_adı_seçmek_için_sayı)
    array_sayısı = int(len(data['result']))

    with open("data/{}".format(dosya_adi),"w" ,encoding="utf-8") as json_value:
        json_value.write(str(data))

    with open("data/{}".format(dosya_adi),"r",encoding="utf-8") as data_value:
        api_read = json.dumps(data_value.read())
    
    yikicilik_list = []

    for i in range (0,array_sayısı):
       
        array = (data['result'])
        print(array[i])
        yikicilik = (array[i]['mag'])
        yikicilik_list.append(yikicilik)
        
        
        
    sonuc = max(yikicilik_list)   
    ind = yikicilik_list.index(sonuc)
    
    res = data['result']
    return res[ind]

def scrapheaal():
 header = {

    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
   
}

 resim_url = "https://heaal.meb.k12.tr"
 r = requests.get("https://heaal.meb.k12.tr/tema/icerik.php?KATEGORINO=94501" ,headers=header)
 source = BeautifulSoup(r.content,"lxml")

 haberler = source.find_all("div",attrs={"class","col-sm-10"}, limit=2)

 haber1 = source.select("#liste > div:nth-child(2) > div.row > div.col-sm-8 > p")
 haber2 = source.select("#liste > div:nth-child(3) > div.row > div.col-sm-8 > p")
 haber3 = source.select("#liste > div:nth-child(4) > div.row > div.col-sm-8 > p")

 baslik1 = source.select("#liste > div:nth-child(2) > div:nth-child(1) > div.liste_baslik > a")
 baslik2 = source.select("#liste > div:nth-child(3) > div:nth-child(1) > div.liste_baslik > a")
 baslik3 = source.select("#liste > div:nth-child(4) > div:nth-child(1) > div.liste_baslik > a")


 resim1 = source.select("#liste > div:nth-child(2) > div.row > div.col-sm-4 > a > img")
 resim2 = source.select("#liste > div:nth-child(3) > div.row > div.col-sm-4 > a > img" )
 resim3 = source.select("#liste > div:nth-child(4) > div.row > div.col-sm-4 > a > img" )

 resim1_url = resim_url + resim1[0]['src']
 resim2_url = resim_url + resim2[0]['src']
 resim3_url = resim_url + resim3[0]['src']

 json_data = {
 
  "data": [
    {"haber": haber1[0].text, "baslik": baslik1[0].text , "resim" : resim1_url},
    {"haber": haber2[0].text, "baslik": baslik2[0].text , "resim" : resim2_url},
    {"haber": haber3[0].text, "baslik": baslik3[0].text , "resim" : resim3_url}
  ],
   
   "author": "LavanderProjects",
   "status": "success"
}
 return json_data


