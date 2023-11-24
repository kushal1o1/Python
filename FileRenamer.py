import os

print("welcome to File Renamer\n")
foldername=input("Enter the folder name")
path=input("Enter the path of  the folder")
os.chdir(path)
ftype=input("ENter the type of file u need to change name")
new_filetype = input('Enter new extension')
def func(ft,fn,nft):
 folder=os.listdir(f"{fn}")
 print(folder)
 i=1
 for file in folder:
    _,extension=os.path.splitext(file)
    print(extension)
    if extension==f".{ft}":
     x=True
     while x:
      if not os.path.exists(f"{i}.{nft}"):
        os.rename(f"{fn}/{file}",f"{fn}/{i}.{nft}")
        print(f"{file} changed to {i}.{ft}")
        i+=1
        x=False
      else:
       i+=1
print("Done Sucessfully.Check your FIle")
func(ftype,foldername,new_filetype)
