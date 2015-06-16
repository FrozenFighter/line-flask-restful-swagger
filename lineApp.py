#-*- coding: utf-8 -*-
'''
Running:

  PYTHONPATH=. python examples/lineApp.py

'''

from flask import Flask, abort, redirect, url_for
from line_login import line_login
from lineapi import lineapi

app = Flask(__name__, static_folder='./static')


@app.route('/')
def index():
    return redirect('/line/docs')
if __name__ == '__main__':
 
  app.register_blueprint(line_login)
  app.register_blueprint(lineapi,url_prefix='/line')
  app.run(debug=True)



