import json
from task5_ import get_movie_list_details
movies_d = get_movie_list_details()
with open("task5_.json","r") as b:
   moviess_d= json.load(b)
def analyse_language_and_directors():
    dic={}
    director_list=[]
    for i in movies_d:
        for j in i['Director']:
            if j not in director_list:
                director_list.append(j) 
    for x in director_list:
        dict={}
        for y in movies_d:
            if x in y['Director']:
                if "Original Language" in y:
                    a=y["Original Language"]
                    for g in a:
                        if g in dict:
                            dict[g]=dict[g]+1
                        if g not in dict:
                            dict[g]=1
                    dic[x]=dict
    with open ("task10_.json","w+") as f:
        json.dump(dic,f,indent=4)    
    return dic 

analyse_language_and_directors()