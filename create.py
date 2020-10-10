import os
import sys
from github import Github

name = str(sys.argv[1])
username = "USERNAME"
password = "PASSWORD"
path = "PATH"
os.chdir("PATH")

def create():
    os.mkdir(name)
    os.chdir("PATH"+name)
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
