'''A small program meant to run/output/test the dht22 sensor'''
import Adafruit_DHT as dht
from time import sleep

quite = False
while(quite is not True):
    try:
        h, t = dht.read_retry(dht.DHT22, 4)
        if h and t:
            print 'Pin 4 Temp={0:0.1f}F Humidity={1:0.1f}%'.format(((t*9/5)+32), h)
        else:
            print 'dht22 pin 4 not valid'
        h, t = dht.read_retry(dht.DHT22, 17)
        if h and t:
            print 'Pin 17 Temp={0:0.1f}F Humidity={1:0.1f}%'.format(((t*9/5)+32), h)
            sleep(2)
        else:
            print 'dht22 pin 17 not valid'
    except KeyboardInterrupt:
        print '\nExiting\n'
        quite = True
