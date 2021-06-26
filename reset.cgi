#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html lang='en'>"
# echo "<meta http-equiv="refresh" content="4;url='../index.html'" />"
echo "<head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Restarting WiFi</title></head>"
echo "<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        background-image: linear-gradient(315deg, #5d4257 0%, #89aa9a 74%);
        align-items: center;
        display: flex;
        flex-direction: column;
        font-family: sans-serif;
        justify-content: flex-start;
        min-height: 100vh;
        text-align: center;
    }

    .return-btn {
        background-color: rgba(66, 66, 66);
        color: white;
        font-size: 1.2rem;
        text-decoration: none;
        padding: 10px;
    }

    .return-btn:hover {
        background-color: white;
        color: black;
    }

    h1 {
        color: white;
        font-size: 2rem;
        letter-spacing: 1px;
        margin: 15px 0;
    }

    .date {
        color: white;
        font-size: 1.5rem;
    }

    .main {
        background-color: rgba(90, 90, 90);
        box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
        align-items: center;
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(3, 1fr);
        justify-content: center;
        margin: 20px;
        padding: 50px;
        row-gap: 20px;
    }

    .nav-bar {
        align-items: center;
        background-color: rgb(66, 66, 66);
        box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
        padding: 20px;
        width: 100%;
    }

    .nav-bar a {
        color: white;
        text-decoration: none;
    }

    .nav-bar a:hover {
        color: rgb(173, 173, 173);
    }

    .nav-bar h3 {
        font-size: 1.5rem;
    }

    /* Progress Bar */
    .progress {
        border: 10px solid #89aa9a;
        border-radius: 15px;
        height: auto;
        width: auto;
    }

    .progress-color {
        animation: progres 4500ms linear;
        background-color: #FFFFFF;
        border-radius: 15px;
        width: 0;
        height: 10px;
    }

    @keyframes progres {
        0% {
            width: 0%;
        }

        25% {
            width: 25%;
        }

        50% {
            width: 50%;
        }

        75% {
            width: 75%;
        }

        100% {
            width: 100%;
        }
    };

    
</style>"
echo "<body>"
echo "<div class='nav-bar'><a href='/index.html'><h3>PfSense Gateway Monitor</h3></a></div>"
echo "<div class='main'>"
echo "<h1> Resetting... </h1>"
echo "<div class='progress'><div class='progress-color'></div></div>"
echo "<p class='date'>$(date)</p>"
echo "<div><a class='return-btn' href='../index.html'>Return to Main Menu</a></div>"
echo "</div>"
sudo systemctl stop rsyslog
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wangw.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wanalt_dhcp.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/wantertiary_dhcp.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/mgmt.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/netherlands.cgi
sudo sed -i 's/: #.*/: #7CFC00;"/g' /usr/lib/cgi-bin/london.cgi
sudo rm -rf /var/log/pfsense_gateway_alarm.log
sudo rm -rf /home/www-data/vpn*
sudo rm -rf /home/www-data/wan*
echo "$(date "+%Y-%m-%e %T") --- Gateway Monitor Reset<br>" >> /home/www-data/temp.log
cat /home/www-data/pfsense_gw.log >> /home/www-data/temp.log
mv /home/www-data/temp.log /home/www-data/pfsense_gw.log 
sudo touch /var/log/pfsense_gateway_alarm.log
sudo chmod 640 /var/log/pfsense_gateway_alarm.log
sudo chown syslog:adm /var/log/pfsense_gateway_alarm.log
sudo systemctl start rsyslog
sudo systemctl restart rsyslog
echo "<br>"
echo ""
echo "<script>setTimeout(() => {
    window.location.href='../index.html';
}, 4500)</script>"
echo "</body></html>"
