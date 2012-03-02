import sqlite3
from bottle import route, run, debug, template

@route('/todo')
def todo_list():
  conn = sqlite3.connect('db/todo.db')
  cur = conn.cursor()
  cur.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
  result = cur.fetchall()
  output = template('tmpl/todo_list', rows=result)
  return output

run()
  
