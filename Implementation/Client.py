

class Client:
    def __init__(self, handler_root):
        self.handler = handler_root

    def print_sgtin_to_human_readable(self, sgtin_str):
        print self.handler.to_human_readable(sgtin_str)
