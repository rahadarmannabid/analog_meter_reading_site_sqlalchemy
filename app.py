from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
#import pymysql
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/meter_reading'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
class aidynamicresource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(20), nullable=False)
    tower_id = db.Column(db.String(20), nullable=False)
    date_and_time = db.Column(db.String(6), nullable=False)
    meter_reading = db.Column(db.Integer, nullable=True)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action_page.php', methods=['GET','POST'])
def login():

    if(request.method=='POST'):

        district = request.form.get('district')
        tower_id = request.form.get('tower_id')
        date_and_time = request.form.get('date_and_time')
        meter_reading = request.form.get('meter_reading')
        entry = aidynamicresource(district=district, tower_id = tower_id, date_and_time = date_and_time, meter_reading= meter_reading)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html')