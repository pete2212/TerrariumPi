import Adafruit_DHT as dht
from time import sleep
from db import Temp, MonitorTime


class Monitor(object):
    def __init__(self, pin):
        self._pin = pin

    def run_monitor(self):
        h, t = dht.read_retry(dht.DHT22, self._pin)
        if h and t:
            temp = (t*9/5) + 32
            return temp, h
        return False, False

    def get_value(self):
        temp, humidity = self.run_monitor()
        return temp, humidity

    def start_monitor(self):
        # TODO put in
        # 2 second init time for dht22
        print 'starting monitor'
        started = False
        counter = 0
        while not started and counter < 10:
            sleep(2)
            temp, humidity = self.get_value()
            if temp and humidity:
                started = MonitorTime.add_value('Start', temp, humidity)
            else:
                print ('Bad data returned from sensor.\nError count: %s'
                       % counter)
                counter += 1
        return started

    def poll_monitor(self):
        fail_counter = 0
        temp = 0
        humidity = 0
        db_conn = Temp()
        try:
            # Continue polling until failure counter reaches 10
            # and data remains invalid
            good_data = self.start_monitor()
            while(good_data or fail_counter < 10):
                sleep(2)
                temp, humidity = self.get_value()
                if temp is not None and humidity is not None:
                    db_conn.add_value(temp, humidity)
                else:
                    fail_counter += 1
            if fail_counter >= 10:
                raise ValueError("Failed to retrieve data for %s seconds" %
                                 (fail_counter * 2))
        except TypeError as e:
            print 'Type error caught({0})'.format(e)
        except KeyboardInterrupt:
            print 'User terminated monitor'
        except ValueError:
            print 'A critical error was encountered, exiting monitor'
        except Exception as inst:
            print 'Unexpected error: %s: %s' % (type(inst), inst)
        finally:
            print 'shutting down monitor and cleaning up'
            tdb_conn = MonitorTime()
            if tdb_conn:
                tdb_conn.add_value('end', temp, humidity)
