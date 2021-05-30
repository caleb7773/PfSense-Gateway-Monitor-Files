sudo apt install net-tools apache2-bin rsyslog -y
sudo apt install apache2 -y

sudo mkdir /home/www-data
sudo chown -R /home/www-data

# Enable CGI Scripts on Apache
sudo chown -R www-data:www-data /var/www
sudo chmod go-rwx /var/www
sudo chmod go+x /var/www
sudo chgrp -R www-data /var/www
sudo chmod -R go-rwx /var/www
sudo chmod -R g+rx /var/www
sudo chmod -R g+rwx /var/www
sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/
sudo systemctl enable apache2
sudo systemctl restart apache2

# Set www-data to no password sudo permissions
echo '%www-data ALL=(ALL) NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo
