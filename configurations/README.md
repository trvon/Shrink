## Configuration Files


## Nginx
### Server
This configuration file is located in:
```
/etc/nginx/sites-available
```
This configuration is used to server the python server client

### nginx.conf
This is a default configuration. We need to make sure if we setup a domain we simply add the correct configuration to:
```
/etc/nginx/sites-available
```
then we will need to 
```
ln -s /etc/nginx/sites-available/[FILE] /etc/nginx/sites-available
```

## Systemd

## MongoDB 
