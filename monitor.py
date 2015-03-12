import Adafruit_DHT as dht
import sys
from time import sleep
from db import Temp, MonitorTime

class Monitor(object):
    @classmethod
    def run_monitor(cls):
        h, t = dht.read_retry(dht.DHT22, 4)
        temp = (t*9/5) + 32
        return temp, h

    @classmethod
    def get_value(cls):
        temp, humidity = cls.run_monitor()
        return temp, humidity

    @classmethod
    def start_monitor(cls):
        #TODO put in
        #2 second init time for dht22
        print 'starting monitor'
        started = False
        while not started:
            sleep(2)
            temp, humidity = cls.get_value()
            started = MonitorTime.add_value('Start', temp, humidity)

    @classmethod
    def poll_monitor(cls):
        temp = 0
        humidity = 0
        try:
            db_conn = Temp()
            cls.start_monitor()
            while(1):
                sleep(2)
                temp, humidity = cls.get_value()
                db_conn.add_value(temp, humidity)
        except:
            print 'Unexpected error:', sys.exc_info()[0]
        finally:
            print 'shutting down monitor and cleaning up'
            tdb_conn = MonitorTime()
            if tdb_conn:
                tdb_conn.add_value('end', temp, humidity)

Monitor.poll_monitor()
