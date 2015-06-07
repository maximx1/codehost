from app import app

app.config['UPLOAD_FOLDER'] = '/tmp/codehost/uploads/binaries'

app.run(host='0.0.0.0',debug=True)