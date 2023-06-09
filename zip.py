from flask import Flask, send_file
from flask import Flask, Response


app = Flask(__name__)

@app.route('/')
def download_txt():
    return Response(
        'Gotcha!!!',
        mimetype='text/plain',
        headers={'Content-disposition': 'attachment; filename=evil.exe'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',ssl_context=('/etc/letsencrypt/live/v4589.zip/cert.pem', '/etc/letsencrypt/live/v4589.zip/privkey.pem'), port=443)
