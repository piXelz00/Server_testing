from flask import Flask,request,render_template
import json
from flask_cors import CORS
from datetime import datetime
import pytz

DATA = None
app = Flask(__name__)

CORS(app)
@app.route("/TESTING",methods = ['POST'])
def hello():
    if request.method=="POST":
        global DATA
        DATA = request.get_json()
        print(DATA)
        return json.dumps({'success':True}), 200, {
    "ContentType":"application/json"
} 

@app.route("/", methods=['GET',"POST"])
def get_global_data():
    global DATA
    if DATA is not None:
        # Set the time zone for India Standard Time (IST)
        ist_tz = pytz.timezone('Asia/Kolkata')
        # Get the current time in IST
        ist_time = datetime.now(ist_tz)
        # Format the time as a string
        formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
        b = {" A Random String ":DATA,
             "Timestamp":formatted_time}
        return render_template("index.html",data=b)
    else:
        return {"message": "No data available,",
                "Timestamp":formatted_time}, 404


if __name__ == '__main__':
    app.run()

