def allowed_file(filename):
  return True in list(map(lambda x: filename.endswith(x), set(['zip', 'tar.gz'])))