# bobrock.dev
My personal website

## Setup process 
This is quite lengthy - check out `SETUP.md` for the full details

## Server maintenance
### Service commands (nginx)
Basic command structure is as follows:
`sudo systemctl (start|stop|restart|reload|disable|enable) nginx`
 - `start`: Starts server when it's stopped
 - `stop`: Stops the server
 - `restart`: Stops and then starts the server again 
 - `reload`: For when you're only making configuration changes - this reloads without dropping connections  
 - `disable`: Nginx starts automatically when the server boots. This disables that behaviour.
 - `enable`: Enable the service on boot
### Log locations
 - `/var/log/nginx/access.log` - Every request to the sever is recorded here
 - `/var/log/nginx/error.log` - Nginx errors logged here
 - `sudo journalctl -u nginx`: check the nginx process logs
 - `sudo journalctl -u bobrock.dev`: check the Flask app's gunicorn logs
