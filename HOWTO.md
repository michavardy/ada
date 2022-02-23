# git
## initialize
- ```git init```
## git add
- ``` git add .```
## git status
- ``` git status```
## git commit
- ``` git commit -m "<commit name>"```
## git remote intialize
- ``` git remote add origin 'http://github.com/michavardy/proj_name'```
## git push
- ```git push -u origin master```
## git branch list all
- ```git branch```
## git branch create a new branch
- ```git checkout -b <branch_name>```
## git switch branches
- ```git checkout <branch_name>```
## list remote branches
- ``` git pull```
## merge branch
- ```git merge <branch_name>```
## delete branch
- ```git branch -d <branch_name>```

# Github CLI
## clone repo
- ```gh repo clone <repository> [<directory>] [-- <gitflags>...]```
## pull request
- ```gh pr create [flags] <repository> ```


# Docker-Compose

## build image from docockerfile
- ```docker-compose build```
## create and start containers
```docker-compose up```
## start services with detached mode
```docker-compose -d up```
## start specific service
```docker-compose up <service-name>```
## list images
```docker-compose images```
## list containers
```docker-compose ps```
## start service
```docker-compose start```
## stop services
```docker-compose stop```
## display running containers
```docker-compose top```
## kill services
```docker-compose kill```
## remove stopped containers
```docker-compose rm```
## stop all contaners and remove images, volumes
```docker-compose down```