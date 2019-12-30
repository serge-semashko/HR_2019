import time
import threading
import json, ast
import threading
import flask
from flask import request
from flask import abort
from flask import Flask
from flask import make_response
from flask import jsonify
def run_flask():

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def get_alldata():
        # self.wfile.write(test2)
        test2 = '{"result":"ok"}'
        resp = make_response(test2,200)
        resp.headers['content-type']='text/html'
        resp.headers['Access-Control-Allow-Origin']= '*'
        resp.headers['Access-Control-Allow-Methods'] ='GET, POST, PUT, DELETE, OPTIONS'
        print('get ok')
        return resp    
    @app.route('/', methods=['POST'])
    def post_alldata():
        test2 = '{"result":"ok"}'
        # self.wfile.write(test2)

        resp = make_response(test2,200)
        resp.headers['content-type']='text/html'
        resp.headers['Access-Control-Allow-Origin']= '*'
        resp.headers['Access-Control-Allow-Methods'] ='GET, POST, PUT, DELETE, OPTIONS'
        print('post ok')
        return resp    




        


    if __name__ == '__main__':
        #from flask.logging import default_handler
        #app.logger.removeHandler(default_handler)
        app.run(debug=True,host="0.0.0.0",port=8082)
       
thread_flask     = threading.Thread(target=run_flask, args=())
print('aSDas')
thread_flask.run()
print('ASDasdaSDas')
