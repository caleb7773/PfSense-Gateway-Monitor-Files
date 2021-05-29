#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html>"
echo "<meta http-equiv="refresh" content="4;url=../index.html" />"
echo "<head><title>Restarting WiFi"
echo "</title></head><body>"
echo "<h1> Resetting... </h1>"
sudo systemctl stop rsyslog
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wangw.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wanalt_dhcp.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wantertiary_dhcp.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/mgmt.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/netherlands.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/london.cgi
sudo rm -rf /var/log/pfsense_gateway_alarm.log
sudo touch /var/log/pfsense_gateway_alarm.log
sudo chmod 640 /var/log/pfsense_gateway_alarm.log
sudo chown syslog:adm /var/log/pfsense_gateway_alarm.log
sudo systemctl start rsyslog
sudo systemctl restart rsyslog
echo "<br>"
echo "$(date)"
echo "<h2><a href="../index.html">Return to Main Menu</a></h3>"
echo ""
echo "</body></html>"
