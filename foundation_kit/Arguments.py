import logging

OUTPUT_PARAMETER = 'output'
OUTPUT_PARAMETER_WINDOW_VALUE = 'window'


class Arguments:
    def __init__(self, prefix, arguments):
        options = {}
        options_length = len(arguments)

        i = 0

        try:
            while i < options_length:
                options[arguments[i]] = arguments[i + 1]
                i = i + 2
        except IndexError:
            print("ERROR: Supplied an argument without value. \n")

        self.options = options
        self.prefix = prefix

    def contains_option(self, option):
        return self.prefix + option in self.options.keys()

    def value_for_option(self, option):
        if self.contains_option(option):
            return self.options[self.prefix + option]
        else:
            logging.CRITICAL('Tried to read a value for argument not supplied.')

    def output_is_window(self):
        return self.contains_option(OUTPUT_PARAMETER) and (self.value_for_option(OUTPUT_PARAMETER) == OUTPUT_PARAMETER_WINDOW_VALUE)
