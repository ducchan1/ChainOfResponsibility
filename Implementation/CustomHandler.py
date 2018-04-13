from SGTINHandler import SGTINHandler


class CustomHandler(SGTINHandler):

    def __init__(self):
        super(CustomHandler, self).__init__()
        self.identifier = "level:"
        self.splitter = "."
        self.sn_identifier = "Sn:"
        self.level_identifier = "(01)"
        self.serial_number_identifier = "(21)"

    def to_human_readable(self, sgtin_str):
        if self.identifier in sgtin_str and self.sn_identifier in sgtin_str:
            # parse the string and convert it
            gtin_components = sgtin_str[len(self.identifier):].split(self.splitter)
            if len(gtin_components) is not 2:
                raise Exception("Badly formatted string")
            string_to_return = self.level_identifier
            level_str = gtin_components[0]
            serial_str = gtin_components[1][len(self.sn_identifier):]
            string_to_return += level_str + self.serial_number_identifier + serial_str
            return string_to_return
        else:
            # pass on to the next handler
            return super(CustomHandler, self).to_human_readable(sgtin_str)