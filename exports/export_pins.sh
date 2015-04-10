#Exports pins for use with power controller, currently only 3 outlets
echo 'Exporting pins 22, 27 and 6'
sudo -u pi /usr/local/bin/gpio export 22 out
sudo -u pi /usr/local/bin/gpio export 27 out
sudo -u pi /usr/local/bin/gpio export 6 out
gpio -g write 22 1
gpio -g write 27 1
gpio -g write 6 1
