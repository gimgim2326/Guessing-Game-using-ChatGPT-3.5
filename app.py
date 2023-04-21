from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.secret_key = 'SecretKey'

if __name__ == '__main__':
    #app.run(debug=True, port=8080)
    app.run(host='0.0.0.0', port=8080)