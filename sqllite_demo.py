#-*- coding: utf-8 -*-
'''
Running:

  PYTHONPATH=. python examples/lineApp.py

'''

from flask import Flask, abort, redirect, url_for
from line_login import line_login
from lineapi import lineapi

import sqlite3

app = Flask(__name__, static_folder='./static')


@app.route('/')
def index():
    conn = sqlite3.connect('line_api.db')
    c = conn.cursor()
    id = 2
    c.execute("SELECT count(line_id) FROM line_authtoken WHERE line_id = %s ",id)
    count = c.fetchone()
    if (count == 0 ) :
        c.execute("INSERT INTO line_authtoken (line_id, line_authtoken ) VALUES ('2','BUY')")
    else:
        c.execute("UPDATE line_authtoken SET  line_authtoken = 'count' ")
    conn.commit()
    return "YES"
if __name__ == '__main__':
 
  
  app.run(debug=True)



