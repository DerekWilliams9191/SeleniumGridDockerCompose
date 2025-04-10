# SeleniumGridDockerCompose


## Getting Started
Starting grid server
```
docker compose -f docker-compose-v3-dev-channel.yaml up
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
