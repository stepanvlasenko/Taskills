from flask import Flask, request
from flask_cors import CORS

from models import Sight
from crud import model_crud

app = Flask(__name__)
CORS(app)

sightAPI = model_crud(Sight)

@app.get('/')
def apiBase():
    return f'Successfully work on url {request.base_url} and caught request with this agruments {dict(request.args)}'

@app.get('/sights')
def apiSights():
    args = request.args
    if ('id' not in args.keys()):
        return sightAPI['read_all']()
    else:
        return sightAPI['read'](args['id'])

app.run(debug=True)