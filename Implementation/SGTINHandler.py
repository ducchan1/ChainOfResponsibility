

class SGTINHandler(object):
    def __init__(self):
        self.next_handler = None

    def to_human_readable(self, sgtin_str):
        return self.next_handler.to_human_readable(sgtin_str)

    def add_handler(self, new_handler):
        if self.next_handler is not None:
            self.next_handler.add_handler(new_handler)
        else:
            self.next_handler = new_handler

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
