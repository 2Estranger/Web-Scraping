from bs4 import BeautifulSoup
from task5_ import get_movie_list_details
import json

language = get_movie_list_details()

def movies_language(movie_list):
    dict = {}
    for i in movie_list:
        if "Original Language" in i:
            Language = i["Original Language"]
            # print(Language)
            
            if Language not in dict:
                Language = i["Original Language"]
                dict[Language] =1
            else:
                dict[Language] += 1

    print(dict)
    
    with open("task6_.json", "w") as f:
        json.dump(dict, f, indent = 4)
            
            
movies_language(language)