import json
from task1_ import scrape_top_list
from task4_ import movie_details

with open("task1_.json","r")as file:
    data = json.load(file)
    
# movies=scrape_top_list()

def get_movie_list_details():
    list = []
    for i in data[:50]:
        a= i["URL"]
        b = movie_details(a)
        list.append(b)
    with open ("task5_.json", "w+") as f:
        json.dump(list, f, indent=4)
    return list
get_movie_list_details()