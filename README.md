# SeleniumGridDockerCompose


### Getting Started
Starting grid server
```
docker compose -f docker-compose-v3-dev-channel.yaml up
```

### How To See Inside (Debug)
#### Accessing Selenium Grid Webpage
```
http://localhost:4444/ui/#
```

#### Accessing the VNC
The vnc is what allows you to see the browser live, Selenium grid uses noVNC so you can view everything in the broswer.

If you would like to access it through a tradtioanl VNC client, you can access with the following. Change the port as needed.
```
127.0.0.1:7900
```

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
