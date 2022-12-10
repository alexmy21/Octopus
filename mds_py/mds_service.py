from commands import Commands

import flask
from flask import request, jsonify,make_response
import time
import multiprocessing

app = flask.Flask('__name__')

def API(Conf):
   print('In API selction')
   app.run(host='0.0.0.0', port=1337,)

if __name__ == "__main__":
   config = {"Something":"SomethingElese"}
   p = multiprocessing.Process(target=API, args=([]))
   p.start()
   #time.sleep(3)
   print('After Flask run')

# class Service:
#     config:dict

#     def __init__(self, _config):
#         self.config = _config