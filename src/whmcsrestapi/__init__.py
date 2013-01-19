# -*- coding: utf-8 -*-
from flask import Flask, request
from pywhmcs import invoke
import logging as log


# Global configurations
WHMCS_URL = "http://manage.mysirket.com/includes/api.php"
API_USER = "apiuser"
API_PASS = "1q2w3e4r"
RESPONSE_TYPE = "json"

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/client/", methods=["GET"])
def get_clients():
    return i("getclients", {})


@app.route("/client/<int:clientid>/",
           methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
def client(clientid):
    if request.method == 'GET':
        return i("getclientsdetails", {'clientid': clientid, 'stats': True})
    elif request.method == 'POST':
        log.debug(request.form)
        data_dict = {}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("addclient", data_dict)
    elif request.method == 'PUT':
        log.debug(request.form)
        data_dict = {'clientid': clientid}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("updateclient", data_dict)
    elif request.method == 'DELETE':
        return i("deleteclient", {'clientid': clientid})


def i(action, params):
    return invoke(WHMCS_URL,
                  API_USER,
                  API_PASS,
                  action,
                  RESPONSE_TYPE,
                  params)[1]


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
