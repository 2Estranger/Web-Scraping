import json 
import requests
from bs4 import BeautifulSoup
with open("task1_.json","r") as f:
    data=json.load(f)
# print(data)  
dic={"1937":[],"1947":[],"1957":[],"1967":[],"1977":[],"1987":[],"1997":[],"2007":[],"2017":[],"2027":[]}

def decade_by_year(data):
    for i in data:
        if i["Year"]>=1937 and i["Year"]<=1947:
            dic["1937"].append(i)
        elif i["Year"]>=1947 and i["Year"]<=1957:
            dic["1947"].append(i)
        elif i["Year"]>=1957 and i["Year"]<=1967:
            dic["1957"].append(i)
        elif i["Year"]>=1967 and i["Year"]<=1977:
            dic["1967"].append(i)
        elif i["Year"]>=1977 and i["Year"]<=1987:
            dic["1977"].append(i)
        elif i["Year"]>=1987 and i["Year"]<=1997:
            dic["1987"].append(i)
        elif i["Year"]>=1997 and i["Year"]<2007:
            dic["1997"].append(i)
        elif i["Year"]>=2007 and i["Year"]<=2017:
            dic["2007"].append(i)
        elif i["Year"]>=2017 and i["Year"]<=2027:
            dic["2017"].append(i)
#            
    # print(dic)   
    with open("task3_.json","w+") as file:
        json.dump(dic,file,indent=4)    

decade_by_year(data)