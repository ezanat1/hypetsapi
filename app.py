from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy


# Create a new Flask application
app = Flask(__name__)


import json

# filename = 'Facts/cats.txt'



  
# creating dictionary

def openAndConvert(filename):
    with open(filename) as fh:
        ct = 0
        myList = []
        for line in fh:
            dict1 = {}
            dict1.update({"fact":(line)})
            myList.append(dict1)
            ct +=1

    # out_file = open("test1.json", "w")
    # json.dump(myList, out_file, indent = 4, sort_keys = False)
    # out_file.close()
    print(ct)
    return myList



@app.route("/catfacts")
def catFacts():
    return jsonify(openAndConvert('Facts/cats.txt'))

@app.route("/dogfacts")
def dogFacts():
    return jsonify(openAndConvert('Facts/dogfacts.txt'))

@app.route("/fishfacts")
def fishFacts():
    return jsonify(openAndConvert('Facts/fish.txt'))

@app.route("/horsefacts")
def horseFacts():
    return jsonify(openAndConvert('Facts/horse.txt'))

if __name__ == "__main__":
    app.run(debug=True)