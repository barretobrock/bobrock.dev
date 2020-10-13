## Notes for adding extra services

### Adding subdomains
Open up the nginx file
```bash
sudo nano /etc/nginx/sites-available/bobrock.dev
```
Add the following below the existing code
```bash
server {
    listen 80;
    server_name viktor.bobrock.dev;
    location / {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:<port>;
        proxy_redirect off;
    }
}
```
Test the service
```bash
sudo nginx -t
```
Add the new subdomain to the DNS record as an A record
(hostname='viktor')

Dig the new address until the ip shows up
```bash
dig viktor.bobrock.dev
```
Run certbot with the new subdomain included, follow the prompts ('u', '2')
```bash
sudo certbot --cert-name bobrock.dev -d bobrock.dev -d www.bobrock.dev -d viktor.bobrock.dev
```
Test and restart nginx
```bash
sudo nginx -t
sudo systemctl restart nginx
```
