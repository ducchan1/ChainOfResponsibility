from SGTINHandler import SGTINHandler
from BaseHandler import BaseHandler


def build_chain_of_responsibility_for_SGTIN():
    handler = SGTINHandler()
    handler.add_handler(BaseHandler())
    return handler
