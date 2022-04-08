from bs4 import BeautifulSoup
import requests,json
def scrape_movie_cast(URL):
    req=requests.get(URL)
    shop=BeautifulSoup(req.text,"html.parser")
    main_d=shop.find("div",class_="castSection")
    d1=main_d.find_all("div",class_="cast-item media inlineBlock")
    d2=main_d.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    l=[]
    for i in d1:
        dic={}
        a=i.find("a")["href"][11:]
        dic["name"]=a
        l.append(dic)
    # print(l)
    for j in d2:
        dic1={}
        a1=j.find("a")["href"][11:]
        dic1["name"]=a1
        l.append(dic1)
    with open("task12_.json","w+") as file:
        json.dump(l,file,indent=4)
        return l
scrape_movie_cast("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")