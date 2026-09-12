# Initial Setup
```
sudo apt install python3-pip
pip install playwright

# Add the directory in which playwright is installed to your PATH variable 
echo 'export PATH="$PATH:$HOME/.local/bin"' >> $HOME/.bashrc

playwright install-deps chromium 
playwright install chromium 
```

# Run

```
python3 wifi_logger.py
```

# Automate
```
# Create a systemd service 
sudo nano /etc/systemd/system/auto_login.service
```
### Create the entry for the login service as follows. Replace "user" under the [Service] section with your actual username
```
[Unit]
Description=Wifi Login Automation
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=user
ExecStart=/usr/bin/python3 $HOME/wifi-auto-login/wifi_logger.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Save the file and exit nano

```
# Reload daemon
sudo systemctl daemon-reload

# Start the service
sudo systemctl start auto_login.service

# Check status
sudo systemctl status auto_login.service

# Start automatically at boot
sudo systemctl enable auto_login.service
```
