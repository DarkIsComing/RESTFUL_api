from flask_script import Manager,Command
import click
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.api_v1 import create_app, db
from app.api_v1.models.user import User

app=create_app()    #实例化Flask类对象app
app.config.from_object('config')
api=Api(app)


api.add_resource()

if __name__=="__main__":
    app.run()