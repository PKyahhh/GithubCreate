package main

import(
	"fmt"
	"os"
	"github.com/google/go-github/v42/github"
	"golang.org/x/oauth2"
	"context"
	"github.com/joho/godotenv"
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
	fmt.Println("Repo created")


	
}
