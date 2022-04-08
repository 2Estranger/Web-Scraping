from task5_ import get_movie_list_details
import json

genre = get_movie_list_details()

def analyse_genre():
    dict = {}
    genre_list = []
    for i in genre:
        if "Gerne" in i:
            m = i["Gerne"]
            # print(m)
            
            for j in m:
                if j not in dict:
                    dict[j] = 1
                else:
                    dict[j] += 1
    print(dict)
    
    
    with open("task11_.json","w+") as file:
        json.dump(dict, file, indent = 4)
    return dict
analyse_genre()