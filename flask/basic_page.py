from flask import Flask, render_template
import sys
sys.path.insert(0,'..')
import db
import datetime
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

@app.template_filter()
def datetimefilter(value, format='%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=85, debug=True)
