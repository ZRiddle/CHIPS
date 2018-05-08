"""
Sample code to setup new hosting
This should be broken out into multiple scripts...
I am combining them now for show-and-tell purposes
"""
from flask import Flask, request, Response, json
import logging

# Logging setup
# TODO - make debug config driven
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [Titanic] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# This should be in a scoring file                 #
# score_model.py
import numpy as np
from cloud_storage import FileStorage

# Load model once into global memory
model = FileStorage().load_pickle('titanic', 'model')


def score(data):
    # Out model takes: ['Age', 'SibSp', 'Fare']
    # Parse and clean data
    x = np.array(data['Age'], data['SibSp'], data['Fare'])

    # should probably handle NAs

    # need to reformat for single row prediction and only return the 1st element
    return model.predict_proba(x[1].reshape(1, -1))[1]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def call_model():
    """
    GET checks if the model service is alive
    POST pings the model service for a score
    """

    if request.method == 'GET':
        return Response("Titanic model is ready", status=200)

    else:
        data = request.get_json()
        logging.info("new POST request")
        logging.info(data)

        s = score(data)
        logging.info("Model Score = {}".format(s))

        output = {
            "Probability": s,
            "Prediction": 0 if s < 0.5 else 1,
            "ModelType": "RandomForestClassifier",
            "ModelName": "Titanic"
        }

        return Response(
            response=json.dumps(output),
            status=200,
            mimetype='application/json'
        )


if __name__ == '__main__':
    app.run(port=8007)
