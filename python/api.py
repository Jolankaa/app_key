
import json
import asyncio
from flask import Flask, request
from scraping import scrapheaal,request,filter_end,filter_start
from datetime import timedelta
from requests import get



app=Flask(__name__)
@app.route("/")
def index():

 return "Lavander Api Hoşgeldiniz"
 

@app.route("/haberler")
def indexx():

 return scrapheaal()

@app.route("/enyuksek")
def indexxx():

 return request(filter_start(),filter_end())


@app.route("/depremler")
def depremler():
    r = get("https://api.orhanaydogdu.com.tr/deprem/live.php?limit=100") # orhanaydogdu special thx 
    return json.loads(r.content)

if __name__=="__main__":
 app.run(debug=True)










