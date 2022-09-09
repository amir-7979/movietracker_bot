from typing import List
from typing import Any
from dataclasses import dataclass

from main import bot_token, client


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
class Summary:
    english: str
    persian: str

    @staticmethod
    def from_dict(obj: Any) -> 'Summary':
        english = str(obj.get("english"))
        persian = str(obj.get("persian"))
        return Summary(english, persian)


@dataclass
class LatestData:
    season: int
    episode: int
    quality: str
    hardSub: str
    dubbed: str
    censored: str
    subtitle: str
    watchOnlineLink: str

    @staticmethod
    def from_dict(obj: Any) -> 'LatestData':
        _season = int(obj.get("season"))
        _episode = int(obj.get("episode"))
        _quality = str(obj.get("quality"))
        _hardSub = str(obj.get("hardSub"))
        _dubbed = str(obj.get("dubbed"))
        _censored = str(obj.get("censored"))
        _subtitle = str(obj.get("subtitle"))
        _watchOnlineLink = str(obj.get("watchOnlineLink"))
        return LatestData(_season, _episode, _quality, _hardSub, _dubbed, _censored, _subtitle, _watchOnlineLink)


@dataclass
class Rating:
    imdb: float
    rottenTomatoes: int
    metacritic: int
    myAnimeList: int

    @staticmethod
    def from_dict(obj: Any) -> 'Rating':
        _imdb = float(obj.get("imdb"))
        _rottenTomatoes = int(obj.get("rottenTomatoes"))
        _metacritic = int(obj.get("metacritic"))
        _myAnimeList = int(obj.get("myAnimeList"))
        return Rating(_imdb, _rottenTomatoes, _metacritic, _myAnimeList)


@dataclass
class TelBotItem:
    s_id: str
    type2: str
    rawTitle: str
    posters: List[Poster]
    year: str
    premiered: str
    rating: Rating
    summary: Summary
    latest_data: LatestData
    genres: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'TelBotItem':
        s_id = str(obj.get("_id"))
        _type = str(obj.get("type"))
        _rawTitle = str(obj.get("rawTitle"))
        _posters = [Poster.from_dict(y) for y in obj.get("posters")]
        _year = str(obj.get("year"))
        _premiered = str(obj.get("premiered"))
        _rating = Rating.from_dict(obj.get("rating"))
        _summary = Summary.from_dict(obj.get('summary'))
        _latest_data = LatestData.from_dict(obj.get('latestData'))
        _genres = [y for y in obj.get("genres")]
        return TelBotItem(s_id, _type, _rawTitle, _posters, _year, _premiered, _rating, _summary, _latest_data, _genres)

    def to_string(self) -> str:
        return f"🎬 {self.rawTitle} \n\n🔹 Type : {self.type2} \n\n🎖IMDb: { self.rating.imdb} | ⓂMeta: {self.rating.metacritic} | 🍅RT: {self.rating.rottenTomatoes} \n\n📅 Year : {self.year} \n\n🎭 Genre : {', '.join(self.genres)} \n\n📜 Summary : \n{self.summary.persian}\n\n[download](https://api.telegram.org/bot<{bot_token}>/sendMessage?chat_id=<{client.get_peer_id()}>&text=Hello%20World)\n\n[github page](https://github.com/ashkan-esz/downloader_api)"


    def get_url(self) -> str:
        return self.posters[0].url
