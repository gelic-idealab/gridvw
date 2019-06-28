import datetime
import json
from uuid import uuid4
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, JSON, DateTime
engine = create_engine('sqlite:///database.db', echo = True)
meta = MetaData()

views = Table(
   'views', meta, 
   Column('id', String, primary_key = True), 
   Column('user_id', String),
   Column('create_date', DateTime),
   Column('modify_date',DateTime),
   Column('view_config', JSON)
)
meta.create_all(engine)

engine = create_engine('sqlite:///database.db')

app = Flask(__name__)


@app.route('/views', methods=['GET','POST','PATCH','DELETE'])
def views_api():
    
    if request.method == 'GET':

        view_id = request.args.get('id')

        query = views.select().where(views.c.id==view_id)
        conn = engine.connect()
        result = conn.execute(query)

        first_row = dict(result.fetchone())

        return jsonify(first_row)
    

    if request.method == 'POST':
        view_id = str(uuid4())
        view_data = request.json
        user_id = view_data.get('user_id')
        view_config = json.dumps(view_data.get('view_config'))
        create_date = datetime.datetime.now()

        new = views.insert().values(id=view_id, user_id=user_id, create_date=create_date, modify_date=create_date, view_config=view_config)
        conn = engine.connect()
        conn.execute(new)
        
        return jsonify({'msg':f'View created for {view_id}'})

    if request.method == 'PATCH':
        view_data = request.json
        view_id = view_data.get('view_id')
        user_id = view_data.get('user_id')
        view_config = json.dumps(view_data.get('view_config'))
        modify_date = datetime.datetime.now()

        update = views.update().where(views.c.id==view_id).values(modify_date=modify_date, view_config=view_config)

        conn = engine.connect()
        conn.execute(update)

        return jsonify({'msg':f'Updated {view_id}'})

    
    if request.method == 'DELETE':
        view_id = request.args.get('id')

        query = views.delete().where(views.c.id==view_id)
        conn = engine.connect()
        result = conn.execute(query)

        return jsonify(dict(result))

if __name__=='__main__':
    app.run()