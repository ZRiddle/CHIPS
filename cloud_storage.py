import os
import logging
import pickle

from google.cloud import storage
CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']


class FileStorage(object):
    """
    directory: project_hash string
    filename: ['data', 'model', 'column', 'column_ohe']
    """

    def __init__(self):
        gcs = storage.Client()
        self.bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

    def save_pickle(self, directory, filename, obj):
        dir = directory + '/' + filename + '.pkl'
        logging.info("Saving pkl: {}".format(dir))
        blob = self.bucket.blob(dir)
        blob.upload_from_string(pickle.dumps(obj))
        return

    def load_pickle(self, directory, filename):
        dir = directory + '/' + filename + '.pkl'
        logging.info("Loading pkl: {}".format(dir))
        blob = self.bucket.blob(dir)
        obj = pickle.loads(blob.download_as_string())
        return obj
