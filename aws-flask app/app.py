from flask import Flask, render_template, request
from upload import *
import socket

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello Everyone, this application is served from {}".format(socket.gethostname())

@app.route("/upload", methods=['POST', 'GET'])
def upload():
        if request.method == 'POST':
            f = request.files['file']
            print(f)
            file_name = upload_my_file(f)
            print(file_name)
       
        return render_template('uploads3.html',myhost=socket.gethostname())

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
