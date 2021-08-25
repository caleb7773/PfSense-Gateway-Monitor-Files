#!/bin/bash

# Password needs to be URL Encoded already and closed in with single quotes
PfSenseAdminPassword='pass'
PfSenseAdminUsername='user'
PfSenseURL='https://ip/'
CookiesFile=~/cookies.txt



grab_csrf() {
csrf=$(cat /tmp/csrf_output.txt | grep csrf_magic -m1 | cut -d ':' -f2 | cut -d ';' -f1)
csrfmagic=$(echo sid:${csrf})
echo ${csrfmagic} > /tmp/csrf.txt
sed -i 's/"//g' /tmp/csrf.txt
csrfmagic=$(cat /tmp/csrf.txt)
rm -rf /tmp/csrf_output.txt
rm -rf /tmp/csrf.txt
}




curl \
	-k \
	-c $CookiesFile \
	-b $CookiesFile \
	$PfSenseURL > /tmp/csrf_output.txt
clear
grab_csrf

#
# You have now requested the Login page for the pfSense
#



curl \
	-X POST \
	-k \
	-c $CookiesFile \
	-b $CookiesFile \
	-d "__csrf_magic=${csrfmagic}&usernamefld=$PfSenseAdminUsername&passwordfld=$PfSenseAdminPassword&login=Sign+In" \
	$PfSenseURL
clear
#
# You should now be logged into the pfSense
#



curl \
	-k \
	-c $CookiesFile \
	-b $CookiesFile \
       	$PfSenseURL > /tmp/csrf_output.txt
clear
grab_csrf

#
# You have now pulled up the pfSense Dashboard
#
echo "Resetting Gateway Group "HomeWAN"..."


curl \
	-k \
	-c $CookiesFile \
	-b $CookiesFile \
	${PfSenseURL}system_gateway_groups_edit.php?id=0 > /tmp/csrf_output.txt
clear
grab_csrf

name=WAN
gwname=WAN_DHCP
WAN_DHCP=1
WAN_DHCP_vip=address
description=WAN_GW
trigger=downlosslatency
descr=HomeWAN
id=0
save=Save


#
# You now have restarted the HomeWAN Gateway Group
#


curl GET \
	-k \
	-c $CookiesFile \
	-b $CookiesFile \
	-d "__csrf_magic=${csrfmagic}&name=${name}&gwname0=${gwname}&WAN_DHCP=${WAN_DHCP}&WAN_DHCP_vip=${WAN_DHCP_vip}&description=${description}&trigger=${trigger}&descr=${descr}&id=0&save=Save" \
	${PfSenseURL}system_gateway_groups_edit.php?id=0 > /tmp/csrf_output.txt
clear


curl \
        -k \
        -c $CookiesFile \
        -b $CookiesFile \
        ${PfSenseURL}system_gateway_groups_edit.php?id=0 > /tmp/csrf_output.txt
clear
grab_csrf


curl \
        -k \
        -c $CookiesFile \
        -b $CookiesFile \
        -d "__csrf_magic=${csrfmagic}&apply=Apply+Changes" \
        ${PfSenseURL}system_gateways.php
clear

#
# You have now applied your changes
#



rm -rf cookies.txt
echo 'Gateway Group "HomeWAN" has been restarted'


