from task5_ import get_movie_list_details
import os
import json
import time
import random
with open("task5_.json","r+") as file:
    a = json.load(file)
def text():
    b = random.randint(1,3)
    print(b)
    for i in a:
        path = "/home/admin123/Desktop/WEB SCRAPING/task9_/task9"+i["Name"]+".json"
        print(path)
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w")
            json.dump(i,create,indent=4)
        time.sleep(b)
text()