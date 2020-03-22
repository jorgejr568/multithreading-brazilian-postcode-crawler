import re


class NumberFormatter:
    @staticmethod
    def only_numbers(str):
        number_groups = re.findall(r'\d+', str)
        return ''.join(number_groups)


class PostcodeFormatter:
    @staticmethod
    def postcode(postcode):
        postcode = str(postcode)
        postcode = NumberFormatter.only_numbers(postcode)
        return postcode.rjust(8, '0')


class FileFormatter:
    @staticmethod
    def remove_extension(filename):
        filename = str(filename)
        extension = re.findall(r'\..+', filename)[-1]
        filename = filename[0: len(filename) - len(extension)]

        return filename
