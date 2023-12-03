import requests
import json
topicQuery=input("Enter the topic of news u wanna see? ")
url2=(f"https://newsdata.io/api/1/news?apikey=sth&q={topicQuery}")
url1 =(f"https://newsapi.org/v2/everything?q={topicQuery}&from=2023-10-22&sortBy=publishedAt&apiKey=sth")
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
       

