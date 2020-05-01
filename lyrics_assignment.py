# import requests
# import json

# data_dict = {
#             "username"  	: "daevheed13",
#             "firstname" 	: "Oluwasegun",
#             "lastname"  	: "Ajikobi",
#             "email"     	: "daevheed13@gmail.com",
#             "phone"     	: "09054833916",
#             "details"   	: "i can't kill myself",
#             "password"  	: "6264213"
#         }

# json_data = json.dumps(data_dict)
# url = "http://univelcity.pythonanywhere.com/data/register/"

# req = requests.post(url, json_data)

# print(req.json())

# {'response': 'success', 'message':
#                                 'Successfully added user -->  Oluwasegun',
#                                 'data': {'access_token': ' w6sOBTjZ5Qr0jPajPzF9AJeVvJ9rZFoOo519ZERJF7LE4STlwOZ6TA'}
#                                 }

import requests
import json 
import os
from collections import Counter

data_raw = {}

data_raw["details"] = {"username"  	: "daevheed13", "access_token"  :  "w6sOBTjZ5Qr0jPajPzF9AJeVvJ9rZFoOo519ZERJF7LE4STlwOZ6TA"}

data_dict = {}

data_raw["data"] = []

path = "C:/Users/Ajikobi Oluwasegun/Desktop/Python/Code/lyrics"

folder = os.fsencode(path)

for i in os.listdir(folder):

    filename = os.fsdecode(i)
    data = open(f"{path}/{filename}", "r", errors = "ignore")
    lyrics = data.read()
    

    s_lyrics = lyrics.strip().replace(",", "").replace("(", "").replace(")", "").lower().split()
    counts = Counter(s_lyrics)
    most_occuring = counts.most_common(1)
    data_dict["most_occuring_word"] = most_occuring[0][0]
    
    ss_lyrics = "".join(s_lyrics)
    sss_lyrics = list(ss_lyrics)
    
    count_a = sss_lyrics.count("a")
    data_dict["vowel_a"] = count_a
        
    count_e = sss_lyrics.count("e")
    data_dict["vowel_e"] = count_e
    
    count_i = sss_lyrics.count("i")
    data_dict["vowel_i"] = count_i
        
    count_o = sss_lyrics.count("o")
    data_dict["vowel_o"] = count_o
        
    count_u = sss_lyrics.count("u")
    data_dict["vowel_u"] = count_u

    data_dict["lyrics"] = lyrics.replace("\n", ". ")

    splitted_filename = filename.replace(".lrc", "").split(" -- ")
    data_dict["artist"] = splitted_filename[1]
    data_dict["title"] = splitted_filename[0]
    
    data_raw["data"].append(data_dict.copy())
    print(data_dict)     
    # print(data_dict["most_occuring_word"])     
# print(json.dumps(data_raw))

# json_data = json.dumps(data_raw)
# url = "http://univelcity.pythonanywhere.com/data/add_lyrics/"

# req = requests.post(url, json_data)

# print(req.json())


# words = ["shegs", "boy", "fam", "shegs", "boy", "fam", "boy", "fam", "fam", "shegs", "boy"]

# from collections import Counter

# counts = Counter(words)
# occurrent = counts.most_common()
# print(occurrent)
