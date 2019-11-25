# -*- coding: utf-8 -*-
"""

@author: alpcan
"""
import json
import time
import cgi
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
# import helper data reading functions
from pricetempreader import *

# Main parameters
HOST_NAME = 'localhost'
PORT_NUMBER = 8080


class MyHandler(BaseHTTPRequestHandler):
    ''' HTTP request handler class extending BaseHTTPRequestHandler '''

    def myparse_getrequest(self):
        ''' GET request: parse the path and extract query  '''
        parsed_path = urllib.parse.urlparse(self.path)
        pathlist = parsed_path.path.split('/')[1:]
        querylist = parsed_path.query.split('&')
        querydict = {}
        for item in querylist:
            keyvalpair = item.split('=')
            if len(keyvalpair) > 1:
                querydict[keyvalpair[0]] = keyvalpair[1]

        # return path components in a list (ordered)
        # and query variables&values in a dictionary (unordered)
        return pathlist, querydict

    def myparse_postrequest(self):
        ''' POST request: parse the form data posted  '''
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        postdict = {}
        for field in list(form.keys()):
            postdict[field] = form.getvalue(field)

        return postdict

    # respond to a GET request
    def do_GET(self):
        ''' responds to a GET request '''
        price_list = import_pricedata()
        # send response
        self.send_response(200)
        self.end_headers()

        pathlist, querydict = self.myparse_getrequest()
#        # replace this part with application logic ----------------
#        # send back parsed request content for debugging
#        pathlist_string = ''.join(pathlist)
#        querydict_bytes = json.dumps(querydict).encode()
        time_index = int(querydict['time'])
        print("received_time_index",time_index)
        price = price_list[time_index]
#        byte_send=json.dumps(querydict)
        #print(byte_send)
        print("send price", price)
        self.wfile.write(str(price).encode())
        return

    # respond to a POST request
    def do_POST(self):

        # Begin the response
        self.send_response(200)
        self.end_headers()

        postdict = self.myparse_postrequest()
        print(postdict)

        # replace this part with application logic ----------------
        # send back parsed post content for
        postdict_bytes = json.dumps(postdict).encode()
        self.wfile.write(postdict_bytes)
        return


def ServerApp():
    ''' this function implements the server application logic '''
    pass


#################################################
##              Main


httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHandler)
print((time.asctime(), "Server Starts - {0}:{1}".format(HOST_NAME, PORT_NUMBER)))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print((time.asctime(), "Server Stops - {0}:{1}" % (HOST_NAME, PORT_NUMBER)))
