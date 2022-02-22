#DA FINIRE
from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
time = datetime_London.strftime("%H:%M:%S")

@app.route('/', methods=['GET'])
def orario():
    return time

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)