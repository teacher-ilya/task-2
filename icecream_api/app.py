from flask import Flask, request
from main import make_ice_cream

from typing import Dict


app = Flask(__name__)


@app.route('/', methods=['POST'])
def make_icecream() -> Dict[str, str]:
    return make_ice_cream(**request.json)


if __name__ == '__main__':
    app.run(debug=True)
