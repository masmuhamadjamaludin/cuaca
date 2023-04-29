from http import client
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb://masmuhamadjamaludin10:GPiccdZTeotp6y68@ac-qxx6olp-shard-00-00.lbomoax.mongodb.net:27017,ac-qxx6olp-shard-00-01.lbomoax.mongodb.net:27017,ac-qxx6olp-shard-00-02.lbomoax.mongodb.net:27017/?ssl=true&replicaSet=atlas-2kj0jp-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def home(): 
    return render_template('index.html')

@app.route('/about',methods= ['GET'])
def about(): 
    return render_template('about.html')

@app.route('/info',methods= ['GET'])
def get_info(): 
    my_name = request.args.get('my_name')
    print(my_name)
    return jsonify({
        'msg': 'GET info'
 })

@app.route('/info',methods= ['POST'])
def post_info(): 
    my_name = request.form['my_name']
    print(my_name)
    return jsonify({
        'msg': 'POST info'
 })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)