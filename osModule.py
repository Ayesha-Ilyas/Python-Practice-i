import os
print(dir(os))
print(os.getcwd())
#os.chdir("C://")
#print(os.getcwd())
f=open("map.html")
print(type(os.listdir("C://")))
os.mkdir("this")
os.makedirs("those/that")
os.rename("t.txt","T.txt")
print(os.environ.get('path'))
print(os.path.join("C://","T.txt"))
print(os.path.exists("C://T.txt"))
print(os.path.isfile("C://T.txt"))
os.rename("T.txt","t.txt")



