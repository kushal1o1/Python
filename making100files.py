import os
if not os.path.exists("TrialFile"):
    os.mkdir("TrialFile")
x=int(input("ENter no of files"))
for i in range(x):
    if not os.path.exists(f"TrialFile/image{i+1}.png"):
        os.mkdir(f"TrialFile/image{i+1}.png")
folders=os.listdir("TrialFile")
print(folders)
for folder in folders:
   print(folder)
print(f"sucessfully created {i+1}files")

