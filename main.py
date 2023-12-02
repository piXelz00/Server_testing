from flask import Flask,request,render_template
import json
from flask_cors import CORS

DATA = None
app = Flask(__name__)

CORS(app)
@app.route("/TESTING",methods = ['POST'])
def hello():
    if request.method=="POST":
        global DATA
        DATA = request.get_json(force=True)
        print(DATA)
        return json.dumps({'success':True}), 200, {
    "ContentType":"application/json"
} 

@app.route("/", methods=['GET',"POST"])
def get_global_data():
    global DATA
    if DATA is not None:
        b= {"data": DATA}, 200
        return render_template("index.html",data=b)
    else:
        return {"message": "No data available"}, 404

if __name__ == '__main__':
    app.run()
