import threading


class MonitorEngine(object):
    def __init__(self):
        self._pin_list = {'warm': 4,  # side of tank with heater
                          'cool': 17
                          }

    def init_engine(self):
        for label, pin in self._pin_list.iteritems():
            print label, pin

m = MonitorEngine()
m.init_engine()
