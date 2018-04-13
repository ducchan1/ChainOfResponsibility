from SGTINHandler import SGTINHandler


class BaseHandler(SGTINHandler):

    def __init__(self):
        super(BaseHandler, self).__init__()

    def to_human_readable(self, sgtin_str):
        return sgtin_str
