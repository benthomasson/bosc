
"""
Here we define the message types
"""

from collections import namedtuple


Hello = namedtuple('Hello', ['message'])


Client = namedtuple('Client', ['id'])
Message = namedtuple('Message', ['id', 'client_id', 'messageType', 'data'])


def serialize(message):
    """
    Serializes a message to a string.
    """

    return ""


"""

class Message(object):

    def __init__(self):
        "doc string"
        self.id = None
        self.client_id = None
        self.messageType = None
        self.data = None
"""
