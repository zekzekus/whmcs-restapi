# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, json
from pywhmcs import invoke
import logging as log


app = Flask(__name__)
app.config.from_object("whmcsrestapi.local_settings")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/client/", methods=["GET"])
def clients():
    return i("getclients", {})


@app.route("/client/<int:clientid>/",
           methods=["GET", "POST", "PUT", "DELETE", "HEAD"])
def client(clientid):
    if request.method == 'GET':
        app.logger.debug("ClientId: %d" % clientid)
        return i("getclientsdetails", {'clientid': clientid, 'stats': True})
    elif request.method == 'POST':
        app.logger.debug(request.form)
        data_dict = {}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("addclient", data_dict)
    elif request.method == 'PUT':
        app.logger.debug(request.form)
        data_dict = {'clientid': clientid}
        for data in request.form.items():
            data_dict.update({data[0]: data[1]})
        return i("updateclient", data_dict)
    elif request.method == 'DELETE':
        app.logger.debug("ClientId: %d" % clientid)
        return i("deleteclient", {'clientid': clientid})


def i(action, params):
    return jsonify(json.loads(invoke(app.config["WHMCS_URL"],
                              app.config["API_USER"],
                              app.config["API_PASS"],
                              action,
                              app.config["RESPONSE_TYPE"],
                              params)[1]))


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
