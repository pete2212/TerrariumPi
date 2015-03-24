import Adafruit_DHT as dht
from time import sleep
from db import Temp, MonitorTime


class Monitor(object):
    @classmethod
    def run_monitor(cls):
        h, t = dht.read_retry(dht.DHT22, 4)
        if h and t:
            temp = (t*9/5) + 32
            return temp, h
        return False, False

    @classmethod
    def get_value(cls):
        temp, humidity = cls.run_monitor()
        return temp, humidity

    @classmethod
    def start_monitor(cls):
        # TODO put in
        # 2 second init time for dht22
        print 'starting monitor'
        started = False
        counter = 0
        while not started and counter < 10:
            sleep(2)
            temp, humidity = cls.get_value()
            if temp and humidity:
                started = MonitorTime.add_value('Start', temp, humidity)
                if started:
                    print ('initial values: temp %s - humidity  %s' %
                           (temp, humidity))
                else:
                    print 'not started'
            else:
                print ('Bad data returned from sensor.\nError count: %s'
                       % counter)
                counter += 1
        return started

    @classmethod
    def poll_monitor(cls):
        fail_counter = 0
        temp = 0
        humidity = 0
        db_conn = Temp()
        try:
            good_data = cls.start_monitor()
            while(good_data or fail_counter < 10):
                sleep(2)
                temp, humidity = cls.get_value()
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

Monitor.poll_monitor()
