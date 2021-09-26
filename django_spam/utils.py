class Colour:
    """
    Color output in terminal so warnings/errors stick out.
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def text(cls, txt: str, status: str = None) -> str:
        """colorize specific text

        :param txt:                     text printed to console
        :param status:                  the type of status depends on the color

        :return:                        colorized text string
        """
        if status == "fail":
            return cls.FAIL + txt + cls.ENDC
        elif status == "ok":
            return cls.OKGREEN + txt + cls.ENDC
        elif status == "warn":
            return cls.WARNING + txt + cls.ENDC
        else:
            return txt
