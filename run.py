# run.py
from flask import request
import chips
import config

# Logging setup
import logging

logging.basicConfig(
    level=config.LOGGING_LEVEL,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

app = chips.create_app(config)


@app.route('/<model_name>', methods=['GET', 'POST'])
def call_model(model_name):
    """
    GET checks if the model service is alive
    POST pings the model service for a score
    """

    if request.method == 'GET':
        data = request.data
        return chips.get_model_score(model_name, data)

    elif request.method == 'POST':
        return chips.get_model_heartbeat(model_name)

    else:
        # return error
        return


if __name__ == '__main__':
    app.run(port=8006)
