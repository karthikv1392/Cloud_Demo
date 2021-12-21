import asyncio
import threading
import time
import tornado.ioloop
import tornado.web
from elasticsearch import Elasticsearch
from fpdf import FPDF
import tornado.httpserver
from datetime import datetime
import json
import requests
import traceback
import os
import random

#port = int(os.environ['PORT_NUM'])
port = 8895
#port = int(os.environ['PORT_NUM'])


booking_counter = 0
available_counter = 0


login_dict = {}
login_dict["username"] = "sample"
login_dict["password"] = "sample123"

class User_Login_Handler(tornado.web.RequestHandler):
    def post(self):
        start_time = datetime.now()
        response_json = {}
        response_json["status"] = "failed"

        global booking_counter
        try:
            json_request_string = self.request.body
            json_object = json.loads(json_request_string)
            print (json_object)
            username = json_object["username"]
            password = json_object["password"]

            '''
            search_param = {
                "query": {
                    "match_all": {
                    }
                }
            }
            res = es.search(index="login", body=search_param, size=200)
            print (res)
            flag = 0
            for hit in res['hits']['hits']:
                if username == hit["_source"]["username"] and password == hit["_source"]["password"]:
                    flag = 1
                    break

            '''
            flag  = 0
            if username == login_dict["username"] and password == login_dict["password"]:
                flag = 1
            # define response header
            self.set_header('Access-Control-Allow-Origin', self.request.headers.get('Origin', '*'))
            self.set_header('Access-Control-Allow-Methods', 'GET, POST')
            self.set_header('Content-Type', 'application/json')
            self.set_status(status_code=200, reason="Request successfully handled")
            response_json["status"] = "success"
            if flag == 1:
                response_json["login"] =  "success"
            else:
                response_json["login"] = "failure"

            #self.flush()
            #self.finish()
            self.write(response_json)

        except Exception as e:
            traceback.print_exc()
            end_time = datetime.now()
            self.write(response_json)

    get = post



''' 
tornado functions for starting an endpoint for each venue
each function will have a thread running so all of them are running at the same time
'''


def start_tornado_server():
    application = tornado.web.Application([(r"/login", User_Login_Handler)])
    application.listen(port)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    try:
        #es = Elasticsearch([es_host1], http_auth=('elastic', 'elasticpassword'))
        print("Starting Tornado Web Server for Login Service on " + str(port))
        #http_server = tornado.httpserver.HTTPServer(start_tornado_1())
        http_server = tornado.httpserver.HTTPServer(start_tornado_server())
        http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except:
        # logger.exception( "Exception occurred when trying to start tornado on " + str(options.port))
        traceback.print_exc()

