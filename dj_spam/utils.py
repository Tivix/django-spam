

class ColorMe(object):
    """
    Color output in terminal so warnings/errors stick out.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def color_text(cls, txt, status):
        if status == 'fail':
            return cls.FAIL + txt + cls.ENDC
        elif status == 'ok':
            return cls.OKGREEN + txt + cls.ENDC
        elif status == 'warn':
            return cls.WARNING + txt + cls.ENDC
        else:
            return txt
