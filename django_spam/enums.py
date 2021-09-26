class SpamBase:
    name = ""
    url = ""

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def to_readable(cls) -> str:
        return cls.name.lower().replace(" ", "_")


class VaderBreathing(SpamBase):
    name = "Darth Vader Breathing"
    url = "https://www.youtube.com/watch?v=un8FAjXWOBY"


class Yodelling(SpamBase):
    name = "Yodelling"
    url = "https://www.youtube.com/watch?v=Lxt0_YrQs0M"


class MulletGuy(SpamBase):
    name = "Whistling Mullet Guy"
    url = "https://www.youtube.com/watch?v=Sbhoym9yzVQ"


class ScreamingGuy(SpamBase):
    name = "Screaming Guy"
    url = "https://www.youtube.com/watch?v=CRcYlE3i_-4"


class FaceSong(SpamBase):
    name = "Awesome Face Song"
    url = "https://www.youtube.com/watch?v=WNeni1lbzgY"


class ScreamingSheep(SpamBase):
    name = "Screaming Sheep"
    url = "https://www.youtube.com/watch?v=SjHUb7NSrNk"


class SaxGuy(SpamBase):
    name = "Epic Sax Guy"
    url = "https://www.youtube.com/watch?v=kxopViU98Xo"


class CrabRave(SpamBase):
    name = "Crab Rave"
    url = "https://www.youtube.com/watch?v=-50NdPawLVY"


class WiiMusic(SpamBase):
    name = "Wii Theme Music"
    url = "https://www.youtube.com/watch?v=Twi92KYddW4"


class NyonCat(SpamBase):
    name = "Nyon Cat"
    url = "https://www.youtube.com/watch?v=wZZ7oFKsKzY"


class Asmr(SpamBase):
    name = "ASMR"
    url = "https://www.youtube.com/watch?v=jbAy9MwBR-I"


class HeMan(SpamBase):
    name = "He-man Heyeayea"
    url = "https://www.youtube.com/watch?v=eh7lp9umG2I"


SPAM_ENUMS = [
    VaderBreathing,
    Yodelling,
    MulletGuy,
    ScreamingGuy,
    FaceSong,
    ScreamingSheep,
    SaxGuy,
    CrabRave,
    WiiMusic,
    NyonCat,
    Asmr,
    HeMan,
]
