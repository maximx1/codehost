from flask import Flask

UPLOAD_FOLDER = '/tmp/codehost/uploads/binaries'
#ALLOWED_EXTENSIONS = set(['.zip', '.tar.gz'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import routes