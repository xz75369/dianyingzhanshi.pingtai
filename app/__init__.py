# _*_ coding: utf-8 _*_
__author__ = 'baiyiheiyue'
__data__ = '2018/7/17 21.28'


from flask import Flask

app = Flask(__name__, template_folder='./templates')
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")