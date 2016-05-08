# Zoom 5370 modem status log to CSV
Logs the connection software and snmp event log pages on the Zoom 5370 modem into CSV output which you can pipe to a file or gzip/xz then to a file in a cron task 

`modem.py > "/var/log/modem/modem-$(date '+%m-%d-%y@%H:%M').csv"`

`modem.py | xz > "/var/log/modem/modem-$(date '+%m-%d-%y@%H:%M').csv.xz"`

`modem.py | gzip > "/var/log/modem/modem-$(date '+%m-%d-%y@%H:%M').csv.gz"`
    
##### modem-05-08-16@08:37.csv
