import os
if not os.path.exists("data"):
 os.mkdir("data")
os.chdir("D:\pythonPractice\data")
x=int(input("Enter no of files"))
ftype=input("ENter file type like png,jpg,pdf,exe,py,c,cpp,doc,etc\n")
for i in range(x):
    f=open(f'myfile{i+1}.{ftype}','x')
print("Sucessfully created")