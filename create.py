import os
import sys
from github import Github

name = str(sys.argv[1])
username = "PKyahhh"
password = "Flare123&"
path = "C:\\Users\\Pradham\\Desktop"
os.chdir("C:\\Users\\Pradham\\Desktop")

def create():
    os.mkdir(name)
    os.chdir("C:\\Users\\Pradham\\Desktop\\"+name)
    user = Github(username, password).get_user()
    user.create_repo(name)
    os.system("git init")
    os.system("git add README.md")
    os.system("git commit -m " + "first commit")
    os.system("git branch -M main")
    os.system("git remote add origin https://github.com/PKyahhh/"+name+".git")
    os.system("git push -u origin main")
    os.system("code .")
    print("Initilization complete")
    

if __name__ == "__main__":
    create()