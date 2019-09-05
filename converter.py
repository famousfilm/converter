class Converter(object):
    def __init__(self):
        self.conversion_table = {
            "kilometers": {"type": "length",
                           "to": lambda x: x * 1,
                           "from": lambda x: x * 1},
            "feet": {"type": "length",
                     "to": lambda x: x / 3280.84,
                     "from": lambda x: x * 3280.84},
            "inches": {"type": "length",
                       "to": lambda x: x / 39370.079,
                       "from": lambda x: x * 39370.079},
            "miles": {"type": "length",
                      "to": lambda x: x * 1.609344,
                      "from": lambda x: x / 1.609344},
            "pounds": {"type": "weight",
                       "to": lambda x: x / 2.20462,
                       "from": lambda x: x * 2.20462},
            "tons": {"type": "weight",
                     "to": lambda x: x * 907.185,
                     "from": lambda x: x / 907.185},
            "kilograms": {"type": "weight",
                          "to": lambda x: x * 1,
                          "from": lambda x: x * 1},
            "Fahrenheit": {"type": "temperature",
                           "to": lambda f: (f - 32) * 5/9,
                           "from": lambda c: (c * 9/5) + 32},
            "Celsius": {"type": "temperature",
                        "to": lambda x: x * 1,
                        "from": lambda x: x * 1},
        }

    def convert(self, source: str, destination: str, units: float):
        if source not in self.conversion_table:
            raise Exception(f"{source} is invalid.")
        elif destination not in self.conversion_table:
            raise Exception(f"{destination} is invalid.")
        convert_source = self.conversion_table[source]
        convert_destination = self.conversion_table[destination]
        if convert_source["type"] is not convert_destination["type"]:
            raise Exception("Inputs must be the same type.")
        converted = convert_source["to"](units)
        return convert_destination["from"](converted)
