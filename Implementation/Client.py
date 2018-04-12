from SGTINHandler import SGTINHandler


class Client:
    def __init__(self):
        self.handler = SGTINHandler()

    def print_sgtin_to_human_readable(self, sgtin_str):
        print self.handler.to_human_readable(sgtin_str)
