'''A small program meant to run/output/test the dht22 sensor'''
import Adafruit_DHT as dht
from time import sleep

while(1):
    h, t = dht.read_retry(dht.DHT22, 4)
    print 'Temp={0:0.1f}F Humidity={1:0.1f}%'.format(((t*9/5)+32), h)
    sleep(2)

