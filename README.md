# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### links
In foreground mode (the default when -d is not specified), docker run can start the process in the container and attach the console to the process’s standard input, output, and standard error. It can even pretend to be a TTY (this is what most command line executables expect) and pass along signals. All of that is configurable:
-t              : Allocate a pseudo-tty
https://docs.docker.com/engine/reference/run/#foreground

Docker:
```
docker run -t test_docker_python-test
```
Docker-compose:
```
sudo docker-compose up/down
```

https://stackoverflow.com/questions/53221412/why-the-none-image-appears-in-docker-and-how-can-we-avoid-it

```
docker system prune
docker image ls
docker rmi image
```
Git ubuntu

```
git add -u, for all files
git commit -m "my text"
git push -u origin master
```



Add additional notes about how to deploy this on a live system

## Built With

* [dockers doc](https://docs.docker.com/) - doc

## Authors

* **jekl** - *Initial work* - [elo](https://follow-e-lo.com/)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
