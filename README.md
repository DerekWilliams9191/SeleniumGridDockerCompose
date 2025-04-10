# SeleniumGridDockerCompose
For those who may come across this, to get started you need **Docker** and **docker compose** installed. Once installed, you can start the docker grid server by running the command below. You can check that it started successfully by accessing the webpage. It should list all the browsers. After starting the server, to get a webdriver, you need to ask the selenium hub for a new driver. I have already made a function that makes this very easy in [get_driver.py](https://github.com/DerekWilliams9191/SeleniumGridDockerCompose/blob/main/get_driver.py). You can run this on the host pt or inside another docker container. If you are running this in another docker container, [docker-compose.yaml](https://github.com/DerekWilliams9191/SeleniumGridDockerCompose/blob/main/docker-compose.yaml) provides the needed environment and host values.


## Getting Started
Starting grid server
```
docker compose -f docker-compose-selenium-grid.yaml up
```

## How To See Inside (Debug)
### Accessing Selenium Grid Webpage
```
http://localhost:4444/ui/
```

___

### Accessing the VNC
The VNC allows you to see the browser live

#### Traditional VNC
If you would like to access it through a traditional VNC client, you can access with the following.
<br>
*Change the port as needed.*
```
127.0.0.1:7900
```

___

#### Web-based VNC
Selenium grid uses noVNC so you can view everything in the broswer.

Chrome (port 7900)
```
http://localhost:7900/?autoconnect=1&resize=scale&password=secret
```

Firefox (port 7901)
```
http://localhost:7901/?autoconnect=1&resize=scale&password=secret
```

Edge (port 7902)
```
http://localhost:7902/?autoconnect=1&resize=scale&password=secret
```
