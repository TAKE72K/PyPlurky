# coding=utf-8


class PythonError(Exception):
    def __init__(self, message):
        super(PythonError, self).__init__()

        self.message = message

    def __str__(self):
        return '%s' % (self.message)
