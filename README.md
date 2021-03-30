# KYJstream

## Install Docker on Windows

## Step 1 install WLS2 (for windows version >= 1903)
for Windows 10 64-bit: Home, Pro, Enterprise, or Education, 
version 1903 (Build 18362 or higher).

https://docs.microsoft.com/zh-tw/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

## Step 2 Install Docker Destop for Windows
https://hub.docker.com/editions/community/docker-ce-desktop-windows/

## App Initiation (Fisrt time only)
- clone the project
- Go to app root directory with bash shell (Git Bash is Okay too)
- execute the following command.
```
$ docker-compose build
$ docker-compose up
```

## Start Application Service
```
$ docker-compose up
```

## If There are Changes in Dockerfile
```
$ docker-compose build
```



