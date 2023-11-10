<!--  https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax   -->
# Devopslive10 -Assignment 1
## Part 2

Step1: Pick Docker  
   

Step 2: Run Docker

```
root@dice-devops:/home# docker run -p 8000:8000  -d -t --name latest_unicorn    unicorn:v1
1c421046eb02bccfb4a8363299892c1d27bd9b5f9b8c8e0d5705f79a1509913c
root@dice-devops:/home# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED         STATUS        PORTS                                       NAMES
1c421046eb02   unicorn:v1   "python3 main.py"        2 seconds ago   Up 1 second   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   latest_unicorn
8b121467c308   nginx        "/docker-entrypoint.…"   13 hours ago    Up 13 hours                                               pedantic_nash
3ea6aa7e4382   nginx        "/docker-entrypoint.…"   39 hours ago    Up 39 hours   80/tcp                                      blissful_shtern

```





Step 3: Fiel Uploaded 

Step 4:  Build
  -  docker buildx build -t unicorn  -f Dockerfile .
 ```
root@dice-devops:/home# docker buildx build -t unicorn  -f Dockerfile .
[+] Building 2.5s (10/10) FINISHED                                                                                                                                                                                                             docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                     0.1s
 => => transferring dockerfile: 158B                                                                                                                                                                                                                     0.0s
 => [internal] load .dockerignore                                                                                                                                                                                                                        0.1s
 => => transferring context: 2B                                                                                                                                                                                                                          0.0s
 => [internal] load metadata for docker.io/library/python:3.8                                                                                                                                                                                            2.3s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                                                                            0.0s
 => [1/4] FROM docker.io/library/python:3.8@sha256:7a82536f5a2895b70416ccaffc49e6469d11ed8d9bf6bcfc52328faeae7c7710                                                                                                                                      0.0s
 => [internal] load build context                                                                                                                                                                                                                        0.0s
 => => transferring context: 503B                                                                                                                                                                                                                        0.0s
 => CACHED [2/4] RUN apt-get update                                                                                                                                                                                                                      0.0s
 => CACHED [3/4] RUN pip install fastapi uvicorn                                                                                                                                                                                                         0.0s
 => [4/4] COPY main.py main.py                                                                                                                                                                                                                           0.0s
 => exporting to image                                                                                                                                                                                                                                   0.0s
 => => exporting layers                                                                                                                                                                                                                                  0.0s
 => => writing image sha256:3496bfbb605ecbab47d1625047c482612cc8303f245638a0f13a8208d3f26234                                                                                                                                                             0.0s
 => => naming to docker.io/library/unicorn                                                                                                                                                                                                               0.0s

 ```  
