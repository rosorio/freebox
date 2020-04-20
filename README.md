# Tools, scripts and docs fo the FreeBox env

## freewifi_autocon.py

This script keeps your authenticated to a FreeWifi hotspot.

*You must edit the script* in order to change the FREEWIFI_ID adn FREEWIFI_PASSWORD the start the script.

The script will check periodically (2 sec) if you are able to access to google server, without catching
an HTTP redirect from FreeWifi Hotspot. If a redirection is spot, the script do/redo the authentication.


