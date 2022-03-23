from bs4 import BeautifulSoup
import requests
import json

url = "https://www.rottentomatoes.com/m/moana_2016"
# print(url)

def movie_details(movie_url):
    data = requests.get(movie_url)
    # print(data)
    soup = BeautifulSoup(data.text,"html.parser")
    # print(soup)
    
    h1 = soup.find('h1', class_="scoreboard__title").get_text()
    """GET_TEXT()   WE NEED IT IN TEXT"""
    # print(h1)
    
    li = soup.find_all('li', class_="meta-row clearfix")
    '''li HTML ELEMENT IS USED TO REPRESENT AN ITEM IN A LIST'''
    # print(li)
    
    dict = {}
    dict["Name"] = h1
    # print(dict)
    
    for i in li:
        # print(i)
        
        j = i.text
        # print(j)
        
        k = j.split()
        '''HERE WE USED SPLIT FUNCTION BECASUE IT REMOVES ALL THE SPACE, GAP AND EXECUTE 
        INSIDE A LIST'''
        # print(k)
        
        if 'Rating:' in k:
            dict["Rating"] = k[1]
            '''WE USED K[1] BECAUSE WE ONLY WANT ONE ELEMENTS SO WE DID INDEX '''
            # print(dict)
            
        elif 'Genre:' in k:
            i = k[1:]
            l = ""
            # print(i)
            for m in i:
                l += m
            # print(l)
            
            l = l.split(",")
            # print(l)
            
            dict["Gerne"] = l
            # print(dict)
            
        elif 'Language:' in k:
            dict["Original Language"] = k[2]
            # print(dict)
            
        elif 'Director:' in k:
            n = k[1:]
            o = ""
            # print(n)
            for p in n:
                o += p
            # print(o)
            
            o = o.split(",")
            # print(o)
            
            dict["Director"] = o
            # print(dict)
            
        elif 'Producer:' in k:
            q = k[1:]
            r = ""
            # print(q)
            for s in q:
                r += s
            # print(r)
            
            dict["Producer"] = r
            # print(dict)
            
        elif 'Writer:' in k:
            a = k[1:]
            b = ""
            # print(a)
            
            for c in a:
                b += c
            # print(b)
            
            dict["Writer"] = b
            # print(dict)
            
            
        elif 'Runtime:' in k:
            s = k[1:]
            # print(s)
            
            for t in s:
                # print(t)
                
                if "h" in t:
                    first = int(t[: -1]) * 60
                    '''MULTIPLYING IT USING INDEX, 0: -1 , IT IS REMOVING THE h---> hour'''
                    # print(first)
                elif "m" in t:
                    second = int(t[: -1]) + first
                    # print(second)
                    
            dict["Runtime"] = second
            # print(dict)
            
            with open("task4_.json", "w") as f:
                json.dump(dict, f, indent = 4)
            return dict
                          
movie_details(url)