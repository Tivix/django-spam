import abc

class AbstractSpam(abc.ABC):
    name: str = ""
    url: str = ""

    @classmethod
    def to_readable(cls) -> str:
        return cls.name.lower().replace(" ", "_")


class VaderBreathing(AbstractSpam):
    name = "Darth Vader Breathing"
    url = "https://www.youtube.com/watch?v=un8FAjXWOBY"


class BouncingDVDLogo(AbstractSpam):
    name = "Bouncing DVD Logo"
    url = "https://www.youtube.com/watch?v=5mGuCdlCcNM"


class MulletGuy(AbstractSpam):
    name = "Whistling Mullet Guy"
    url = "https://www.youtube.com/watch?v=Sbhoym9yzVQ"


class ScreamingGuy(AbstractSpam):
    name = "Screaming Guy"
    url = "https://www.youtube.com/watch?v=CRcYlE3i_-4"


class FaceSong(AbstractSpam):
    name = "Awesome Face Song"
    url = "https://www.youtube.com/watch?v=WNeni1lbzgY"


class ScreamingSheep(AbstractSpam):
    name = "Screaming Sheep"
    url = "https://www.youtube.com/watch?v=SjHUb7NSrNk"


class SaxGuy(AbstractSpam):
    name = "Epic Sax Guy"
    url = "https://www.youtube.com/watch?v=kxopViU98Xo"


class CrabRave(AbstractSpam):
    name = "Crab Rave"
    url = "https://www.youtube.com/watch?v=-50NdPawLVY"


class WiiMusic(AbstractSpam):
    name = "Wii Theme Music"
    url = "https://www.youtube.com/watch?v=Twi92KYddW4"


class Nothing(AbstractSpam):
    name = "Nothing"
    url = "https://www.youtube.com/watch?v=fx2Z5ZD_Rbo"


class Asmr(AbstractSpam):
    name = "ASMR"
    url = "https://www.youtube.com/watch?v=jbAy9MwBR-I"


class JoePera(AbstractSpam):
    name = "Joe Pera Talks You To Sleep"
    url = "https://www.youtube.com/watch?v=91wX0NRjJqg"


SPAM_ENUMS = [
    VaderBreathing,
    Nothing,
    MulletGuy,
    ScreamingGuy,
    FaceSong,
    ScreamingSheep,
    SaxGuy,
    CrabRave,
    WiiMusic,
    BouncingDVDLogo,
    Asmr,
    JoePera,
]
