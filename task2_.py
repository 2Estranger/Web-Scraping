from task1_ import scrape_top_list
import json

file = open("task1_.json",'r')
data = json.load(file)
# print(data)

def group_by_year(movies):
    dict = {}
    for i in data:
        top_movie_list = []
        year = i['Year']
        # print(year)
        '''ALL YEAR WILL BE EXECUTED'''
        if year not in dict:
            for key in data:
                if year == key['Year']:
                    # print(year)
                    top_movie_list.append(key)
            dict[year] = top_movie_list
            # print(dict)
    with open("task2_.json","w") as f:
        json.dump(dict,f,indent = 4)
        a = json.dumps(dict)
group_by_year(movies = scrape_top_list())
