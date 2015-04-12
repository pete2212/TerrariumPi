#!/bin/bash
dt=`date '+%d/%m/%Y %H:%M:%S'`
echo -e "$dt\tGood morning!\tStarting filter and turning on UVA light"
python /home/pi/monitor/control_outlet/controller.py -p22,27,13 -a0
