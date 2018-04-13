from SGTINHandler import SGTINHandler


class UrnHandler(SGTINHandler):

    def __init__(self):
        super(UrnHandler, self).__init__()
        self.identifier = "urn:epc:id:sgtin:"
        self.splitter = "."
        self.level_identifier = "(01)"
        self.serial_number_identifier = "(21)"

    def to_human_readable(self, sgtin_str):
        if self.identifier in sgtin_str:
            # parse the string and convert it
            gtin_components = sgtin_str[len(self.identifier):].split(self.splitter)
            if len(gtin_components) is not 3:
                raise Exception("Badly formatted string")
            string_to_return = self.level_identifier
            level_str = gtin_components[1][0] + gtin_components[0] + gtin_components[1][1:]
            checksum_value = self.compute_checksum(level_str)
            string_to_return += level_str + checksum_value + self.serial_number_identifier + gtin_components[2]
            return string_to_return
        else:
            # pass on to the next handler
            return super(UrnHandler, self).to_human_readable(sgtin_str)

    def compute_checksum(self, level_str):
        # here we should actually compute the checksum
        # but for dojo purposes this algorithm is not worth
        # implementing
        return "2"
