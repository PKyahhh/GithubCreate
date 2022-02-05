package main

import(
	"fmt"
	"os"
	"github.com/google/go-github/v42/github"
	"golang.org/x/oauth2"
	"context"
	"github.com/joho/godotenv"
	"os/exec"
	"runtime"
)

func main(){
	if len(os.Args) != 2{
		fmt.Println("Usage: init <RepoName>")
		os.Exit(-1)
	}

	godotenv.Load()
	ctx := context.Background()
	ts := oauth2.StaticTokenSource(&oauth2.Token{AccessToken: os.Getenv("TOKEN")},)
	tc := oauth2.NewClient(ctx, ts) //Create auth client
	client := github.NewClient(tc) //Create github client
	

	repo := &github.Repository{Name: github.String(os.Args[1])} //Create repo object
	_,_,err := client.Repositories.Create(ctx, "", repo) //Create repo
	if err != nil{
		fmt.Println("Error creating repo")
		os.Exit(-1)
	}
	//Create README and add to repo
	file := &github.RepositoryContentFileOptions{
		Message: github.String("Initial commit"),
		Content: []byte("# " + os.Args[1]),
	}
	_,_,err = client.Repositories.CreateFile(ctx, os.Getenv("USERNAME"), os.Args[1], "README.md", file) //Add README to repo
	if err != nil{
		fmt.Println("Error creating README")
		fmt.Println(err)
		os.Exit(-1)
	}
	//Create .gitignore and add to repo
	file = &github.RepositoryContentFileOptions{
		Message: github.String("Initial commit"),
		Content: []byte(".gitignore"),
	}
	_,_,err = client.Repositories.CreateFile(ctx, os.Getenv("USERNAME"), os.Args[1], ".gitignore", file) //Add .gitignore to repo
	if err != nil{
		fmt.Println("Error creating .gitignore")
		fmt.Println(err)
		os.Exit(-1)
	}
	
	//Run platform specific command to clone repo
	if runtime.GOOS == "windows"{
		_, err = exec.Command("cmd.exe","/c","git clone https://github.com/" + os.Getenv("USERNAME") + "/" + os.Args[1]).Output()
	} else{
		_, err = exec.Command("bash","-c","git clone https://github.com/" + os.Getenv("USERNAME") + "/" + os.Args[1]).Output()
	}
	fmt.Println("Repo created successfully")
}
