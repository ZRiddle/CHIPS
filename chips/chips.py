# chips/chips.py
import logging
from flask import request


def get_model_score(model_name, data):
    """
    Routes to the correct model within the microservice framework

    :param model_name: model name in url (str)
    :param data: data to pass on (json)
    :return: model return info (json)
    """

    logging.info("get_model_score for model: {}".format(model_name))
    # TODO - add code here

    return


def get_model_heartbeat(model_name):
    """

    :param model_name: model name in url (str)
    :return: heartbeat info (json)
    """

    logging.info("get_model_heartbeat for model: {}".format(model_name))
    # TODO - add code here

    return
