from flask import json, jsonify
from app import app
from app import db
from app.models import Menu

@app.route('/')
def home():
	return jsonify({ "app_status": "ok" })

@app.route('/menu')
def menu():
    record = Menu.query.first()
    if record:
        inc = 1
        body = '<html><body><center><h1>Menu</h1><table>'
        for item in Menu.query:
            if item:
               body += "<tr><td><h2>menu " + str(inc) + ': </h2><img src="https://loremflickr.com/320/240/' + item.name + '" /></td></tr>'
               inc+=1
        body += '</table></center></body></html>'
        status = 200
    else:
        body = jsonify({ "error": "Sorry, the service is not available today." })
        status = 404

    return body, status
