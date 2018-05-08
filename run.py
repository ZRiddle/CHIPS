# run.py
from flask import request, Response, render_template, Flask
import chips
import config
import json

# Logging setup
import logging

logging.basicConfig(
    level=config.LOGGING_LEVEL,
    format='[%(asctime)s] [CHIPS] [%(levelname)s] %(message)s',
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
    logging.info("Request for model: {}".format(model_name))

    if request.method == 'POST':
        data = request.get_json()
        res = chips.get_model_score(model_name, data)

        return Response(
            response=json.dumps(res),
            status=200,
            content_type='application/json'
        )

    elif request.method == 'GET':
        return chips.get_model_heartbeat(model_name)
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
