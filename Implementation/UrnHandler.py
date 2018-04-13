
class UrnHandler:

    def __init__(self):
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
            return sgtin_str

    @staticmethod
    def compute_checksum(level_str):
        if len(level_str) != 13:
            raise Exception("Invalid length")

        odd_sum = 0
        even_sum = 0
        for i, char in enumerate(level_str):
            j = i + 1
            if j % 2 == 0:
                even_sum += int(char)
            else:
                odd_sum += int(char)

        total_sum = (odd_sum * 3) + even_sum
        mod = total_sum % 10
        check_digit = 10 - mod
        if check_digit == 10:
            check_digit = 0
        return str(check_digit)
