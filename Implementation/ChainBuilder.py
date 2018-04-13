from SGTINHandler import SGTINHandler
from BaseHandler import BaseHandler
from UrnHandler import UrnHandler
from CustomHandler import CustomHandler


def build_chain_of_responsibility_for_SGTIN():
    handler = SGTINHandler()

    # handlers must be in the right other in this case
    # since the BaseHandler handles just about everything
    handler.add_handler(UrnHandler())
    handler.add_handler(CustomHandler())
    handler.add_handler(BaseHandler())
    return handler
