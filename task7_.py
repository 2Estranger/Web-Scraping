from task5_ import get_movie_list_details
import json
movie_list = get_movie_list_details()
def movies_language():
    lan_list=[]
    for i in movie_list:
        if "Director" in i:
    
            for j in i["Director"]:
                lan_list.append(j)
        lan_dict={}
        for i in lan_list:
            if i in lan_dict:
                lan_dict[i]=lan_dict[i]+1
            else:
                lan_dict[i]=1
    with open("task7_.json","w") as file:
        json.dump(lan_dict, file, indent = 4)
movies_language()