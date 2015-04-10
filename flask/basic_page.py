from flask import Flask, render_template
import sys
sys.path.insert(0, '/home/pi/monitor')
import db
import wiringpi2 as wiringpi
# 0 = on, 1 = off, 27 = filter, 22 = light uva 6 = uvb


app = Flask(__name__)


@app.route("/")
def get_temp():
    v = db.QueryDb().get_recent()[0]
    vals = db.QueryDb().get_values(v.time)
    templateData = {}
    templateData = {'title': 'Terrarium controller',
                    'data': vals
                    }
#    for val in vals:
#        templateData.append({'humidity': val.humidity,
#                             'temp': val.temp,
#                             'time': val.time})
#        templateData[val.time] = {'humidity': val.humidity,
#                                'temp': val.temp,}
    return render_template('main.html', **templateData)


@app.route("/turnoff")
def turn_off():
    wiringpi.wiringPiSetupSys()
#    wiringpi.wiringPiSetupGpio()
#    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
#    wiringpi.pinMode(27, 1)
#    wiringpi.pinMode(22, 1)
#    wiringpi.pinMode(5, 0)
#    wiringpi.pinMode(6, 1)
#    wiringpi.pinMode(13, 0)
#    wiringpi.pinMode(19, 0)
#    wiringpi.pinMode(26, 0)
    wiringpi.digitalWrite(6, 1)
    wiringpi.digitalWrite(27, 1)
    wiringpi.digitalWrite(22, 1)
    templateData = {}
    return render_template('off.html', **templateData)


@app.route("/turnon")
def turn_on():
    wiringpi.wiringPiSetupSys()
#    wiringpi.wiringPiSetupGpio()
#    wiringpi.pinMode(27, 1)
#    wiringpi.pinMode(22, 1)
#    wiringpi.pinMode(5, 0)
#    wiringpi.pinMode(6, 1)
#    wiringpi.pinMode(13, 0)
#    wiringpi.pinMode(19, 0)
#    wiringpi.pinMode(26, 0)
    wiringpi.digitalWrite(6, 0)
    wiringpi.digitalWrite(27, 0)
    wiringpi.digitalWrite(22, 0)
    templateData = {}
    return render_template('on.html', **templateData)

@app.route("/turn_filter_off")
def turn_filter_off():
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(27, 1)
    wiringpi.pinMode(22, 1)
    wiringpi.pinMode(5, 0)
    wiringpi.pinMode(6, 1)
    wiringpi.pinMode(13, 0)
    wiringpi.pinMode(19, 0)
    wiringpi.pinMode(26, 0)
    wiringpi.digitalWrite(27, 1)
    templateData = {}
    return render_template('off.html', **templateData)

@app.template_filter()
def datetimefilter(value, format='%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
