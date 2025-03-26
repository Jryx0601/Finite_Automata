from flask import request,jsonify
from config import app
from dfa_checker import dfa_checker


@app.route('/get_valid',methods = ['GET'])
def get_dfa_valid():
    string = request.json.get('Strings')
    types = request.json.get('Types')
    results,state = dfa_checker(string,types)
    return jsonify({'result':results,
                    'States':state})

if __name__ == "__main__":
    app.run(debug=True)