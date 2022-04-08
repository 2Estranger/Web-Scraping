from task4_ import movie_details
from task12_ import scrape_movie_cast
import json
l=[]
url=("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")

def scrape_cast():
    details= movie_details(url)
    cast=scrape_movie_cast(url)
    details["cast"]=cast
    l.append(details)
    with open("task13_.json","w") as f1:
        json.dump(l,f1,indent=4)
scrape_cast()