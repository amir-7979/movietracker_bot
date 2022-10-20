from dataclasses import dataclass
from typing import Any
from typing import List


@dataclass
class Link:
    link: str
    info: str
    qualitySample: str
    sourceName: str
    pageLink: str
    season: int
    episode: int

    @staticmethod
    def from_dict(obj: Any) -> 'Link':
        _link = str(obj.get("link"))
        _info = str(obj.get("info"))
        _qualitySample = str(obj.get("qualitySample"))
        _sourceName = str(obj.get("sourceName"))
        _pageLink = str(obj.get("pageLink"))
        _season = int(obj.get("season"))
        _episode = int(obj.get("episode"))
        return Link(_link, _info, _qualitySample, _sourceName, _pageLink, _season, _episode)


@dataclass
class Poster:
    url: str
    info: str
    size: int

    @staticmethod
    def from_dict(obj: Any) -> 'Poster':
        _url = str(obj.get("url"))
        _info = str(obj.get("info"))
        _size = int(obj.get("size"))
        return Poster(_url, _info, _size)

@dataclass
class Episode:
    episodeNumber: int
    title: str
    released: str
    releaseStamp: str
    duration: str
    imdbRating: str
    imdbID: str
    links: List[Link]

    @staticmethod
    def from_dict(obj: Any) -> 'Episode':
        _episodeNumber = int(obj.get("episodeNumber"))
        _title = str(obj.get("title"))
        _released = str(obj.get("released"))
        _releaseStamp = str(obj.get("releaseStamp"))
        _duration = str(obj.get("duration"))
        _imdbRating = str(obj.get("imdbRating"))
        _imdbID = str(obj.get("imdbID"))
        _links = [Link.from_dict(y) for y in obj.get("links")]
        return Episode(_episodeNumber, _title, _released, _releaseStamp, _duration, _imdbRating, _imdbID, _links)


@dataclass
class Quality:
    quality: str
    links: List[Link]

    @staticmethod
    def from_dict(obj: Any) -> 'Quality':
        _quality = str(obj.get("quality"))
        _links = [Link.from_dict(y) for y in obj.get("links")]
        return Quality(_quality, _links)


@dataclass
class Season:
    seasonNumber: int
    episodes: List[Episode]

    @staticmethod
    def from_dict(obj: Any) -> 'Season':
        _seasonNumber = int(obj.get("seasonNumber"))
        _episodes = [Episode.from_dict(y) for y in obj.get("episodes")]
        return Season(_seasonNumber, _episodes)


@dataclass
class DLinkItem:
    _id: str
    rawTitle: str
    type: str
    qualities: List[Quality]
    seasons: List[Season]
    posters: List[Poster]
    year: str

    @staticmethod
    def from_dict(obj: Any) -> 'DLinkItem':
        __id = str(obj.get("_id"))
        _rawTitle = str(obj.get("rawTitle"))
        _type = str(obj.get("type"))
        _qualities = [Quality.from_dict(y) for y in obj.get("qualities")]
        _seasons = [Season.from_dict(y) for y in obj.get("seasons")]
        _posters = [Poster.from_dict(y) for y in obj.get("posters")]
        _year = str(obj.get("year"))
        return DLinkItem(__id, _rawTitle, _type, _qualities, _seasons, _posters, _year)

    @property
    def id(self):
        return self._id