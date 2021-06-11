# Some brief notes to help with periodic maintenance...

## service files
`/etc/systemd/system/bobrock.dev.service`
```unit file (systemd)
[Unit]
Description=Gunicorn instance to serve bobrock.dev
After=network.target

[Service]
User=bobrock
Group=www-data
WorkingDirectory=/home/bobrock/extras/bobrock.dev
Environment="PATH=/home/bobrock/venvs/bobrock.dev/bin"
ExecStart=/home/bobrock/venvs/bobrock.dev/bin/gunicorn --workers 3 --bind unix:bobrock.dev.sock -m 007 'wsgi:create_app()'

[Install]
WantedBy=multi-user.target
```