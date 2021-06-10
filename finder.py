from ip2geotools.databases.noncommercial import DbIpCity
from flask import Flask, request
from flask import Blueprint

app = Flask(__name__)
location = Blueprint("location", __name__)


@location.route('/location_finder', methods=["GET"])
def find_location():
    body = request.args
    ip = body.get('ip_address')
    response = DbIpCity.get(f'{ip}', api_key='free')
    return response
