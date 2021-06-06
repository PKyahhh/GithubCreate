#pip install PyGithub
import os
import sys
from github import Github

#Defining variables like username and path
try:
    name = str(sys.argv[1]) #reads the value given after the word "create"
except:
    print("Usage: create [name of repo]")
    exit()
username = "USERNAME"
path = "PATH" #Don't forget to add backslashes to the end for later
os.chdir(path)
word = "First commit" 

def create():
    #Creating repo folder in the path specified and changing to that path
    os.mkdir(name)
    os.chdir(path+name)

    #Creating readme file inside the new folder
    f = open("README.md", "w+")
    f.write("Readme")
    f.close()

    #Accessing Github with login credentials
    user = Github("API Token")
    n = user.get_user()
    n.create_repo(name)

    #Using basic github steps to creating repo from terminal (Found on github)
    os.system("git init")
    os.system("git config --global user.email EMAIL")
    os.system("git commit -m " + word)
    os.system("git branch -m master")
    os.system("git remote add origin https://github.com/"+username+"/"+name+".git") #Don't forget to add username here
    os.system("code .")
    os.system("git add .")
    os.system("git commit -m README.md")
    os.system("git push origin master")
    print("Initilization complete")
    

if __name__ == "__main__":
    create()
