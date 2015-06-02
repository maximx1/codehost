import os
from app import app
from flask import send_from_directory
from app.security_helpers import *

@app.route('/uploads/<filename>')
@requires_auth
def retrieve_uploaded_file(filename):
  print(app.config['UPLOAD_FOLDER'] + "/" + filename)
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)