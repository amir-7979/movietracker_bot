from typing import List, Any
from dataclasses import dataclass


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
    type: str
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

    def to_string(self):
        rate: str = ''
        if self.rating.imdb != 0:
            rate = rate.__add__(f"🎖IMDb: {self.rating.imdb} ")
        if self.rating.metacritic != 0:
            rate = rate.__add__(f"|ⓂMeta: {self.rating.metacritic} ")
        if self.rating.rottenTomatoes != 0:
            rate = rate.__add__(f"|🍅RT: {self.rating.rottenTomatoes} ")
        if self.rating.myAnimeList != 0:
            rate = rate.__add__(f"|🏅myAnimeList: {self.rating.myAnimeList} ")
        if rate[0] == '|':
            rate = rate[1:]
        summary: str = ''
        if len(self.summary.persian) == 0:
            if len(self.summary.english) != 0:
                summary = f"📜 Summary: \n{self.summary.english}\n\n"
        else:
            summary = f"📜 Summary: \n{self.summary.persian}\n\n"
        year = ''
        if len(self.year) != 0:
            f"📅 Year : {self.year}\n\n"
        genre = ''
        if len(self.genres) != 0:
            genre = f"🎭 Genre : {', '.join(self.genres)}\n\n"

        website_url = f"https://movie-tracker-nine.vercel.app/movie/{self.s_id}/{self.rawTitle.replace(' ', '_')}"
        if len(self.year) != 0:
            website_url = website_url.__add__(f"-{self.year}")
        print(website_url)
        return f"🎬 {self.rawTitle}\n\n🔹 Type : {self.type.title().replace('_', ' ')}\n\n{rate}\n\n{year}{genre}{summary}[📥 download](https://t.me/MovieTracker1bot?start={self.s_id})\n\n[🌐 website]({website_url})"

    def get_url(self) -> str:
        return self.posters[0].url
