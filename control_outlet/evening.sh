#!/bin/bash
dt=`date '+%d/%m/%Y %H:%M:%S'`
echo -e "$dt\tGood evening!\tTurning off filter for feeding time!"
python /home/pi/monitor/control_outlet/controller.py -p27 -a1
