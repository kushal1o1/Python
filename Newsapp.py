import requests
import json
topicQuery=input("Enter the topic of news u wanna see? ")
url2=(f"https://newsdata.io/api/1/news?apikey=pub_33348feb9670e375922fd8884b1751b2080dd&q={topicQuery}")
url1 =(f"https://newsapi.org/v2/everything?q={topicQuery}&from=2023-10-22&sortBy=publishedAt&apiKey=c223759de787406e80aa53c2add7b48e")
url=int(input("Type 1 for url1 or 2 for  url2(np)"))
if url==1:
    response = requests.get(url1)
    news=json.loads(response.text)
    for article in news["articles"]:
       print(f"HEADING:\n{article["title"]}       ")
       print(f"DESCRIPTION:\n{article["description"]} ")
       print(f"LINK:{article["url"]}         ")
       print(f"PUBLISHED AT:{article["publishedAt"]} ")
       print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
       
else:
    response = requests.get(url2)
    news=json.loads(response.text)
    for article in news["results"]:
       print(f"HEADING:\n{article["title"]} ")
       print(f"DESCRIPTION:\n{article["description"]} ")
       print(f"LINK:{article["link"]}         ")
       print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
       

