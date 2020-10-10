#pip install PyGithub
import os
import sys
from github import Github

#Defining variables like username and path
name = str(sys.argv[1]) #reads the value given after the word "create"
username = "USERNAME"
password = "PASSWORD"
path = "PATH" #Don't forget to add backslashes to the end for later
os.chdir("PATH")
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
    user = Github(username, password).get_user()
    user.create_repo(name)

    #Using basic github steps to creating repo from terminal (Found on github)
    os.system("git init")
    os.system("git commit -m " + word)
    os.system("git branch -m master")
    os.system("git remote add origin https://github.com/USERNAME/"+name+".git") #Don't forget to add username here
    os.system("code .")
    os.system("git add .")
    os.system("git commit -m README.md")
    os.system("git push origin master")
    print("Initilization complete")
    

if __name__ == "__main__":
    create()
