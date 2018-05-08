# chips/chips.py
import logging
import requests

HOST_URL = "prog-chips.appspot.com"


def _create_url(name):
    url = "https://{}-dot-{}".format(name, HOST_URL)
    logging.info("formatting url: {}".format(url))
    return url


def get_model_score(model_name, data):
    """
    Routes to the correct model within the microservice framework

    :param model_name: model name in url (str)
    :param data: data to pass on (json)
    :return: model return info (json)
    """

    logging.info("get_model_score for model: {}".format(model_name))
    # TODO - add code here
    url = _create_url(model_name)
    headers = {'Content-type': 'application/json'}

    res = requests.post(url, json=data, headers=headers)
    logging.info("Response from {}: {}".format(model_name, res.json()))

    return res.json()


def get_model_heartbeat(model_name):
    """

    :param model_name: model name in url (str)
    :return: heartbeat info (json)
    """

    logging.info("get_model_heartbeat for model: {}".format(model_name))
    # TODO - add code here
    url = _create_url(model_name)
    res = requests.get(url)

    return res.json()

if __name__ == '__main__':
    pass
