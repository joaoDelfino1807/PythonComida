from server import app
from flaskext.mysql import MySQL
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1807'
app.config['MYSQL_DATABASE_DB'] = 'comidarest'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
