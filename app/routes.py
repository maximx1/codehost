import os
from app import app
from flask import send_from_directory
from app.security_helpers import *
from flask import render_template
from flask import redirect
from flask import url_for
from werkzeug.utils import secure_filename
from app.utils import *

@app.route('/uploads/<filename>')
@auth_basic
def retrieve_uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
@auth_basic
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if file and allowed_file(file.filename):
      print("here")
      filename = secure_filename(file.filename)
      print(filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return render_template("upload_file.html", message=file.filename + " uploaded successfully")

@app.route('/', methods=['GET'])
@auth_basic
def display_upload_page():
  return render_template("upload_file.html", message="")