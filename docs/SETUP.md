# bobrock.dev setup

## Sources
 - Droplet, Nginx, Gunicorn, Flask (general) setup: [here](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04)
 - 

## More Info
 - [nginx block selection algorithms](https://www.digitalocean.com/community/tutorials/understanding-nginx-server-and-location-block-selection-algorithms)

## Step 1: Droplet setup
### Non-root user creation
```bash
MYUSER=username_here
adduser ${MYUSER}
usermod -aG sudo ${MYUSER}
```
### Firewall setup
```bash
ufw allow OpenSSH
ufw enable
ufw status
```
### Enable non-root user access
```bash
rsync --archive --chown=${MYUSER}:${MYUSER} ~/.ssh /home/${MYUSER}
```
Open up a new terminal window, try to log in as non-root user.
Close root session upon successful log in.

Make some new directories on the non-root user's home & set the timezone
```bash
mkdir keys logs venvs extras data
sudo timedatectl set-timezone America/Chicago
```

## Step 2: NGINX Setup
### Update env & install dependencies
```bash
sudo apt update && sudo apt upgrade
sudo apt install nginx
```
### Firewall adjustment
```bash
sudo ufw allow 'Nginx HTTP'
# Make sure service is running before testing site
sudo systemctl status nginx.service
```
Go to `http://{your-ip}` to confirm that your sit eis up
### Server block setup
This is used to encapsulate configuration details and host more than one domain from a single server
```bash
# Create directory and set ownership/permissions
sudo mkdir -p /var/www/bobrock.dev/html
sudo chown -R ${USER}:${USER} /var/www/bobrock.dev/html
sudo chmod -R 755 /var/www/bobrock.dev
# Create sample index.html file
nano /var/www/bobrock.dev/html/index.html
```
Copy/paste this in that file 
```html
<html>
    <head>
        <title>Welcome to bobrock.dev!</title>
    </head>
    <body>
        <h1>Success!  The bobrock.dev server block is working!</h1>
    </body>
</html>
```
Then let's make a new configuration file for nginx (instead of adjusting the `default`)
```bash
sudo nano /etc/nginx/sites-available/bobrock.dev
```
Copy/paste this into that file
```
server {
        listen 80;
        listen [::]:80;

        root /var/www/bobrock.dev/html;
        index index.html index.htm index.nginx-debian.html;

        server_name bobrock.dev www.bobrock.dev;

        location / {
                try_files $uri $uri/ =404;
        }
}
```
Then enable the file by creating a link from it to the `sites-enabled` directory
```bash
sudo ln -s /etc/nginx/sites-available/bobrock.dev /etc/nginx/sites-enabled/
```
Correct for possible hash bucket memory problem (idk, seems like something worth avoiding)
```bash
sudo nano /etc/nginx/nginx.conf
```
Uncomment the line that has `server_names_hash_bucket_size`, save and close.
Then test nginx configs and, if succeeded, restart the service.
```bash
sudo nginx -t
sudo systemctl restart nginx
```
## Step 3: Python env setup
```bash
sudo apt install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools 
# Setup venv and source into it
(cd ~/venvs && python3 -m venv bobrock.dev) && source ~/venvs/bobrock.dev/bin/activate
# Install necessary packages
pip install wheel flask gunicorn
```
Clone the git repo, Create a sample app
```bash
cd ~/extras && git clone https://github.com/barretobrock/bobrock.dev.git
cd bobrock.dev
nano test.py
```
```python
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1 style='color: blue'>Welcome!</h1>"   

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```
Allow access to port 5000
```bash
sudo ufw allow 5000
```
Check that the site shows this. Go to `http://{ip_address}:5000`

Create the WSGI entry point
```bash
nano wsgi.py
```
```python
from test import app

if __name__ == "__main__":
    app.run()
```
## Step 4: Gunicorn setup
Check that gunicorn can serve the application correctly
```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
Once that's running, the site again. Go to `http://{ip_address}:5000`

After that, `deactivate` the python env

Create the gunicorn service file
```bash
sudo nano /etc/systemd/system/bobrock.dev.service
```
```unit file (systemd)
[Unit]
Description=Gunicorn instance to serve bobrock.dev
After=network.target

[Service]
User=bobrock
Group=www-data
WorkingDirectory=/home/bobrock/extras/bobrock.dev
Environment="PATH=/home/bobrock/venvs/bobrock.dev/bin"
ExecStart=/home/bobrock/venvs/bobrock.dev/bin/gunicorn --workers 3 --bind unix:bobrock.dev.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```
Start the service & enable it
```bash
sudo systemctl start bobrock.dev
sudo systemctl enable bobrock.dev
```
## Step 5: Configure nginx to proxy requests
```bash
sudo nano /etc/nginx/sites-available/bobrock.dev
```
Add the following to the `location` section after `try_files`:
```
include proxy_params;
proxy_pass http://unix:/home/bobrock/extras/bobrock.dev/bobrock.dev.sock;
```
Test nginx and reload
```bash
sudo nginx -t
sudo systemctl restart nginx
```
Remove port 5000 access since we don't need it
```bash
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
## Step 6: Securing the site
Install certbot & setup the nginx plugin of certbot's SSL configuration
```bash
sudo apt install python3-certbot-nginx
sudo certbot --nginx -d bobrock.dev -d www.bobrock.dev
```
Remove redundant HTTP profile
```bash
sudo ufw delete allow 'Nginx HTTP'
```
The domain should now load properly when you go to `https://bobrock.dev`