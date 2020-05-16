import MySQLdb
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

conn = MySQLdb.connect( host    =   "localhost",
                        user    =   "username",
                        passwd  =   "passwd",
                        db      =   "go"
                        )
cursor = conn.cursor(MySQLdb.cursors.DictCursor)

@app.route('/')
def index():
    return render_template('index.html');


@app.route('/getUsers', methods=['GET', 'POST'])
def getUsers():
    search = ''
    if request.method == 'POST':
        postData = request.get_json()
        search  = postData.get('search', '')

    sql = "SELECT * FROM users WHERE CONCAT_WS(' ', name, surname) LIKE %s" 
    cursor.execute(sql, ("%" + search + "%",))
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)