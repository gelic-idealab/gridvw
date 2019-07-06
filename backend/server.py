import datetime
import json
from uuid import uuid4
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, JSON, DateTime, Binary, BLOB
engine = create_engine('sqlite:///database.db', echo = True)
meta = MetaData()

views = Table(
   'views', meta, 
   Column('id', String), 
   Column('user_id', String),
   Column('create_date', DateTime),
   Column('modify_date',DateTime),      
   Column('view_config', JSON),
   Column('file', Binary)
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
        view_data = json.loads(request.form.get('view_data'))
        view_id = str(uuid4())
        user_id = view_data.get('user_id')
        view_config = json.dumps(view_data.get('view_config'))
        create_date = datetime.datetime.now()
        kwargs = {"create_date": create_date, "view_config":view_config, "user_id":user_id, "id":view_id, "modify_date":create_date}

        blob_file = request.files['file']
        print("FILE:"+str(blob_file))

        if blob_file: kwargs.update({"file":blob_file.read()})
        
        new = views.insert().values(kwargs)
        # new = views.insert().values(id=view_id, user_id=user_id, create_date=create_date, modify_date=create_date, view_config=view_config)
        conn = engine.connect()
        conn.execute(new)
        
        return jsonify({'msg':f'View created for {view_id}'})


    if request.method == 'PATCH':
        view_data = request.json
        view_id = view_data.get('id')
        user_id = view_data.get('user_id')
        view_config = json.dumps(view_data.get('view_config'))
        modify_date = datetime.datetime.now()
        
        kwargs = {"modify_date":modify_date, "view_config":view_config}

        if user_id: kwargs.update({"user_id":user_id})
        
        update = views.update().where(views.c.id==view_id).values(kwargs)
        
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