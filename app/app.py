import os

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__, static_url_path='', static_folder="static")
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

APP.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    'manager@contextiapgs', 'supersecretpass', 'contextiapgs.postgres.database.azure.com', 'eventregistration'
) + '?sslmode=require'

# initialize the database connection
DB = SQLAlchemy(APP)

# initialize database migration management
MIGRATE = Migrate(APP, DB)

from models import *


@APP.route('/')
def view_registered_guests():
    return APP.send_static_file('dist/index.html')

@APP.route('/guest')
def view_registered_guests():
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)
#

@APP.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')


@APP.route('/register', methods = ['POST'])
def register_guest():
    name = request.form.get('name')
    email = request.form.get('email')
    partysize = request.form.get('partysize')
    if not partysize or partysize=='':
        partysize = 1

    guest = Guest(name, email, partysize)
    DB.session.add(guest)
    DB.session.commit()

    return render_template('guest_confirmation.html',
        name=name, email=email, partysize=partysize)
