# run.py
from flask import request, Response, render_template, Flask
import chips
import config


# Logging setup
import logging

logging.basicConfig(
    level=config.LOGGING_LEVEL,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)


# TODO - Default page
@app.route('/')
def default():
    return render_template("index.html")


@app.route('/<model_name>', methods=['GET', 'POST'])
def call_model(model_name):
    """
    GET checks if the model service is alive
    POST pings the model service for a score
    """

    if request.method == 'POST':
        data = request.data
        return chips.get_model_score(model_name, data)

    elif request.method == 'GET':
        return render_template("index.html")
        #return chips.get_model_heartbeat(model_name)

    else:
        # return error
        response = Response(
            "Only POST and GET are supported",
            status='501',
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run(port=8006)
