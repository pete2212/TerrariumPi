class ProcessEvent(object):
    '''
    Possible output types:
        api, db
    '''
    def __init__(self,
                 output='api',
                 url='chasingdaylight.net',
                 port='85'):
        self._output = output
        self._url = url
        self._port = port

    def action_event(self, action, time):
        ''' Takes a given event and time and logs them
        '''
        message = {'action': {'time': time,
                              'action': action
                              }
                   }
        self.send_event(message)

    def monitor_update_event(self, info):
        message = {'thermistor': {'time': info['time'],
                                  'pin': info['pin'],
                                  'label': info['label'],
                                  'humidity': info['humidity'],
                                  'temp': info['temp']
                                  }
                   }
        self.send_event(message)

    def send_event(self, message):
        pass
