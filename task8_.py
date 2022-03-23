# from task1_ import scrape_top_list
# import json
# import os
# import requests
# t1=scrape_top_list()
# with open("task1_.json","r+")as file:
#     a=json.load(file)
# def text():
#     for i in a:
#         path="/home/admin123/Desktop/WEB SCRAPING"+i["movieName"]+".text"
#         # path=""+i["movieName"]+".text"
#         if os.path.exists(path):
#             pass
#         else:
#             create=open("/home/admin123/Desktop/WEB SCRAPING"+i["movieName"]+".text","w")
#             # b=open(path,"w")
#             url=requests.get(i["moviceurl"])
#             create1=create.write(url.text)
#             create.close()
# text()



from urllib import request
from task1_ import scrape_top_list
import json
import os
import requests

t1 = scrape_top_list()
# print(t1)

with open("task1_.json", "r") as file:
    a = json.load(file)
    # print(a)
def text():
    for i in a[:10]:
        path = "/home/admin123/Desktop/WEB SCRAPING" + i["Movie_name"] + ".text"
        # print(path)
        path = "" + i["Movie_name"] + ".text"
        # print(path)
        
        if os.path.exists(path):
            pass
        else:
            create = open("/home/admin123/Desktop/WEB SCRAPING" + i["Movie_name"] + ".text" , "w")
            b = open(path, "w")
            url = requests.get(i["URL"])
            
            create1 = create.write(url.text)
            create.close()
            
            
                
text()