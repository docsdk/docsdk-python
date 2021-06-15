from docsdk.docsdkrestclient import *
from docsdk.task import Task
from docsdk.job import Job
from docsdk.webhook import Webhook

def configure(**config):
    """
    Configure the REST Client With Latest API Key and Mode
    :return:
    """
    set_config(**config)


def default():
    """
    Configure the REST Client With Default API Key and Mode
    :return:
    """
    default_client()

