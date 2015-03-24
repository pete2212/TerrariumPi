import uuid
import datetime
import psycopg2.extras
from sqlalchemy import create_engine, MetaData, Table, desc
from sqlalchemy.orm import mapper, sessionmaker


class UpdateDBEntry(object):
    @classmethod
    def add_time_value(cls, temp, humidity):
        val = Temp()
        val.id = uuid.uuid4()
        val.time = datetime.datetime.now()
        val.temp = temp
        val.humidity = humidity
        session.add(val)
        session.commit()


class Temp(object):
    @classmethod
    def check_value(cls, temp, humidity):
        q = session.query(cls).order_by(desc('time')).first()
        if (q is not None and
            int(q.temp) == int(temp) and
                int(q.humidity) == int(humidity)):
            return False
        return True

    @classmethod
    def add_value(cls, temp, humidity):
        if cls.check_value(temp, humidity):
            UpdateDBEntry.add_time_value(temp, humidity)


class MonitorTime(object):
    @classmethod
    def add_value(cls, action, temp, humidity):
        if humidity and temp:
            val = cls()
            val.time = datetime.datetime.now()
            val.temp = temp
            val.humidity = humidity
            val.action = action
            session.add(val)
            session.commit()
            return True
        return False


class QueryDb(object):
    @classmethod
    def get_recent(cls, time_start=None):
        '''Gets the most recent data from last monitor timestamp until now
        '''
        q = session.query(MonitorTime)
        q = q.filter(MonitorTime.action == 'Start')
        q = q.order_by(MonitorTime.time.desc())
        q = q.limit(1)
        return q.all()

    @classmethod
    def get_values(cls, time):
        q = session.query(Temp).filter(Temp
                                       .time
                                       .between(time,
                                                datetime.datetime.now()))
        q = q.limit(150)
        return q.all()

temperature_schema = 'temperature'
engine = create_engine('postgresql://pi:raspberry@localhost/monitor')
metadata = MetaData(engine)
psycopg2.extras.register_uuid()
temp = Table('temp', metadata, schema=temperature_schema, autoload=True)
tmonitor = Table('monitor_time',
                 metadata,
                 schema=temperature_schema,
                 autoload=True)
mapper(Temp, temp)
mapper(MonitorTime, tmonitor)
Session = sessionmaker(bind=engine)
session = Session()
