import requests
import multiprocessing

url="https://picsum.photos/2000/3000"
# num1=int(input("How many contents u want to download"))
def downloadFunc(url,i):
    print(f"Started Downloading file {i}")
    r = requests.get(url)
    open(f"photosDownload/ppDownloaded{i+1}.jpg","wb").write(r.content)
    print(f"Finished Downloading file {i}")
if __name__=="__main__":
        pros=[]
        for i in range(10):
                # url=input("Enter the url of the content")
                url="https://picsum.photos/2000/3000"
                p=multiprocessing.Process(target=downloadFunc,args=[url,i])
                pros.append(p)
                p.start()
                
        for p in pros:
            p.join()



