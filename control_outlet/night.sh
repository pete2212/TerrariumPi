#!/bin/bash
dt=`date '+%d/%m/%Y %H:%M:%S'`
echo -e "$dt\tGood night!\tTurning all outlets off for the night!"
python /home/pi/monitor/control_outlet/controller.py -p6,22,27,13 -a1
