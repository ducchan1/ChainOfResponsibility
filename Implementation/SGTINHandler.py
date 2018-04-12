from BaseHandler import BaseHandler


class SGTINHandler:
    def __init__(self):
        self.handlers = [BaseHandler]
        self.current_handler = 0

    def to_human_readable(self, sgtin_str):
        human_readable = None
        if self.current_handler is not None:
            handler = self.handlers[self.current_handler]
            if self.current_handler < len(self.handlers) - 1:
                self.current_handler += 1
            else:
                self.current_handler = 0

            human_readable = handler.to_human_readable(sgtin_str)

        return human_readable
