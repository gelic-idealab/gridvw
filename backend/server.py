import datetime
import json
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, JSON
engine = create_engine('sqlite:///database.db', echo = True)
meta = MetaData()

views = Table(
   'views', meta, 
   Column('view_id', Integer, primary_key = True), 
   Column('user_id', String),
   Column('create_date', Date),
   Column('view_config', JSON)
)
meta.create_all(engine)

engine = create_engine('sqlite:///database.db')

app = Flask(__name__)

@app.route('/')
def index():
    return 200

@app.route('/load', methods=['GET'])
def load():

    if request.method == 'GET':

        view_id = request.args.get('view_id')

        query = views.select().where(views.c.view_id==view_id)
        conn = engine.connect()
        result = conn.execute(query)

        first_row = dict(result.fetchone())

        return jsonify(first_row)

@app.route('/save', methods=['POST','PATCH'])
def save():

    if request.method == 'POST':
        view_data = request.json
        user_id = view_data.get('user_id')
        view_config = view_data.get('view_config')
        create_date = datetime.datetime.now()

        new = views.insert().values(user_id=user_id, create_date=create_date, view_config=json.dumps(view_config))
        conn = engine.connect()
        conn.execute(new)
        
        return jsonify({'msg':'Inserted view in table'})

    
if __name__=='__main__':
    app.run()