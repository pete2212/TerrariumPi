#!/bin/bash
dt=`date '+%d/%m/%Y %H:%M:%S'`
echo -e "$dt\tGood afternoon!\tTurning on UVB light"
python /home/pi/monitor/control_outlet/controller.py -p6 -a0
